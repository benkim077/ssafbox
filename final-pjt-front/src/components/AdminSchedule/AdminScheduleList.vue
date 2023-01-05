<template>
  <div>
    <h3>상영 스케줄 목록</h3>
    <div>
      <admin-schedule-list-item
        v-for="scheduleItem in scheduleList"
        :key="scheduleItem.id"
        :scheduleItem="scheduleItem"
      >
      </admin-schedule-list-item>
    </div>
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
import AdminScheduleListItem from "./AdminScheduleListItem.vue"
export default {
  components: { AdminScheduleListItem },
  name: "AdminScheduleList",
  data() {
    return {
      scheduleList: [],
    }
  },
  computed: {
    theaterId() {
      return this.$store.state.admin.theaterId
    },
    screenId() {
      return this.$store.state.admin.screenId
    },
    computedScheduleList() {
      return this.$store.getters["admin/getScheduleList"]
    },
  },
  watch: {
    computedScheduleList(value) {
      this.scheduleList = value
    },
  },
  methods: {
    getScheduleList() {
      adminApi
        .getScheduleList(this.theaterId, this.screenId)
        .then((res) => {
          this.$store.commit("admin/SET_SCHEDULE_LIST", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getScheduleList()
  },
}
</script>

<style></style>
