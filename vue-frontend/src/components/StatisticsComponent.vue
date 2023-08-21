<template>
  <div class="container">
    <h3>Department Statistics:</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Department ID</th>
          <th scope="col">Department Name</th>
          <th scope="col">Average Age</th>
          <th scope="col">Number of Employees</th>
          <th scope="col">Number of Projects</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="statistic in statistics" :key="statistic.department_id">
          <td>{{ statistic.department_id }}</td>
          <td>{{ statistic.department_name }}</td>
          <td>{{ statistic.average_age }}</td>
          <td>{{ statistic.employees.length }}</td>
          <td>{{ statistic.number_of_projects }}</td>
          <td>
            <button @click="showEmployeesPopup(statistic.employees)">View Employees</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-if="error" class="error-message">{{ error }}</p>

    <div class="popup" v-if="selectedEmployees">
      <div class="popup-content">
        <h2>Employees List</h2>
        <ul>
          <li v-for="employee in selectedEmployees" :key="employee.id">
            {{ employee.firstname }} {{ employee.lastname }} ({{ employee.age }} years old)
          </li>
        </ul>
        <button @click="closeEmployeesPopup">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'StatisticsComponent',
  data() {
    return {
      statistics: [],
      selectedEmployees: null,
      error: null,
    };
  },
  mounted() {
    this.fetchDepartmentStatistics();
  },
  methods: {
    fetchDepartmentStatistics() {
      axios
        .get('http://localhost:8000/statistics/departments')
        .then(res => {
          this.statistics = res.data;
        })
        .catch(error => {
          this.error = 'Error fetching department statistics: ' + error.message;
        });
    },
    showEmployeesPopup(employees) {
      this.selectedEmployees = employees;
    },
    closeEmployeesPopup() {
      this.selectedEmployees = null;
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

/* Popup Styles */
.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.popup-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  text-align: center;
}

.popup button {
  margin-top: 10px;
}
</style>
