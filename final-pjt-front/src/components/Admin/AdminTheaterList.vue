<template>
  <div>
    <h3>극장 목록</h3>
    <ul>
      <admin-theater-list-item
        v-for="theaterItem in theaterList"
        :key="theaterItem.id"
        :theater="theaterItem"
      ></admin-theater-list-item>
    </ul>
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
import AdminTheaterListItem from "@/components/Admin/AdminTheaterListItem"
export default {
  components: { AdminTheaterListItem },
  name: "AdminTheaterList",
  data() {
    return {
      theaterList: [],
    }
  },
  methods: {
    readTheaterList() {
      adminApi
        .readTheaterList()
        .then((res) => {
          this.theaterList = res.data
          this.$store.commit("admin/SET_THEATER_LIST", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  computed: {
    computedTheaterList() {
      return this.$store.getters["admin/getTheaterList"]
    },
  },
  watch: {
    computedTheaterList(value) {
      this.theaterList = value
    },
  },
  created() {
    this.readTheaterList()
  },
}
</script>

<style></style>
