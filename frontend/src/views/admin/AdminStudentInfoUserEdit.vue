<template>
    <AccountInformation :not_admin="false"></AccountInformation>
</template>

<script>
import AccountInformation from "@/components/AccountInformation";

export default {
  name: "AdminStudentInfoUserEdit",
  components: {AccountInformation}
}
</script>
