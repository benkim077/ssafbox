<template>
  <div>
    <ul>
      <reserved-ticket-item
        v-for="reservedTicketItem in reservedTicketList"
        :key="`reservedTicketItem-${reservedTicketItem.order_set[0].id}`"
        :reservedTicketItem="reservedTicketItem"
      ></reserved-ticket-item>

      <p v-if="emptyListNotificationMessage">
        {{ emptyListNotificationMessage }}
      </p>
    </ul>
  </div>
</template>

<script>
import * as checkTicketApi from "@/api/checkTicket"
import ReservedTicketItem from "./ReservedTicketItem.vue"
export default {
  components: { ReservedTicketItem },
  name: "ReservedTicketList",
  data() {
    return {
      reservedTicketList: [],
      emptyListNotificationMessage: "",
    }
  },
  methods: {
    getReservedTicketList() {
      checkTicketApi
        .getReservedTicketList()
        .then((res) => {
          if (res.data.message === "예매 내역이 없습니다.") {
            this.emptyListNotificationMessage = res.data.message
          } else {
            this.reservedTicketList = res.data
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getReservedTicketList()
  },
}
</script>

<style></style>
