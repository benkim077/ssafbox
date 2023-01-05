<template>
  <div>
    <ul>
      <ticket-date-list-item
        v-for="(dateItem, idx) in dateList"
        :key="`dateItem-${idx}`"
        :dateItem="dateItem"
      ></ticket-date-list-item>
    </ul>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
import TicketDateListItem from "./TicketDateListItem.vue"
export default {
  components: { TicketDateListItem },
  name: "TicketDateList",
  data() {
    return {
      dateList: [],
    }
  },
  computed: {
    selectedTheaterId() {
      return this.$store.state.ticket.selectedTheaterId
    },
  },
  watch: {
    selectedTheaterId() {
      // 선택된 극장이 바뀌면 선택할 수 있는 날짜도 바뀌도록 watch 구현
      this.getDateList()
    },
  },
  methods: {
    getDateList() {
      ticketApi
        .getAvailableDate(this.selectedTheaterId)
        .then((res) => {
          console.log("날짜 목록", res.data)
          this.dateList = res.data.dates
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
