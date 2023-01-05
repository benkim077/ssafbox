<template>
  <div>
    <h2>로그인</h2>
    <login-form></login-form>
  </div>
</template>

<script>
import LoginForm from "@/components/Auth/LoginForm.vue"

export default {
  components: { LoginForm },
  name: "LoginView",
}
</script>

<style></style>
