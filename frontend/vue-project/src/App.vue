<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'


//     function loadMessage() {
//         fetch('http://localhost:5000/')
//             .then(response => response.json())
//             .then(data => {
//                 console.log(data)
//                 document.getElementById('message').innerText = data.message;
//             })
//             .catch(error => {
//                 document.getElementById('message').innerText = 'Error fetching message';
//                 console.log(error)
//                 console.error('Error fetching message:', error);
//             });
//     }

</script>

<template>
  <!-- <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="Student did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <h1>MAD2 Project Frontend!</h1>

  <p id="message">Click below button to load message</p>

  <button @click="loadMessage()">Get message from backend</button> -->

  <!-- <RouterView /> -->
  <RouterView />
</template>

<style scoped></style>