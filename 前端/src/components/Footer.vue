<template>
  <div id="footer" @click="changeMood" @mouseleave="changeMood">
    <p class="footer-text">{{ message }}</p>
    <p class="footer-owner">版权所有 © 2023 智慧食安管理系统</p>
    <p class="footer-owner">中国高校计算机大赛 网络技术挑战赛</p>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      message: "食品安全，健康无忧。",
    };
  },
  methods: {
    changeMood() {
      const arr = [
        "食品安全，健康无忧。",
        "保障食品安全，关爱每一口。",
        "美味源于安全，安全才能放心。",
        "食品安全，家庭幸福。",
        "关爱食品安全，共筑健康生活。",
      ];
      this.message = arr[Math.floor(Math.random() * 5)];
    },
  },
};
</script>


<style scoped>
#footer {
  background: #f5f5f5;
  padding: 20px 0;
  text-align: center;
  border-radius: 10px;
}

.footer-text {
  color: #333;
  font-size: 20px;
  margin: 10px 0;
  transition: color 0.3s;
}

.footer-text:hover {
  color: #21b3b9;
}

.footer-owner {
  color: #777;
  font-size: 14px;
  margin-top: 5px;
}
</style>
