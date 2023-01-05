<template>
  <div>
    <h2>회원가입</h2>
    <sign-up-form />
  </div>
</template>

<script>
import SignUpForm from "@/components/Auth/SignUpForm.vue"
export default {
  components: { SignUpForm },
  name: "SignUpView",
}
</script>

<style></style>
