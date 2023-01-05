<template>
  <div id="app">
    <app-header></app-header>
    <header-link-list></header-link-list>
    <hr />
    <router-view />
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue"
import HeaderLinkList from "./components/HeaderLinkList.vue"
export default {
  components: { AppHeader, HeaderLinkList },
  name: "App",
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

span {
  padding: 15px;
}

nav a {
  font-weight: bold;
  color: #503396;
  text-decoration: none;
}

h1 {
  color: #503396;
}

.container {
  display: grid;
}
</style>
