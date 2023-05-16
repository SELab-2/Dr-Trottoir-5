<template>
  <AccountInformation :can_edit_permission="false" :not_admin="true"></AccountInformation>
</template>

<script>
import AccountInformation from "@/components/AccountInformation";

export default {
  name: "AdminStudentInfoUser",
  components: {AccountInformation}
}
</script>

<style scoped>

</style>
