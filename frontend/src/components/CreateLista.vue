<template>
  <div class="lista-creation-form">
    <h1>Create Lista</h1>
    <form @submit.prevent.stop="createLista">
      <div class="form-group">
        <label>Nombre:</label>
        <input type="text" v-model.lazy.trim="lista.name" />
      </div>

      <button class="submit-button" type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "CreateLista",
  components: {},
  data() {
    return {
      lista: {
        name: "",
      },
    };
  },
  methods: {
    createLista() {
      this.$emit("new-lista", this.lista);
    },
  },
};
</script>
<style>
.lista-creation-form {
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
