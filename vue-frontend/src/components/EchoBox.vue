<template>
  <div>
    <p>{{ apiResponse }}</p>
    <input type="text" v-model="message" />
    <button v-on:click="doEcho">
      <b>{{ buttonText }}</b>
    </button>
  </div>
</template>

<script>
import client from "@/services/ApiClient.js";

export default {
  name: "EchoBox",
  data: () => ({
    apiResponse: "Click the button to ping the API.",
    message: ""
  }),
  computed: {
    buttonText: function() {
      return !this.message ? "GET" : "POST";
    }
  },
  methods: {
    doEcho: async function() {
      const payload = { text: this.message };
      const endpoint = "/api/echo";
      const request = !this.message
        ? client.get(endpoint)
        : client.post(endpoint, payload);
      const res = await request;
      this.apiResponse = res.data;
      this.message = "";
    }
  }
};
</script>

<style scoped>
button,
input {
  padding: 0.5rem 3rem;
  background-color: #ffffff;
  text-transform: capitalize;
  font-size: 1rem;
  border-radius: 1rem;
  margin: 0 0.5rem;
}
p {
  text-transform: capitalize;
}
</style>
