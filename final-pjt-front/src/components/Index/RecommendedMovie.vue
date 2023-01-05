<template>
  <div>
    <div>
      <h3>추천 영화</h3>
      <div>
        <img
          class="postal_size__div"
          :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${recommendedMovie.poster}`"
          alt="추천 영화 이미지"
        />
      </div>
      <div>
        <p>{{ recommendedMovie.title }}</p>
      </div>
    </div>
    <movie-review v-if="temp"></movie-review>
  </div>
</template>

<script>
import * as recommentdationApi from "@/api/recommendation"
import MovieReview from "./MovieReview.vue"
export default {
  components: { MovieReview },
  name: "RecommendedMovie",
  data() {
    return {
      temp: false,
      recommendedMovie: {
        poster: "",
        title: "",
      },
    }
  },
  methods: {
    async getRecommendedMovie() {
      return recommentdationApi
        .getRecommendedMovie()
        .then((res) => {
          this.recommendedMovie.poster = res.data.poster
          this.recommendedMovie.title = res.data.title
          this.$store.commit(
            "recommendation/SET_RECOMMENDED_MOVIE",
            res.data.id
          )
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  async created() {
    console.log("RecommendedMovie created")
    await this.getRecommendedMovie()
    this.temp = true
  },
}
</script>

<style>
.postal_size__div {
  width: 300px;
}
</style>
