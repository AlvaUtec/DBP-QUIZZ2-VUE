import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000/partidos";

export const createPartido = async (payload) => {
  const { data } = await axios.post(BASE_URL, payload);

  return data;
};

export const getAllPartidos = async () => {
  const { data } = await axios.get(BASE_URL);

  return data;
};
