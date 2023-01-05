<template>
  <div>
    <p>5__좌석을 선택하세요.</p>
    <ticket-select-seat-list></ticket-select-seat-list><br />
    <button @click="createOccupation">결제하기(자리점유)</button>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
import TicketSelectSeatList from "@/components/Ticket/TicketSelectSeatList.vue"
export default {
  components: { TicketSelectSeatList },
  name: "TicketSelectSeatView",
  computed: {
    selectedSeatId() {
      return this.$store.state.ticket.selectedSeatId
    },
  },
  methods: {
    createOccupation() {
      if (this.selectedSeatId === null) {
        alert("좌석을 선택해주세요.")
      } else {
        ticketApi
          .occupySeat(this.selectedSeatId)
          .then((res) => {
            if (res.data.message === "success") {
              this.$router.push({ name: "payment" })
            } else {
              alert("이미 결제된 좌석입니다. 다른 좌석을 선택해주세요.")
              this.$router.push({ name: "seat" }).catch(() => {})
            }
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
  },
}
</script>

<style></style>
