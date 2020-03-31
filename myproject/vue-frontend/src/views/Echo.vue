<template>
  <div>
    <h1>Test API Connection</h1>
    <EchoBox />
  </div>
</template>
<script>
// @ is an alias to /src
import EchoBox from "@/components/EchoBox.vue";

export default {
  name: "Ping",
  components: {
    EchoBox
  }
};
</script>
