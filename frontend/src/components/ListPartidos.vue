<template>
  <div class="list-partidos">
    <table class="custom-table">
      <thead>
        <tr>
          <th>Equipo Local</th>
          <th>Equipo Visitante</th>
          <th>Estadio</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="partido in partidos" :key="partido.id">
          <td>{{ partido.equipo_local }}</td>
          <td>{{ partido.equipo_visitante }}</td>
          <td>{{ partido.estadio }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "ListPartidos",
  props: {
    partidos: {
      type: [],
      required: true,
    },
  },
};
</script>

<style>
.list-partidos {
  padding: 0px;
  margin: 0px;
  width: 300px;
}
.custom-table {
  width: 100%;
  border-collapse: collapse;
}

.custom-table th,
.custom-table td {
  padding: 8px;
  text-align: left;
}

.custom-table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.custom-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.custom-table tr:hover {
  background-color: #e6e6e6;
}

.custom-table td {
  border-bottom: 1px solid #ccc;
}
</style>
