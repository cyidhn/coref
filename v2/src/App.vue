<template>
  <div>
    <Navbar />
    <br/><br/><br/><br/>
    <br/><br/><br/><br/>
    <br/><br/><br/><br/>
    <Footer />
  </div>
</template>

<script>
  // import { Menu, MenuButton, MenuItems, MenuItem } from "@headlessui/vue";
  // import AlgorithmsList from "./components/AlgorithmsList.vue";
  import Navbar from "./components/Navbar.vue";
  import Footer from "./components/Footer.vue";

  export default {
    components: {
      Navbar,
      Footer,
    },
  };
</script>
