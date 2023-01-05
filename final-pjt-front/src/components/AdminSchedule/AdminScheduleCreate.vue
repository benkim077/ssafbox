<template>
  <div>
    <h3>상영 스케줄 생성하기</h3>
    <form @submit.prevent="createScheduleItem">
      <label for="start_date">상영일 :</label>
      <input type="date" id="start_date" v-model="startDate" /><br />
      <label for="start_time">상영시간 :</label>
      <input type="time" id="start_time" v-model="startTime" /><br />
      <label for="movie">영화id :</label>
      <input type="text" id="movie" v-model="movie" /><br />
      <input type="submit" value="상영 스케줄 만들기" />
    </form>
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
export default {
  name: "AdminScheduleCreate",
  data() {
    return {
      startDate: null,
      startTime: null,
      movie: null,
    }
  },
  computed: {
    theaterId() {
      return this.$store.state.admin.theaterId
    },
    screenId() {
      return this.$store.state.admin.screenId
    },
  },
  methods: {
    createScheduleItem() {
      adminApi
        .createSchedule(
          this.theaterId,
          this.screenId,
          this.startDate,
          this.startTime,
          this.movie
        )
        .then((res) => {
          console.log(res)
          this.$store.commit("admin/PUSH_SCHEDULE_ITEM", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
