<template>
  <div class="listas-view">
    <div class="create-listas">
      <CreateLista @new-lista="createListaEvent" />
    </div>

    <div class="listas-section">
      <h2 class="listas-heading">Listas</h2>
      <div class="listas-list">
        <ListListas :listas="allListas" />
      </div>
    </div>
  </div>
</template>

<script>
import CreateLista from "@/components/CreateLista.vue";
import ListListas from "@/components/ListListas.vue";

import { createLista, getAllListas } from "@/services/listas.api";
export default {
  name: "ListasView",
  components: {
    CreateLista,
    ListListas,
  },
  mounted() {
    this.loadAllListas();
  },
  data() {
    return {
      selectedOption: null,
      allListas: [],
    };
  },
  methods: {
    async loadAllListas() {
      const { listas } = await getAllListas();
      console.log("listas: ", listas);
      this.allListas = listas;
      console.log("this.allListas: ", this.allListas);
    },
    async createListaEvent(lista) {
      const { lista: { id, name } = {}, success } = await createLista(lista);
      if (success) {
        this.allListas.push({ id, name });
      }
    },
  },
};
</script>

<style>
.listas-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f5faff;
  padding: 20px;
}

.create-listas {
  margin-bottom: 20px;
}

.listas-section {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.listas-heading {
  text-align: center;
  font-size: 28px;
  color: #333333;
  margin-bottom: 20px;
}

.listas-list {
  margin-top: 10px;
}

/* Additional Styles for ListListas Component */
.listas-list ul {
  list-style-type: none;
  padding: 0;
}

.listas-list li {
  background-color: #e4f0ff;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 10px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
}

.listas-list li:hover {
  background-color: #d0e7ff;
}
</style>
