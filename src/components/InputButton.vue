<template>
  <div class="row mx-1 mb-3 mt-5">
    <button class="form-control btn btn-primary" @click="$emit('is-anagram')">
      Enter
    </button>
  </div>
</template>

<script>
  export default {
    name: 'InputButton'
  }
</script>