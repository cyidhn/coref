<template>
  <div>
    <Navbar />
    <Analytics />
    <Footer />
  </div>
</template>

<script>
  // import { Menu, MenuButton, MenuItems, MenuItem } from "@headlessui/vue";
  // import AlgorithmsList from "./components/AlgorithmsList.vue";
  import Navbar from "./components/Navbar.vue";
  import Footer from "./components/Footer.vue";
  import Analytics from "./components/Analytics.vue";

  export default {

    components: {
      Navbar,
      Footer,
      Analytics
    },
  };
</script>
