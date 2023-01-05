<template>
  <div>
    <li>
      <div @click="setSelectedTheater">
        {{ theaterItem.name }}
      </div>
    </li>
  </div>
</template>

<script>
export default {
  name: "TicketTheaterListItem",
  props: {
    theaterItem: Object,
  },
  methods: {
    setSelectedTheater() {
      //
      this.$store.commit("ticket/SET_SELECTED_THEATER", this.theaterItem.id)
    },
  },
}
</script>

<style></style>
