<template>
  <div class="row mx-1 mb-3 mt-5">
    <button class="form-control btn btn-primary" @click="$emit('is-anagram')">
      Enter
    </button>
  </div>
</template>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script>
  export default {
    name: 'InputButton'
  }
</script>