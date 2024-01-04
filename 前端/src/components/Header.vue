<template>
  <div id="Header">
    <div class="nav">
      <router-link to="/" class="nav-item">首页</router-link>
      <router-link to="/monitor" class="nav-item">食安监控</router-link>
      <router-link to="/other" class="nav-item">其他</router-link>
    </div>
    <div class="title">
      <h1>基于YOLO算法的食安后厨人员行为规范预警监管系统</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
#Header {
  background: #ffffffae;
  padding: 6px;
  border-radius: 5px;
  width: 88%;
  height: 146px;
  margin: 20px auto;
  padding: 30px 0 20px 40px;
}

.nav {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.nav-item {
  color: #21b3b9;
  font-weight: bold;
  text-decoration: none;
  font-size: 20px;
}

.title h1 {
  color: #21b3b9;
  font-size: 30px;
  margin-top: -10px;
}
</style>
