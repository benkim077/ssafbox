<template>
  <div>
    <li>
      <div @click="setSelectedDate">
        {{ dateItem }}
      </div>
    </li>
  </div>
</template>

<script>
export default {
  name: "TicketDateListItem",
  props: {
    dateItem: String,
  },
  methods: {
    setSelectedDate() {
      this.$store.commit("ticket/SET_SELECTED_DATE", this.dateItem) // 제대로 된 정보를 주고 있는가?
    },
  },
}
</script>

<style></style>
