<template>
  <div>
    <h3>극장 정보</h3>
    <p>
      번호 : {{ theaterObject.theaterNo }} / 이름 :
      {{ theaterObject.theaterName }} / 위치 :
      {{ theaterObject.theaterLocation }}
    </p>
  </div>
</template>

<script>
export default {
  name: "TheaterOverall",
  props: {
    theaterObject: Object,
  },
}
</script>

<style></style>
