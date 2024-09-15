<template>
  <div>
    <nav>
      <ul>
        <li>
          <NuxtLink to="/race">Race</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/history">History</NuxtLink>
        </li>
      </ul>
    </nav>
    <NuxtPage />
  </div>
</template>

<script lang="ts">
export default {
  name: 'App'
}
</script>

<style scoped>
nav {
  background-color: #f8f8f8;
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

ul {
  display: flex;
  list-style: none;
  gap: 20px;
  margin: 0;
  padding: 0;
}

li {
  font-size: 16px;
}

a {
  text-decoration: none;
  color: #007bff;
}

a:hover {
  text-decoration: underline;
}
</style>