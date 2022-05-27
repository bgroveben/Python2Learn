<template>
  <div id="equation" class="row">
    <div class="col-6 text-end display-2 mr-5">{{question}}</div>
    <div class="col-1 display-2">=</div>
    <div class="col-5 text-start display-2">{{answer}}</div>
  </div>
</template>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

<script>
  export default {
    name: 'Equation',
    props: {
      question: String,
      answer: String,
      answered: Boolean
    }
  }
</script>

<style scoped>
/*
  #equation {
    font-size: 1.6em;
    margin: auto;
    width: 90%;
  }
  */
</style>