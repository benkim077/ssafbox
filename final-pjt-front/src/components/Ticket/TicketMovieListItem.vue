<template>
  <div>
    <li>
      <div @click="setSelectedMovie">
        {{ movieItem.title }}
      </div>
    </li>
  </div>
</template>

<script>
export default {
  name: "TicketMovieListItem",
  props: {
    movieItem: Object,
  },
  methods: {
    setSelectedMovie() {
      this.$store.commit("ticket/SET_SELECTED_MOVIE", this.movieItem.id)
    },
  },
}
</script>

<style></style>
