<template>
  <div>
    <p>2__날짜를 선택하세요.</p>
    <ticket-date-list></ticket-date-list>
  </div>
</template>

<script>
import TicketDateList from "./TicketDateList.vue"
export default {
  components: { TicketDateList },
  name: "TicketDateSelector",
}
</script>

<style></style>
