<template>
  <div>
    <h2>예매가 완료되었습니다!</h2>
    <div>
      <button @click="goCheckTicketPage">예매 내역 보기</button>
    </div>
  </div>
</template>

<script>
import * as ticketApi from "@/api/ticket"
export default {
  name: "PaymentCompleteView",
  data() {
    return {
      uuid: null,
      pg_token: null,
      paymentCompleteData: null,
    }
  },
  methods: {
    getCompletePaymentData() {
      this.uuid = this.$route.params.uuid
      this.pg_token = this.$route.query.pg_token
    },
    goCheckTicketPage() {
      this.$router.push({ name: "check" })
    },
  },
  created() {
    this.getCompletePaymentData()
    ticketApi
      .kakaopayCheckSuccess(this.uuid, this.pg_token)
      .then((res) => {
        this.paymentCompleteData = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style></style>
