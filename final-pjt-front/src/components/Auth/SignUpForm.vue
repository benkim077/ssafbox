<template>
  <div>
    <form @submit.prevent="requestSignUp">
      <label for="id">아이디 입력 : </label>
      <input type="text" id="id" v-model="username" required /><br />
      <label for="pw1">비밀번호 입력 : </label>
      <input type="password" id="pw1" v-model="password1" required /><br />
      <label for="pw2">비밀번호 재입력 : </label>
      <input type="password" id="pw2" v-model="password2" required /><br />
      <input type="submit" value="회원가입하기" />
    </form>
  </div>
</template>

<script>
import * as authApi from "@/api/auth"

export default {
  name: "SignUpForm",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    requestSignUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      authApi
        .signup(username, password1, password2)
        .then((res) => {
          console.log(res.status, res.statusText)
          this.$router.push({
            name: "index",
          })
        })
        .catch((err) => {
          console.log(err)
          const passwordChecker =
            /^(?=.*[a-zA-Z])(?=.*[!@#$%^&*=-])(?=.*[0-9]).{8,25}$/
          if (!passwordChecker.test(password1)) {
            alert(
              "비밀번호는 영문자, 숫자, 특수문자 조합으로 8-25자리를 사용해야 합니다."
            )
            return false
          }
          if (password1 !== password2) {
            alert("비밀번호가 일치하지 않습니다.")
          }
        })
    },
  },
}
</script>

<style></style>
