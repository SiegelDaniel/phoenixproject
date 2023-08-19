/* eslint-disable */
<template>
  <div id="app">
    <EmployeeComponent />
  </div>
</template>

<script>
import EmployeeComponent from "@/components/EmployeeComponent.vue";

export default {
  name: 'app',
  components: {
    EmployeeComponent
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>