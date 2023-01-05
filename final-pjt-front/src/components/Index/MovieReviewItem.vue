<template>
  <div>
    <span
      >내용: {{ movieReviewItem.content }} / 작성자:
      {{ movieReviewItem.username }}</span
    >
    <span v-if="movieReviewItem.user === userId"
      ><button @click="deleteReview">X</button></span
    >
  </div>
</template>

<script>
import * as communityApi from "@/api/community"
export default {
  name: "MovieReviewItem",
  computed: {
    userId() {
      return this.$store.state.auth.userId
    },
    reviewId() {
      return this.movieReviewItem.id
    },
  },
  props: {
    movieReviewItem: Object,
  },
  methods: {
    deleteReview() {
      communityApi
        .deleteReview(this.reviewId)
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          if (err.response.status === 403) {
            alert("삭제 권한이 없습니다.(403 Forbidden)")
          }
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
