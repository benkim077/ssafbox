<template>
  <div>
    <h3>예매 정보 요약</h3>
    <ul>
      <li>극장 : {{ selectedTheaterData?.name }}</li>
      <li>날짜 : {{ ticketDataObject.selectedDate }}</li>
      <li>영화 : {{ ticketDataObject.selectedMovie }}</li>
      <li>
        날짜, 시간 :
        {{
          `${ticketDataObject.scheduleItem.start_date} - ${ticketDataObject.scheduleItem.start_time}`
        }}
      </li>
      <li>좌석 번호 : {{ ticketDataObject.selectedSeatNumber }}</li>
    </ul>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
export default {
  name: "PaymentOverall",
  data() {
    return {
      selectedTheaterData: null,
    }
  },
  computed: {
    ticketDataObject() {
      return {
        selectedTheaterId: this.$store.state.ticket.selectedTheaterId,
        selectedDate: this.$store.state.ticket.selectedDate,
        selectedMovie: this.$store.state.ticket.selectedMovie,
        scheduleItem: this.$store.state.ticket.scheduleItem,
        selectedSeatNumber: this.$store.state.ticket.selectedSeatNumber,
      }
    },
  },
  methods: {
    readTheaterItem(theater_id) {
      ticketApi
        .readTheaterItem(theater_id)
        .then((res) => {
          this.selectedTheaterData = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.readTheaterItem(this.ticketDataObject.selectedTheaterId)
  },
}
</script>

<style></style>
