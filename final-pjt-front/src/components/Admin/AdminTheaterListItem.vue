<template>
  <div>
    <li class="margin_y__li">
      <div>
        <span>{{ theater.name }}점</span>
        <span>
          <button @click="goManagementPage(theater.id)">관리</button>
        </span>
      </div>
    </li>
  </div>
</template>

<script>
export default {
  name: "AdminTheaterListItem",
  props: {
    theater: Object,
  },
  methods: {
    storeTheaterId() {
      this.$store.commit("admin/STORE_THEATER_ID", this.theater.id)
    },
    goManagementPage(theaterId) {
      this.storeTheaterId()
      this.$router
        .push({ name: "manageTheater", params: { theaterId } })
        .catch(() => {})
    },
  },
}
</script>

<style>
.margin_y__li {
  margin-bottom: 1rem;
}
</style>
