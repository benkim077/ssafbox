<template>
  <div>
    <ul>
      <ticket-schedule-list-item
        v-for="(scheduleItem, idx) in scheduleList"
        :key="`scheduleItem-${idx}`"
        :scheduleItem="scheduleItem"
      ></ticket-schedule-list-item>
    </ul>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
import TicketScheduleListItem from "./TicketScheduleListItem.vue"
export default {
  components: { TicketScheduleListItem },
  name: "TicketScheduleList",
  data() {
    return {
      scheduleList: [],
    }
  },
  computed: {
    selectedTheaterId() {
      return this.$store.state.ticket.selectedTheaterId
    },
    selectedDate() {
      return this.$store.state.ticket.selectedDate
    },
    selectedMovie() {
      return this.$store.state.ticket.selectedMovie
    },
    areTheaterAndDateAndMovieSelected() {
      // Theater, Date, Movie가 전부 선택되었는지 확인하는 computed
      return this.selectedTheaterId && this.selectedDate && this.selectedMovie
    },
  },
  watch: {
    // 만약 selectedTheaterId && selectedDate && selectedMovie === false 이라면, 이 함수들은 실행되지 않도록 리팩토링
    selectedTheaterId() {
      if (this.areTheaterAndDateAndMovieSelected) {
        this.getScheduleList()
      }
    },
    selectedDate() {
      if (this.areTheaterAndDateAndMovieSelected) {
        this.getScheduleList()
      }
    },
    selectedMovie() {
      if (this.areTheaterAndDateAndMovieSelected) {
        this.getScheduleList()
      }
    },
  },
  methods: {
    getScheduleList() {
      ticketApi
        .getAvailableSchedule(
          this.selectedTheaterId,
          this.selectedDate,
          this.selectedMovie
        )
        .then((res) => {
          console.log("상영 시간 목록", res.data)
          this.scheduleList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
