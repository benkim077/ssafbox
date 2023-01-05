<template>
  <div>
    <movie-review-list></movie-review-list>
    <br />
    <movie-review-create></movie-review-create>
  </div>
</template>

<script>
import MovieReviewCreate from "./MovieReviewCreate.vue"
import MovieReviewList from "./MovieReviewList.vue"
export default {
  components: { MovieReviewList, MovieReviewCreate },
  name: "MovieReview",
}
</script>

<style></style>
