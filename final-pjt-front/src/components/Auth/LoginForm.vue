<template>
  <div>
    <form @submit.prevent="requestLogin">
      <label for="input_id__input">아이디: </label>
      <input
        type="text"
        id="input_id__input"
        v-model="username"
        required
      /><br />
      <label for="input_password__input">비밀번호: </label>
      <input
        type="password"
        id="input_password__input"
        v-model="password"
        required
      /><br />
      <input type="submit" value="로그인" />
    </form>
  </div>
</template>

<script>
import * as authApi from "@/api/auth"

export default {
  name: "LoginForm",
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    requestLogin() {
      console.log("로그인 요청 함수 실행")
      const username = this.username
      const password = this.password

      authApi
        .login(username, password)
        .then((res) => {
          console.log(res)
          this.$router.push({ name: "index" })
        })
        .catch((err) => {
          if (
            err.response.data.non_field_errors[0] ===
            "Unable to log in with provided credentials."
          ) {
            alert("아이디 또는 비밀번호가 틀렸습니다. 다시 로그인 해주세요.")
          }
        })
    },
  },
}
</script>

<style></style>
