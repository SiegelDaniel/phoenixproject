<template>
  <div>
    <button @click="openFileDialog">Select File</button>
    <input type="file" ref="fileInput" style="display: none" @change="handleFileChange" />
    <!-- Rest of your component content -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    openFileDialog() {
      this.$refs.fileInput.click();
    },
    async handleFileChange(event) {
      const selectedFile = event.target.files[0];
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await axios.post('http://localhost:8000/upload/', formData);
        console.log('File uploaded:', response.data);
      } catch (error) {
        console.error('Error uploading file:', error);
      }
    }
  }
}
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
