<template>
  <div>
    <a @click="goTheaterManageView">[뒤로 가기]</a>
    <h2>{{ theaterId }} 극장의 {{ screenId }} 상영관 관리</h2>

    <div>
      <form @submit.prevent="updateScreen">
        <h3>상영관 수용 인원 변경하기</h3>
        <p>현재 수용 인원 : {{ seatItem?.seats }}</p>
        <label for="seatNumbers">인원 입력</label>
        <input type="text" id="seatNumbers" v-model="inputSeatNumber" />
        <span></span>
        <input type="submit" value="변경" />
      </form>
    </div>
    <div>
      <button @click="deleteScreen">상영관 삭제</button>
    </div>
    <div>
      <admin-schedule-create></admin-schedule-create>
      <admin-schedule-list></admin-schedule-list>
    </div>
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
import AdminScheduleCreate from "@/components/AdminSchedule/AdminScheduleCreate.vue"
import AdminScheduleList from "@/components/AdminSchedule/AdminScheduleList.vue"
export default {
  components: { AdminScheduleCreate, AdminScheduleList },
  name: "AdminScreenManageView",
  data() {
    return {
      theaterId: null,
      screenId: null,
      seatItem: null,
      inputSeatNumber: null,
    }
  },
  methods: {
    goTheaterManageView() {
      this.$router.push({
        name: "manageTheater",
        params: { theaterId: this.theaterId },
      })
    },
    updateScreen() {
      adminApi
        .updateScreenItem(this.theaterId, this.screenId, this.inputSeatNumber)
        .then((res) => {
          console.log(res)
          this.seatItem.seats = res.data.seats
          this.inputSeatNumber = null
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteScreen() {
      adminApi
        .deleteScreenItem(this.theaterId, this.screenId)
        .then((res) => {
          console.log(res)
          this.$router.push({
            name: "manageTheater",
            params: { id: this.theaterId },
          })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getId() {
      const routingData = this.$route.params
      this.theaterId = routingData.theaterId
      this.screenId = routingData.screenId

      this.$store.commit("admin/STORE_THEATER_ID", this.theaterId)
      this.$store.commit("admin/STORE_SCREEN_ID", this.screenId)
    },
    getScreenItem() {
      adminApi
        .getScreenItem(this.theaterId, this.screenId)
        .then((res) => {
          this.seatItem = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getId()
    this.getScreenItem()
  },
}
</script>

<style></style>
