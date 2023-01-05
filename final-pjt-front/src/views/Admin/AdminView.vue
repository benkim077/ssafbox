<template>
  <div>
    <nav>
      <span>
        <router-link :to="{ name: 'adminTheater' }">극장 관리</router-link>
      </span>
    </nav>
    <hr />
    <router-view />
  </div>
</template>

<script>
export default {
  name: "AdminView",
  methods: {},
}
</script>

<style></style>
