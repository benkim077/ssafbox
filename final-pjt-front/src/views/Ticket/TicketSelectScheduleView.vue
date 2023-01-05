<template>
  <div>
    <div><ticket-theater-selector></ticket-theater-selector></div>
    <hr />
    <div><ticket-date-selector></ticket-date-selector></div>
    <hr />
    <div><ticket-movie-selector></ticket-movie-selector></div>
    <hr />
    <div><ticket-schedule-selector></ticket-schedule-selector></div>
    <hr />
    <button @click="routeSelectSeat">좌석 선택하러 가기</button>
  </div>
</template>

<script>
import TicketTheaterSelector from "@/components/Ticket/TicketTheaterSelector.vue"
import TicketDateSelector from "@/components/Ticket/TicketDateSelector.vue"
import TicketMovieSelector from "@/components/Ticket/TicketMovieSelector.vue"
import TicketScheduleSelector from "@/components/Ticket/TicketScheduleSelector.vue"
export default {
  name: "TicketSelectScheduleView",
  components: {
    TicketTheaterSelector,
    TicketDateSelector,
    TicketMovieSelector,
    TicketScheduleSelector,
  },
  computed: {
    scheduleItem() {
      return this.$store.state.ticket.scheduleItem
    },
  },
  methods: {
    routeSelectSeat() {
      if (this.scheduleItem === null) {
        alert("상영 스케줄을 선택하세요.")
      } else {
        this.$router.push({ name: "seat" })
      }
    },
  },
}
</script>

<style></style>
