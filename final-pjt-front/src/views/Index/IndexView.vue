<template>
  <div>
    <h2>Main Page</h2>
    <recommended-movie></recommended-movie>
    <br />
  </div>
</template>

<script>
import RecommendedMovie from "@/components/Index/RecommendedMovie.vue"
export default {
  components: { RecommendedMovie },
  name: "IndexView",
}
</script>

<style></style>
