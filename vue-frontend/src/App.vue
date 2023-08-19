/* eslint-disable */
<template>
  <div id="app">
    <div class="nav-bar">
      <button @click="activeTab = 'employees'">Employees</button>
      <button @click="activeTab = 'projects'">Projects</button>
      <button @click="activeTab = 'departments'">Departments</button>
    </div>
    <div class="content">
      <EmployeeComponent v-show="activeTab === 'employees'" />
      <ProjectsComponent v-show="activeTab === 'projects'" />
      <DepartmentsComponent v-show="activeTab === 'departments'" />
    </div>
  </div>
</template>



<script>
import EmployeeComponent from "@/components/EmployeeComponent.vue";
import ProjectsComponent from "@/components/ProjectsComponent.vue";
import DepartmentsComponent from "@/components/DepartmentsComponent.vue";

export default {
  name: "app",
  components: {
    EmployeeComponent,
    ProjectsComponent,
    DepartmentsComponent,
  },
  data() {
    return {
      activeTab: "employees", // Default active tab
    };
  },
};
</script>



<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.nav-bar {
  position: sticky;
  top: 0;
  background-color: #f1f1f1;
  padding: 10px;
}

button {
  background-color: transparent;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

button.active {
  background-color: #3498db;
  color: white;
}

.content {
  margin-top: 20px;
}
</style>
