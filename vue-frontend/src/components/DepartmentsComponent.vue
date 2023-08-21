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
            <button @click="showPopup(department)">View Details</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-if="error" class="error-message">{{ error }}</p>

    <div class="popup" v-if="selectedDepartment">
      <div class="popup-content">
        <h2>Department Details</h2>
        <p><strong>Id:</strong> {{ selectedDepartment.id }}</p>
        <input v-model="editedDepartmentName" />
        <button @click="saveEditedDepartment">Save</button>
        <button @click="closePopup">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DepartmentsComponent',
  data() {
    return {
      departments: null,
      selectedDepartment: null,
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
        this.fetchDepartments();
      } catch (error) {
        console.error('Error deleting department:', error);
      }
    },
    showPopup(department) {
      this.selectedDepartment = department;
      this.editedDepartmentName = department.name;
    },
     closePopup() {
      this.selectedDepartment = null;
    },

    async saveEditedDepartment() {
      try {
        await axios.put(`http://localhost:8000/departments/${this.selectedDepartment.id}`, {
          name: this.editedDepartmentName,
        });

        const editedIndex = this.departments.findIndex(department => department.id === this.selectedDepartment.id);
        if (editedIndex !== -1) {
          this.departments[editedIndex].name = this.editedDepartmentName;
        }

        this.closePopup();
      } catch (error) {
        console.error('Error updating department:', error);
      }
    },
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
