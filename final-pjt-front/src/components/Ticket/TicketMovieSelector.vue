<template>
  <div>
    <p>3__영화를 선택하세요.</p>
    <ticket-movie-list></ticket-movie-list>
  </div>
</template>

<script>
import TicketMovieList from "./TicketMovieList.vue"
export default {
  components: { TicketMovieList },
  name: "TicketMovieSelector",
}
</script>

<style></style>
