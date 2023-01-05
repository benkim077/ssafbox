<template>
  <div>
    <h3>결제 수단 선택</h3>
    <div
      v-for="(paymentMethodItem, idx) in paymentMethodList"
      :key="`paymentMethodItem-${idx}`"
    >
      <label :for="paymentMethodItem">{{ paymentMethodItem }}</label>
      <input
        type="radio"
        v-model="selectedPaymentMethod"
        :value="paymentMethodItem"
        :id="paymentMethodItem"
      />
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  name: "PaymentMethodList",
  data() {
    return {
      selectedPaymentMethod: null,
      paymentMethodList: ["카카오페이", "애플페이"],
    }
  },
  watch: {
    selectedPaymentMethod() {
      this.$store.commit(
        "ticket/SET_SELECTED_PAYMENT_METHOD",
        this.selectedPaymentMethod
      )
    },
  },
}
</script>

<style></style>
