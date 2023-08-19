<template>
  <div class="container">
    <h3>Projects:</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Id</th>
          <th scope="col">Name</th>
          <th scope="col">Client</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="project in projects" :key="project.id">
          <th scope="row">{{ project.id }}</th>
          <td>{{ project.name }}</td>
          <td>{{ project.client }}</td>
          <td>
            <button @click="deleteProject(project.id)">Delete</button>
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
  name: 'ProjectsComponent',
  data() {
    return {
      projects: null,
      error: null,
    };
  },
  created() {
    this.fetchProjects();
  },
  methods: {
    fetchProjects() {
      axios
        .get('http://localhost:8000/projects/')
        .then(res => {
          this.projects = res.data;
        })
        .catch(error => {
          this.error = 'Error fetching projects: ' + error.message;
        });
    },
    async deleteProject(projectId) {
      try {
        await axios.delete(`http://localhost:8000/projects/${projectId}`);
        // After deleting, refresh the projects list
        this.fetchProjects();
      } catch (error) {
        console.error('Error deleting project:', error);
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
