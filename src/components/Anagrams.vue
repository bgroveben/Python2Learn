<template>
  <div id="body">
    <div>
        <div class="row input-group">
            <h4>Anagrams left: {{anagramsLeft}}</h4>
          <div class="row mt-3">
            <h4>Anagrams guessed: {{anagramsGuessed}}</h4>
          </div>
        </div>
    </div>   
  </div>
</template>

<script>

export default {
    name: 'Anagrams',
    props: {
        anagramsGuessed: Array, // Correct answers by user
        anagramsLeft: Number // Number of words left in anagram's array
    }
  }
</script>