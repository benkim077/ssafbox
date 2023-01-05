<template>
  <div>
    <movie-review-item
      v-for="movieReviewItem in movieReviewList"
      :key="movieReviewItem.id"
      :movieReviewItem="movieReviewItem"
    ></movie-review-item>
  </div>
</template>

<script>
import * as communityApi from "@/api/community"
import MovieReviewItem from "./MovieReviewItem.vue"
export default {
  components: { MovieReviewItem },
  name: "MovieReviewList",
  data() {
    return {
      movieReviewList: [],
      movieId: null,
    }
  },
  methods: {
    getMovieId() {
      this.movieId = this.$store.state.recommendation.movieId
    },
    getReviewList() {
      communityApi
        .getReviewList(this.movieId)
        .then((res) => {
          this.movieReviewList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getMovieId()
    this.getReviewList()
  },
}
</script>

<style></style>
