<template>
  <div>
    <h3>상영관 생성</h3>
    <admin-screen-create></admin-screen-create>
    <hr />
    <h3>상영관 관리</h3>
    <admin-screen-list></admin-screen-list>
  </div>
</template>

<script>
import AdminScreenCreate from "./AdminScreenCreate.vue"
import AdminScreenList from "./AdminScreenList.vue"

export default {
  components: { AdminScreenCreate, AdminScreenList },
  name: "AdminScreenManage",
}
</script>

<style></style>
