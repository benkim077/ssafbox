<template>
  <div>
    <li>
      <div @click="setSelectedSchedule">
        <p>{{ hours }}시 {{ minutes }}분</p>
      </div>
    </li>
  </div>
</template>

<script>
export default {
  name: "TicketScheduleListItem",
  props: {
    scheduleItem: Object,
  },
  computed: {
    selectedMovie() {
      return this.$store.state.ticket.selectedMovie
    },

    // "2022-11-22" "22:40:00"
    hours() {
      return this.scheduleItem.start_time.slice(0, 2)
    },
    minutes() {
      return this.scheduleItem.start_time.slice(3, 5)
    },
    seconds() {
      return this.scheduleItem.start_time.slice(6, 8)
    },
  },
  methods: {
    setSelectedSchedule() {
      this.$store.commit("ticket/SET_SELECTED_SCHEDULE", this.scheduleItem)
    },
  },
}
</script>

<style></style>
