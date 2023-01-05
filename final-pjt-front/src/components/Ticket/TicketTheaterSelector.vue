<template>
  <div>
    <p>1__극장을 선택하세요.</p>
    <ticket-theater-list></ticket-theater-list>
  </div>
</template>

<script>
import TicketTheaterList from "./TicketTheaterList.vue"
export default {
  components: { TicketTheaterList },
  name: "TicketTheaterSelector",
}
</script>

<style></style>
