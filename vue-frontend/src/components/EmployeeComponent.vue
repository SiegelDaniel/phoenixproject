<template>
  <div class="container">
    <h3>Employees:</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Id</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Email</th>
          <th scope="col">Age</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <th scope="row">{{ employee.id }}</th>
          <td>{{ employee.firstname }}</td>
          <td>{{ employee.lastname }}</td>
          <td>{{ employee.email }}</td>
          <td>{{ employee.age }}</td>
          <td>
            <button @click="openEditPopup(employee)">Edit</button>
            <button @click="deleteEmployee(employee.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-if="error" class="error-message">{{ error }}</p>

    <!-- Edit Popup -->
    <div v-if="editingEmployee" class="popup">
      <div class="popup-content">
        <h3>Edit Employee</h3>
        <input v-model="editingEmployee.firstname" />
        <input v-model="editingEmployee.lastname" />
        <input v-model="editingEmployee.email" />
        <input v-model="editingEmployee.age" />
        <button @click="saveEditedEmployee">Save</button>
        <button @click="closeEditPopup">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'EmployeeComponent',
  data() {
    return {
      employees: null,
      editingEmployee: null,
      error: null,
    };
  },
  created() {
    this.fetchEmployees();
  },
  methods: {
    fetchEmployees() {
      axios
        .get('http://localhost:8000/employees/')
        .then(res => {
          this.employees = res.data;
          this.sortEmployeesById();
        })
        .catch(error => {
          this.error = 'Error fetching employees: ' + error.message;
        });
    },
    async deleteEmployee(employeeId) {
      try {
        await axios.delete(`http://localhost:8000/employees/${employeeId}`);
        this.fetchEmployees();
      } catch (error) {
        console.error('Error deleting employee:', error);
      }
    },
    openEditPopup(employee) {
      this.editingEmployee = { ...employee };
    },
    closeEditPopup() {
      this.editingEmployee = null;
    },
    async saveEditedEmployee() {
      try {
        await axios.put(`http://localhost:8000/employees/${this.editingEmployee.id}`, this.editingEmployee);
        this.fetchEmployees();
      } catch (error) {
        console.error('Error updating employee:', error);
      }
    },
    sortEmployeesById() {
      this.employees.sort((a, b) => a.id - b.id);
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
}
</style>
