<template>
  <div>
    <form @submit.prevent="createScreen">
      <label for="seatNumbers">좌석 수 입력: </label>
      <input type="text" id="seatNumbers" v-model="seatNumbers" />
      <span></span>
      <input type="submit" value="생성" />
    </form>
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
export default {
  name: "AdminScreenCreate",
  data() {
    return {
      seatNumbers: null,
    }
  },
  computed: {
    theaterId() {
      return this.$store.state.admin.theaterId
    },
  },
  methods: {
    createScreen() {
      adminApi
        .createScreen(this.theaterId, this.seatNumbers)
        .then((res) => {
          console.log(res)
          this.$store.commit("admin/PUSH_SCREEN_ITEM", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
