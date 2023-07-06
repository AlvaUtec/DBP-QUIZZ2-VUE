<template>
  <div class="list-listas">
    <ul class="custom-list">
      <li v-for="lista in listas" :key="lista.id">
        {{ lista.nombre }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ListListas",
  props: {
    listas: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style>
.list-listas {
  padding: 0;
  margin: 0;
  width: 300px;
}

.custom-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.custom-list li {
  padding: 8px;
  border-bottom: 1px solid #ccc;
}
</style>
