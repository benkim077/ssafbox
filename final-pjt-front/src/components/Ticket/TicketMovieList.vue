<template>
  <div>
    <ul>
      <ticket-movie-list-item
        v-for="(movieItem, idx) in movieList"
        :key="`movieItem-${idx}`"
        :movieItem="movieItem"
      ></ticket-movie-list-item>
    </ul>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
import TicketMovieListItem from "./TicketMovieListItem.vue"
export default {
  components: { TicketMovieListItem },
  name: "TicketMovieList",
  data() {
    return {
      movieList: [],
    }
  },
  computed: {
    selectedTheaterId() {
      return this.$store.state.ticket.selectedTheaterId
    },
    selectedDate() {
      return this.$store.state.ticket.selectedDate
    },
  },
  watch: {
    selectedTheaterId() {
      this.getDateList()
    },
    selectedDate() {
      this.getMovieList()
    },
  },
  methods: {
    getDateList() {
      // TicketDateList.vue 에서 가져오기
      ticketApi
        .getAvailableDate(this.selectedTheaterId)
        .then((res) => {
          // console.log(res)
          this.dateList = res.data.dates
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovieList() {
      // Movie List를 받아서 data에 저장하는 함수
      ticketApi
        .getAvailableMovie(this.selectedTheaterId, this.selectedDate)
        .then((res) => {
          console.log("영화 목록", res.data)
          this.movieList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
