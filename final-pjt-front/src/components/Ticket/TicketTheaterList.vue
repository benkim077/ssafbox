<template>
  <div>
    <ul>
      <ticket-theater-list-item
        v-for="theaterItem in theaterList"
        :key="theaterItem.id"
        :theaterItem="theaterItem"
      ></ticket-theater-list-item>
    </ul>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
import TicketTheaterListItem from "./TicketTheaterListItem.vue"
export default {
  components: { TicketTheaterListItem },
  name: "TicketTheaterList",
  data() {
    return {
      theaterList: [],
    }
  },
  methods: {
    getTheaterList() {
      ticketApi
        .getAvailbleTheater()
        .then((res) => {
          console.log(`극장 목록:`, res.data)
          this.theaterList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getTheaterList()
  },
}
</script>

<style></style>
