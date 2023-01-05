<template>
  <div class="seat-list-warapper__div">
    <ticket-select-seat-item
      v-for="seatItem in seatList"
      :key="`seatItem-${seatItem.id}`"
      :seatItem="seatItem"
    ></ticket-select-seat-item>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
import TicketSelectSeatItem from "./TicketSelectSeatItem.vue"
export default {
  components: { TicketSelectSeatItem },
  name: "TicketSelectSeatList",
  data() {
    return {
      seatList: [],
    }
  },
  computed: {
    selectedscheduleId() {
      return this.$store.state.ticket.scheduleItem.id
    },
    // seatListPerTenSeats() {
    //   // 2차원 배열을 리턴하고 싶다.
    //   const arr = []
    //   const SeatListLength = this.seatList.length
    //   let i = 0

    //   while (i <= SeatListLength) {
    //     if (i % 10 == 9) {
    //       console.log(Array(this.seatList.slice(i - 9, i + 1)))
    //       arr.push(Array(this.seatList.slice(i - 9, i + 1)))
    //     }
    //     i++
    //   }
    //   return arr
    // },
  },
  methods: {
    getSeatList() {
      ticketApi
        .getAvailableSeatList(this.selectedscheduleId)
        .then((res) => {
          console.log(`${this.selectedscheduleId} 번 스케줄 좌석 화면`)
          console.log("-----좌석 목록-----", res.data)
          this.seatList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getSeatList()
    // console.log("><<<<<<<<<<<<<<<", this.seatListPerTenSeats)
  },
}
</script>

<style>
.seat-list-warapper__div {
  border: 1px solid black;
  width: 430px;
}
</style>
