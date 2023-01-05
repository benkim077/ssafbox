<template>
  <div>
    <payment-overall></payment-overall>
    <hr />
    <payment-method-list></payment-method-list>
    <hr />
    <button @click="payBySelectedPaymentMethod">결제하기</button>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
import PaymentOverall from "@/components/Ticket/Payment/PaymentOverall.vue"
import PaymentMethodList from "@/components/Ticket/Payment/PaymentMethodList.vue"
export default {
  components: { PaymentOverall, PaymentMethodList },
  name: "PaymentView",
  computed: {
    selectedPaymentMethod() {
      return this.$store.state.ticket.selectedPaymentMethod
    },
    selectedSeatId() {
      return this.$store.state.ticket.selectedSeatId
    },
  },
  methods: {
    payBySelectedPaymentMethod() {
      if (this.selectedPaymentMethod === "카카오페이") {
        ticketApi
          .kakaopayReady(this.selectedSeatId)
          .then((res) => {
            location.href = res.data.next_redirect_pc_url
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
  },
}
</script>

<style></style>
