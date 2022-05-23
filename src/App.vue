<template>
  <div id="app">
    <Header />
    <!--
    <About />
    -->
    <router-view></router-view>
    <!--
    <Main />
    -->
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header';
// import Main from './components/Main';
import Footer from './components/Footer';
// import About from './components/About';
export default {
  name: 'app',
  components: {
    Header,
    // Main,
    Footer,
    // About
}
}
</script>

<style>
header, footer {
  background-color: #3f7cad;
}
</style>
