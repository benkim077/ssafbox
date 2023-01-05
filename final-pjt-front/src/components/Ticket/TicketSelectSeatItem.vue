<template>
  <div class="seats_container__div">
    <!-- 만약 is_reserved가 false 이면 ?? -->
    <div
      :class="{
        selectedSeatColor__div: selectedSeatNumber === this.seatItem.seat_no,
        isReservedSeatColor__div:
          this.seatItem.is_possible_to_reserve === false,
        seats_box_container__div: true,
      }"
      @click="selectSeat"
    >
      <div class="">{{ seatItem.seat_no }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TicketSelectSeatItem",
  props: {
    seatItem: Object,
  },
  computed: {
    selectedSeatNumber() {
      return this.$store.state.ticket.selectedSeatNumber
    },
  },
  methods: {
    selectSeat() {
      console.log(
        `(seat_no: ${this.seatItem.seat_no})번 좌석 선택됨! (seat_id: ${this.seatItem.id})`
      )
      // console.log(`번 좌석 선택됨!`)
      this.$store.commit("ticket/SET_SELECTED_SEAT_ID", this.seatItem.id)
      this.$store.commit("ticket/SET_SELECTED_SEAT_NO", this.seatItem.seat_no)
    },
  },
}
</script>

<style>
.seats_container__div {
  display: inline-block;
}
.seats_box_container__div {
  /* display: flex-block; */
  margin: 5px;
  width: 30px;
  height: 30px;
  border: 1px solid black;
}
/* .seats_box__div {
  justify-content: center;
  align-items: center;
} */

.selectedSeatColor__div {
  background-color: greenyellow;
}
.isReservedSeatColor__div {
  background-color: red;
}
</style>
