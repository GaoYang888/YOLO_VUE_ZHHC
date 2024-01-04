<template>
  <div id="app">
    <!-- Conditional rendering based on login status -->
    <div v-if="isLoggedIn">
      <app-header></app-header>
      <app-content></app-content>
      <app-footer></app-footer>
    </div>
    <div v-else>
      <app-login @login-success="handleLoginSuccess"></app-login>
    </div>
  </div>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import Content from "./components/Content";
import Login from "./components/Login.vue";

export default {
  name: "Smart Kitchen Management System",
  components: {
    "app-header": Header,
    "app-footer": Footer,
    "app-content": Content,
    "app-login": Login,
  },
  data() {
    return {
      isLoggedIn: false, // Initial login status
    };
  },
  methods: {
    handleLoginSuccess() {
      this.isLoggedIn = true; // Set login status to true when login is successful
    },
  },
};
</script>

<style scoped>
/* Your styles here */
</style>
