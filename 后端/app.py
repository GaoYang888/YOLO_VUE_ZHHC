import datetime
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *
from processor.AIDetector_pytorch import Detector

import core.main

# 引用config.py文件
from config import *
import math

# 为方便打包，路径引用方式改为自动获取
import os
import sys
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(PROJECT_DIR, 'uploads')

ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'secret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='index.html'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    print(datetime.datetime.now(), file.filename)
    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)
        shutil.copy(src_path, PROJECT_DIR+'/tmp/original')
        image_path = os.path.join(PROJECT_DIR+'/tmp/original', file.filename)
        pid, image_info = core.main.c_main(
            image_path, current_app.model, file.filename.rsplit('.', 1)[1])
        delete_file(file.filename)
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/tmp/original/' + pid,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
                        'image_info': image_info})

    return jsonify({'status': 0})

def delete_file(filename):
    os.remove(app.config['UPLOAD_FOLDER']+'/'+filename)

@app.route('/testdb', methods=['GET', 'POST'])
def testdb():
    db = SQLManager()
    show_data_db = db.get_list('SELECT * FROM imginfo ')
    db.close()
    return jsonify({'status': 1,
                    'historical_data': show_data_db})

@app.route('/testdbow', methods=['GET', 'POST'])
def testdbow():
    db = SQLManager()
    show_data_ow_db = db.get_list('SELECT * FROM testoverview ')
    db.close()
    return jsonify({'status': 1,
                    'testoverview': show_data_ow_db})

@app.route('/testdb1', methods=['GET', 'POST'])
def testdb1():
    db = SQLManager()
    show_data_db1 = db.get_list('SELECT * FROM imginfo ')
    db.close()
    return render_template('testdb.html', show_data_db1=show_data_db1)

def convertdata(image_info):
    str = image_info
    return str

@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if not file is None:
            image_data = open(PROJECT_DIR+f'/tmp/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response

if __name__ == '__main__':
    with app.app_context():
        current_app.model = Detector()
    app.run(host='127.0.0.1', port=5003, debug=True)
