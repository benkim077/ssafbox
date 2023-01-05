<template>
  <div>
    <p>4__상영 시간을 선택하세요.</p>
    <ticket-schedule-list></ticket-schedule-list>
  </div>
</template>

<script>
import TicketScheduleList from "./TicketScheduleList.vue"
export default {
  components: { TicketScheduleList },
  name: "TicketSchduleSelector",
}
</script>

<style></style>
