<template>
  <div>
    <a @click="goTheaterListView">[뒤로 가기]</a>
    <theater-overall
      :theaterObject="{ theaterNo, theaterName, theaterLocation }"
    ></theater-overall>
    <div>
      <form v-if="isUpdateForm" @submit.prevent="updateTheater">
        <label for="name">수정할 이름 입력: </label>
        <input type="text" id="name" v-model="inputTheaterName" /><br />
        <label for="location">수정할 위치 입력: </label>
        <input type="text" id="location" v-model="inputTheaterLocation" /><br />
        <input type="submit" value="극장 정보 업데이트" />
      </form>
      <br />
    </div>

    <div>
      <button @click="toggleFormElement">수정하기</button>
      <span></span>
      <button @click="deleteTheater">삭제하기</button>
    </div>
    <hr />
    <div>
      <admin-screen-manage></admin-screen-manage>
    </div>
  </div>
</template>

<script>
import * as adminApi from "@/api/admin"
import AdminScreenManage from "@/components/AdminScreen/AdminScreenManage.vue"
import TheaterOverall from "@/components/Admin/TheaterOverall.vue"

export default {
  components: { AdminScreenManage, TheaterOverall },
  name: "AdminTheaterManageView",
  data() {
    return {
      theaterNo: null,
      theaterName: null,
      theaterLocation: null,
      inputTheaterName: null,
      inputTheaterLocation: null,
      isUpdateForm: false,
    }
  },
  computed: {
    theaterId() {
      return this.$route.params.theaterId
    },
  },
  watch: {
    isUpdateForm() {
      if (this.isUpdateForm === false) {
        this.theaterName = this.inputTheaterName
        this.theaterLocation = this.inputTheaterLocation
      }
    },
  },
  methods: {
    goTheaterListView() {
      this.$router.push({ name: "adminTheater" })
    },
    updateTheater() {
      adminApi
        .updateTheaterItem(
          this.theaterId,
          this.inputTheaterName,
          this.inputTheaterLocation
        )
        .then((res) => {
          console.log(res)
          this.toggleFormElement()
          this.$router
            .push({
              name: "manageTheater",
              params: { id: this.theaterId },
            })
            .catch(() => {})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    toggleFormElement() {
      this.isUpdateForm = !this.isUpdateForm
    },
    readTheaterItem() {
      adminApi
        .readTheaterItem(this.theaterId)
        .then((res) => {
          this.theaterNo = res.data.id
          this.theaterName = res.data.name
          this.theaterLocation = res.data.location
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteTheater() {
      adminApi
        .deleteTheaterItem(this.theaterNo)
        .then((res) => {
          console.log(res)
          this.$router.push({ name: "adminTheater" })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.readTheaterItem()
  },
}
</script>

<style></style>
