<template>
  <div>
    <li>영화: {{ reservedTicketItem.schedule.movie.title }}</li>
    <li>상영관: {{ reservedTicketItem.schedule.screen }}관</li>
    <li>상영일: {{ reservedTicketItem.schedule.start_date }}</li>
    <li>상영 시간: {{ reservedTicketItem.schedule.start_time }}</li>
    <li>좌석번호: {{ reservedTicketItem.seat_no }}번</li>
    <hr />
  </div>
</template>

<script>
export default {
  name: "ReservedTicketItem",
  props: {
    reservedTicketItem: Object,
  },
}
</script>

<style>
.no_decoration__ul {
  list-style-type: none;
}
</style>
