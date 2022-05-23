<template>
  <div class="bg-info bg-gradient bg-opacity-10">
    <header class="bg-danger bg-gradient bg-opacity-10">
      <nav class="navbar navbar-expand-lg navbar-light bg-primary bg-gradient bg-opacity-10">
        <div class="container-fluid bg-danger bg-gradient bg-opacity-10">
          <i class="fa fa-user-graduate"></i>
          <i class="fa fa-user-graduate"></i>
          <i class="fa fa-user-graduate"></i>
          <i class="fa fa-user-graduate"></i>
          <i class="fa fa-user-graduate"></i>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
              <!--
              <li class="nav-item">
                <a class="nav-link mx-3 fw-bold" aria-current="page" href="index.html">Home</a>
              </li>
              -->
              <li class="nav-item"><router-link to="/" class="nav-link mx-3 fw-bold">Home</router-link></li>
              <!--
              <li class="nav-item">
                <a class="nav-link mx-3 fw-bold" href="login.html">Login</a>
              </li>
              -->
              <li class="nav-item"><router-link to="/login" class="nav-link mx-3 fw-bold">Login</router-link></li>
              <!--
              <li class="nav-item">
                <a class="nav-link mx-3 fw-bold" href="about.html">About</a>
              </li>
              -->
              <li class="nav-item"><router-link to="/about" class="nav-link mx-3 fw-bold">About Us</router-link></li>
              
              <!--
              <router-link to="/about">About</router-link>
              <router-view></router-view>
              -->

              <li class="nav-item dropdown">
                <a class="nav-link mx-3 dropdown-toggle fw-bold" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Games
                 <!-- <i class="fa fa-arrow-down" id="arrow"></i> -->
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <!--<li><a class="dropdown-item fw-bold" href="games/math-facts.html">Math Facts</a></li>-->
                  <li class="nav-item"><router-link to="/games/math-facts" class="nav-link mx-3 fw-bold">Math Facts</router-link></li>
                  <!--<li><a class="dropdown-item fw-bold" href="games/anagram-hunt.html">Anagram Hunt</a></li>-->
                  <li class="nav-item"><router-link to="/games/anagram-hunt" class="nav-link mx-3 fw-bold">Anagram Hunt</router-link></li>
                  <!--<li class="nav-item"><router-link to="/games/main" class="nav-link mx-3 fw-bold">Main</router-link></li>-->
                </ul>
              </li>
              <!--
              <li class="nav-item">
                <a class="nav-link mx-3 fw-bold" href="contact-us.html">Contact</a>
              </li>
              -->
              <li class="nav-item"><router-link to="/contact" class="nav-link mx-3 fw-bold">Contact</router-link></li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  </div>
</template>

<script>
  export default {
    name: 'Header'
  }
</script>

<style>

</style>