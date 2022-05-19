<template>
  <strong>Score: {{score}}</strong>
</template>

<script>
  // import Anagrams from './Anagrams';

  export default {
    name: 'Score',
    props: {
      score: Number
    }
  }
</script>