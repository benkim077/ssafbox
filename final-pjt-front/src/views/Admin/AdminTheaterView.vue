<template>
  <div>
    <admin-theater-create></admin-theater-create>
    <admin-theater-list></admin-theater-list>
  </div>
</template>

<script>
import AdminTheaterCreate from "@/components/Admin/AdminTheaterCreate.vue"
import AdminTheaterList from "@/components/Admin/AdminTheaterList.vue"

export default {
  components: { AdminTheaterCreate, AdminTheaterList },
  name: "AdminTheaterView",
}
</script>

<style></style>
