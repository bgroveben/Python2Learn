<template>
  <button class="btn btn-primary"
    @click="increment"
    @mouseout="count=0">{{count}}</button>
</template>

<script>
export default {
  name: "Counter",  
  data: function() {
    return {
      count: 0
    }
  },
  methods: {
    increment: function() {
      this.count++;
    }
  }
}
</script>
<style scoped>
  button {
    text-decoration: none;
    margin: 0 1em;
    width: 200px;
  }

  button[disabled] {
    background-color: lightgray;
    border-color: gray;
    color: black;
    cursor: not-allowed;
    font-variant: small-caps;
  }
</style>