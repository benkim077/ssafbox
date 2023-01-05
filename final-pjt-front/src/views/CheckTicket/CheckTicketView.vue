<template>
  <div>
    <h2>예매 확인</h2>
    <reserved-ticket-list></reserved-ticket-list>
  </div>
</template>

<script>
import ReservedTicketList from "@/components/CheckTicket/ReservedTicketList.vue"
export default {
  components: { ReservedTicketList },
  name: "CheckTicketView",
}
</script>

<style></style>
