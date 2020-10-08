<template>
  <div id="app">
    <Header :isHeader="isHeader" />
    <router-view />
  </div>
</template>

<script src="https://use.fontawesome.com/releases/v5.2.0/js/all.js"></script>
<script>
import "./assets/css/style.scss";
import Header from "./components/common/Header.vue";

export default {
  name: "App",
  components: {
    Header,
  },
  data: function () {
    return {
      isHeader: true,
    };
  },
  created () {
    // 탭 타이틀 변경
    document.title = "Omok Jmok"
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
