<template>
  <div class="container">
    <h3>Departments:</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Id</th>
          <th scope="col">Name</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="department in departments" :key="department.id">
          <th scope="row">{{ department.id }}</th>
          <td>{{ department.name }}</td>
          <td>
            <button @click="deleteDepartment(department.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-if="error" class="error-message">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DepartmentsComponent',
  data() {
    return {
      departments: null,
      error: null,
    };
  },
  created() {
    this.fetchDepartments();
  },
  methods: {
    fetchDepartments() {
      axios
        .get('http://localhost:8000/departments/')
        .then(res => {
          this.departments = res.data;
        })
        .catch(error => {
          this.error = 'Error fetching departments: ' + error.message;
        });
    },
    async deleteDepartment(departmentId) {
      try {
        await axios.delete(`http://localhost:8000/departments/${departmentId}`);
        // After deleting, refresh the departments list
        this.fetchDepartments();
      } catch (error) {
        console.error('Error deleting department:', error);
      }
    }
  }
};
</script>

<style>
h3 {
  margin-bottom: 5%;
}
.error-message {
  color: red;
  font-weight: bold;
}
</style>
