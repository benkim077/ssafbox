<template>
  <div>
    <div>스케줄 id : {{ scheduleItem__data.id }}</div>
    <div>스케줄 시작일: {{ scheduleItem__data.start_date }}</div>
    <div>스케줄 시작 시간: {{ scheduleItem__data.start_time }}</div>
    <form v-if="isUpdateForm" @submit.prevent="updateSchedule">
      <label for="date">날짜 입력: </label>
      <input type="date" id="date" v-model="inputDate" />
      <label for="time">시간 입력: </label>
      <input type="time" id="time" v-model="inputTime" />
      <input type="submit" value="스케줄 변경하기" />
    </form>
    <div>
      <button @click="toggleFormElement">상영 스케줄 변경</button>
      <span></span>
      <button @click="deleteSchedule">상영 스케줄 삭제</button>
    </div>
    <br />
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
export default {
  name: "AdminScheduleListItem",
  data() {
    return {
      isUpdateForm: false,
      inputDate: null,
      inputTime: null,
      scheduleItem__data: null,
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
  props: {
    scheduleItem: Object,
  },
  methods: {
    updateSchedule() {
      adminApi
        .updateScheduleItem(
          this.theaterId,
          this.screenId,
          this.scheduleItem.id,
          this.inputDate,
          this.inputTime
        )
        .then((res) => {
          this.scheduleItem__data = res.data
          console.log(res)
          this.toggleFormElement()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    toggleFormElement() {
      this.isUpdateForm = !this.isUpdateForm
    },
    deleteSchedule() {
      adminApi
        .deleteScheduleItem(this.theaterId, this.screenId, this.scheduleItem.id)
        .then((res) => {
          console.log(res)
          this.$store.commit("admin/DELETE_SCHEDULE_ITEM", this.scheduleItem)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.scheduleItem__data = this.scheduleItem
  },
}
</script>

<style></style>
