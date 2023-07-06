<template>
  <div class="partidos-view">
    <div class="create-partidos">
      <CreatePartido @new-partido="createPartidoEvent" />
    </div>

    <div class="partidos-section">
      <h2>Partidos</h2>
      <div class="list-partidos">
        <ListPartidos :partidos="allPartidos" />
      </div>
    </div>
  </div>
</template>

<script>
import CreatePartido from "@/components/CreatePartido.vue";
import ListPartidos from "@/components/ListPartidos.vue";

import { createPartido, getAllPartidos } from "@/services/partidos.api";
export default {
  name: "PartidosView",
  components: {
    CreatePartido,
    ListPartidos,
  },
  mounted() {
    this.loadAllPartidos();
  },
  data() {
    return {
      selectedOption: null,
      allPartidos: [],
    };
  },
  methods: {
    async loadAllPartidos() {
      const { partidos } = await getAllPartidos();
      console.log("partidos: ", partidos);
      this.allPartidos = partidos;
      console.log("this.allPartidos: ", this.allPartidos);
    },
    async createPartidoEvent(partido) {
      const { partido: { id, name } = {}, success } = await createPartido(
        partido
      );
      if (success) {
        this.allPartidos.push({ id, name });
      }
    },
  },
};
</script>

<style>
.partidos-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f5f5f5;
  padding: 20px;
}

.create-partidos {
  margin-bottom: 20px;
}

.partidos-section {
  background-color: #fff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

.partidos-heading {
  text-align: center;
  font-size: 28px;
  color: #333;
  margin-bottom: 20px;
}

.list-partidos {
  margin-top: 10px;
}

/* Additional Styles for ListPartidos Component */
.list-partidos ul {
  list-style-type: none;
  padding: 0;
}

.list-partidos li {
  background-color: #fafafa;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 10px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
}

.list-partidos li:hover {
  background-color: #f0f0f0;
}
</style>
