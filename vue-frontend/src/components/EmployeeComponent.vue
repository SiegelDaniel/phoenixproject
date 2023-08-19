<template>
  <div class="container">
    <h3>Employees:</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Id</th>
          <th scope="col">First </th>
          <th scope="col">Last </th>
          <th scope="col">Email</th>
          <th scope="col">Age</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <th scope="row">{{ employee.id }}</th>
          <td>{{ employee.firstname }}</td>
          <td>{{ employee.lastname }}</td>
          <td>{{ employee.email }}</td>
          <td>{{ employee.age }}</td>
        </tr>
      </tbody>
    </table>
    <p v-if="error" class="error-message">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'EmployeeComponent',
  data() {
    return {
      employees: null,
      error: null,
    };
  },
  created() {
    axios
      .get('http://localhost:8000/employees/')
      .then(res => {
        this.employees = res.data;
      })
      .catch(error => {
        this.error = 'Error fetching employees: ' + error.message;
      });
  },
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
