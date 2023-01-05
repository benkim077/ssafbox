<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  components: {},
  name: "TicketView",
  methods: {
    reset_ticketing_data() {
      this.$store.commit("ticket/RESET_SELECTED_DATA")
    },
  },
  created() {
    console.log("TicketView created")
    this.reset_ticketing_data()
    this.$router.push({ name: "schedules" }).catch(() => {})
  },
  updated() {
    console.log("TicketView updated")
    if (this.$route.name === "seat" || this.$route.name === "payment") {
      // console.log(1)
    } else {
      this.reset_ticketing_data()
      this.$router.push({ name: "schedules" }).catch(() => {})
    }
    console.log("route 객체", this.$route)
  },
}
</script>

<style></style>
