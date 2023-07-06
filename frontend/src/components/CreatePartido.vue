<template>
  <div class="partido-creation-form">
    <h1>Create Partido</h1>
    <form @submit.prevent.stop="createPartido">
      <div class="form-group">
        <label>Equipo Local:</label>
        <input type="text" v-model.lazy.trim="partido.local" />
      </div>

      <div class="form-group">
        <label>Equipo Visitante:</label>
        <input type="text" v-model.lazy.trim="partido.visitante" />
      </div>

      <div class="form-group">
        <label>Estadio:</label>
        <input type="text" v-model.lazy.trim="partido.estadio" />
      </div>

      <div class="form-group">
        <label>Lista:</label>
        <input type="text" v-model.lazy.trim="partido.lista" />
      </div>

      <button class="submit-button" type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "CreatePartido",
  components: {},
  data() {
    return {
      partido: {
        local: "",
        visitante: "",
        estadio: "",
        lista: "",
      },
    };
  },
  methods: {
    createPartido() {
      this.$emit("new-partido", this.partido);
    },
  },
};
</script>
<style>
.partido-creation-form {
  padding: 0;
  margin: 0;
  width: 300px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 300px;
}

.submit-button {
  margin-top: 10px;
  background-color: #4caf50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
