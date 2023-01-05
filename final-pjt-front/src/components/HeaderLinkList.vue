<template>
  <div>
    <nav>
      <span>
        <router-link :to="{ name: 'index' }">메인페이지</router-link>
      </span>
      <span v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">로그인</router-link>
      </span>
      <span v-if="isLoggedIn">
        <a @click.prevent="requestLogout" class="mouser_hover_pointer__a"
          >로그아웃</a
        >
      </span>
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'ticket' }">예매하기</router-link>
      </span>
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'check' }">예매확인</router-link>
      </span>
      <span v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">회원가입</router-link>
      </span>
      <span v-if="isLoggedIn && isAdmin">
        <router-link :to="{ name: 'admin' }">Admin</router-link>
      </span>
    </nav>
  </div>
</template>

<script>
export default {
  name: "HeaderLinkList",
  methods: {
    requestLogout() {
      this.$store.commit("auth/DELETE_ACCESS_TOKEN")
      this.$store.commit("auth/DELETE_REFRESH_TOKEN")
      this.$router.push({ name: "index" }).catch(() => {})
    },
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters["auth/isLoggedIn"]
    },
    isAdmin() {
      return true
    },
  },
}
</script>

<style>
.mouser_hover_pointer__a {
  cursor: pointer;
}
</style>
