<template>
  <div id="login-container">
    <div class="login-content">
      <div class="image-container">
        <img src="../../public/pub01.jpg" alt="宣传图片" class="promo-image">
      </div>
      <div class="login-box">
        <h2 class="login-title">智慧食安管理系统</h2>
        <input v-model="username" type="text" placeholder="用户名" class="login-input">
        <input v-model="password" type="password" placeholder="密码" class="login-input">
        <button @click="login" class="login-button">登录</button>
      </div>
    </div>
    <div class="footer">
      <p class="footer-text">版权所有 © 2023 智慧食安管理系统</p>
      <p class="footer-text">中国高校计算机大赛 网络技术挑战赛</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      if (this.username === "admin" && this.password === "123456") {
        // Emit a custom event to notify parent component (App.vue) of login success
        this.$emit("login-success");
      } else {
        alert("登录失败，请检查用户名和密码");
      }
    },
  },
};
</script>

<style scoped>
#login-container {
  background-image: url("../../public/background-image.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-content {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80%;
  max-width: 1200px;
  margin: 0 auto;
}

.image-container {
  flex: 1;
  padding: 30px;
}

.promo-image {
  max-width: 100%;
  border-radius: 15px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

.login-box {
  flex: 1;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.login-title {
  font-size: 28px;
  margin-bottom: 30px;
}

.login-input {
  display: block;
  width: 100%;
  padding: 15px;
  margin: 15px 0;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 16px;
}

.login-button {
  background-color: #21b3b9;
  color: white;
  border: none;
  padding: 15px 25px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 18px;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #1a8e96;
}

.footer {
  background-color: rgba(255, 255, 255, 0.9);
  padding: 10px;
  text-align: center;
  position: absolute;
  bottom: 0;
  width: 100%;
}
</style>
