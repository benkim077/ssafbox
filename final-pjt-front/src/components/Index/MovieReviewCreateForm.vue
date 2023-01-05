<template>
  <div>
    <form @submit.prevent="createReview">
      <label for="review-text">리뷰작성 :</label>
      <textarea type="text" id="review-text" v-model="reviewText"></textarea>
      <input type="submit" value="등록" />
    </form>
  </div>
</template>

<script>
import * as communityApi from "@/api/community"
export default {
  name: "MovieReviewCreateForm",
  data() {
    return {
      reviewText: "",
    }
  },
  computed: {
    userId() {
      return this.$store.state.auth.userId
    },
    movieId() {
      return this.$store.state.recommendation.movieId
    },
  },
  methods: {
    createReview() {
      communityApi
        .createReview(this.movieId, this.reviewText)
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
