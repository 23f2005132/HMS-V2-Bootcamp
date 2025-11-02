<script setup>
function loadMessage() {
  fetch('http://localhost:5000/')
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      document.getElementById('message').innerText = data.message
    })
    .catch((error) => {
      document.getElementById('message').innerText = 'Error fetching message'
      console.log(error)
      console.error('Error fetching message:', error)
    })
}
</script>

<template>
  <h1>User Registration Page</h1>

  <p id="message">Click below button to load message</p>

  <button @click="loadMessage()">Get message from backend</button>
</template>