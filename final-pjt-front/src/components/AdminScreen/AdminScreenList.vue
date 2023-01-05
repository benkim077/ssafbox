<template>
  <div>
    <ul>
      <admin-screen-list-item
        v-for="screenItem in screenList"
        :key="screenItem.id"
        :screenItem="screenItem"
      ></admin-screen-list-item>
    </ul>
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
import AdminScreenListItem from "./AdminScreenListItem.vue"

export default {
  components: { AdminScreenListItem },
  name: "AdminScreenList",
  data() {
    return {
      screenList: [],
    }
  },
  computed: {
    theaterId() {
      return this.$store.state.admin.theaterId
    },
    computedScreenList() {
      return this.$store.getters["admin/getScreenList"]
    },
  },
  watch: {
    computedScreenList(value) {
      this.screenList = value
    },
  },
  methods: {
    getScreenList() {
      adminApi
        .getScreenList(this.theaterId)
        .then((res) => {
          this.$store.state.admin.screenList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getScreenList()
  },
}
</script>

<style></style>
