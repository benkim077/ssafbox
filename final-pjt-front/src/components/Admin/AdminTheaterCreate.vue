<template>
  <div>
    <h3>극장 생성</h3>
    <form @submit.prevent="createTheater">
      <label for="name">극장 이름 입력</label>
      <input type="text" id="name" v-model="name" /><br />
      <label for="location">극장 위치 입력</label>
      <input type="text" id="location" v-model="location" /><br />
      <input type="submit" value="새 극장 생성" />
    </form>
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
export default {
  name: "AdminTheaterCreate",
  data() {
    return {
      name: "",
      location: "",
    }
  },
  methods: {
    createTheater() {
      adminApi
        .createTheater(this.name, this.location)
        .then((res) => {
          console.log(res)
          this.$store.commit("admin/PUSH_THEATER_ITEM", res.data)
          // this.$router.push({ name: "adminTheater" }).catch(() => {})
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
