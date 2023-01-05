<template>
  <div>
    <li class="margin_y__li">
      <span>{{ screenItem.id }} 번 상영관</span>
      <button @click="goScreenManagePage">관리</button>
    </li>
  </div>
</template>

<script>
export default {
  name: "AdminScreenListItem",
  props: {
    screenItem: Object,
  },
  methods: {
    goScreenManagePage() {
      this.$router.push({
        name: "manageScreen",
        params: { screenId: this.screenItem.id },
      })
    },
  },
}
</script>

<style>
.margin_y__li {
  margin-bottom: 1rem;
}
</style>
