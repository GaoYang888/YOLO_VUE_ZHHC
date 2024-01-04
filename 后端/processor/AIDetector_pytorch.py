# 本模块为检测核心模块
# --设置各种参数，导入模型
# --绘制检测框
# --返回监测数据
# --数据库操作
# 代码优化【正在进行】
# 最后编译时间 2023-05-09
# 存在问题【暂无】

import datetime
import torch
import numpy as np
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords, letterbox
from utils.torch_utils import select_device
import cv2
from random import randint

#引用config.py文件
from config import *
import math

#为方便打包，路径引用方式改为自动获取
import os
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
WEIGHTS_DIR = os.path.join(PROJECT_DIR,"..\\weights")

class Detector(object):

    # 设定检测参数
    def __init__(self):
        self.img_size = 640 # 表示图像的输入尺寸，即将输入图像的宽和高都调整为640像素。
        self.threshold = 0.3 # 表示目标检测的置信度阈值，即只有置信度大于0.4的目标才会被检测出来。
        self.max_frame = 30 # 表示最大的帧数，即最多处理160帧图像。
        self.init_model()

    def init_model(self):
        self.weights = WEIGHTS_DIR+'\\'+'yolov5s.pt'
        # self.weights = WEIGHTS_DIR+'\\'+'model_a.pt'
        # self.weights = 'weights/yolov5s.pt'
        self.device = '0' if torch.cuda.is_available() else 'cpu'
        self.device = select_device(self.device)
        model = attempt_load(self.weights, map_location=self.device)
        model.to(self.device).eval()
        model.half()
        # torch.save(model, 'test.pt')
        self.m = model
        self.names = model.module.names if hasattr(
            model, 'module') else model.names
        self.colors = [
            (randint(0, 255), randint(0, 255), randint(0, 255)) for _ in self.names
        ]

    def preprocess(self, img):

        img0 = img.copy()
        img = letterbox(img, new_shape=self.img_size)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.half()  # 半精度
        img /= 255.0  # 图像归一化
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        return img0, img

    def plot_bboxes(self, image, bboxes, line_thickness=None):
        tl = line_thickness or round(
            0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
        for (x1, y1, x2, y2, cls_id, conf) in bboxes:
            #if self.names.index(cls_id) == 0 : #只过滤【人】
            color = self.colors[self.names.index(cls_id)]
            c1, c2 = (x1, y1), (x2, y2)
            cv2.rectangle(image, c1, c2, color,
                        thickness=tl, lineType=cv2.LINE_AA)
            tf = max(tl - 1, 1)  # font thickness
            t_size = cv2.getTextSize(
                cls_id, 0, fontScale=tl / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
            cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
            cv2.putText(image, '{} ID-{:.2f}'.format(cls_id, conf), (c1[0], c1[1] - 2), 0, tl / 3,
                [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
                
        return image

    def detect(self, im):
        im0, img = self.preprocess(im)
        pred = self.m(img)[0]  # 修改模型输出，去掉增强
        pred = pred.float()
        pred = non_max_suppression(pred, self.threshold, 0.3)

        pred_boxes = []
        image_info = {}
        count = 0
        db = SQLManager()  # 创建数据库连接
        try:
            for det in pred:
                if det is not None and len(det):
                    det[:, :4] = scale_coords(
                        img.shape[2:], det[:, :4], im0.shape).round()

                    for *x, conf, cls_id in det:
                        lbl = self.names[int(cls_id)]  # 用个中间参来保存人物类型名称
                        x1, y1 = int(x[0]), int(x[1])
                        x2, y2 = int(x[2]), int(x[3])
                        pred_boxes.append((x1, y1, x2, y2, lbl, conf))

                        #if lbl == "person":  # 只输出【人】
                        count += 1
                        key = '{}-{:02}'.format(lbl, count)  # 输出类型和编号
                        image_info[key] = ['{}×{}'.format(x2-x1, y2-y1), np.round(float(conf), 3)]

                        # 数据库操作
                        target_width = x2 - x1
                        target_height = y2 - y1
                        confidence = np.round(float(conf), 3)
                        detection_timestamp = datetime.datetime.now().replace(microsecond=0)
                        sql = 'INSERT INTO imginfo (target_type_and_id, target_width, target_height, confidence, detection_timestamp) VALUES (%s, %s, %s, %s, %s);'
                        values = (key, target_width, target_height, confidence, detection_timestamp)
                        db.moddify(sql, values)

            im = self.plot_bboxes(im, pred_boxes)

            # 添加时间戳
            cut_off_rule = '-----'
            datatimenow = datetime.datetime.now().replace(microsecond=0)
            sql = 'INSERT INTO imginfo (target_type_and_id, target_width, target_height, confidence, detection_timestamp) VALUES (%s, %s, %s, %s, %s);'
            values = (cut_off_rule, 0, 0, 0, datatimenow)
            sqlow = 'INSERT INTO testoverview (timestamp, count) VALUES (%s, %s);'
            valuesow = (datatimenow, count)
            db.moddify(sql, values)
            db.moddify(sqlow, valuesow)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            db.close()

        return im, image_info







