<template>
  <div id="body">
    <div class="mt-3">
      <h3>Anagram:</h3>
    </div>
    <div>
      <!-- Nested v-for div tags to loop through arrays and sub-arrays? -->
      <!-- <h3 class="fw-bold text-primary" id="anagram">{{randomWord}}</h3> -->
      <h3 class="fw-bold text-primary" id="anagram">{{randomWord}}</h3>
      
      <h3 class="fw-bold text-success" id="answer">{{answer}}</h3>
      
        <div>
          <div class="my-3">
            <h3>Answer Here:</h3>
            <input type="text" class="form-control" v-model="answer" ref="answer" placeholder="Your Answer" aria-label="Answer" id="answer" aria-describedby="Answer" />
          </div>
        </div>
        <div class="row input-group">
          <div class="col input-group">
            <h4>Anagrams left: {{anagramsLeft}}</h4>
          </div>
          <div class="col">
            <button class="btn btn-lg btn-success form-control ms-4" @click="isAnagram(randomWord, answer)">Enter</button>
          </div>
          <div class="row mt-3">
            <!--<h4>Anagrams guessed: {{Object.values(anagrams)[0][0][0].toString()}}</h4>-->
            <h4>Anagrams guessed: {{anagramsGuessed}}</h4>
          </div>
          <div class="mt-3">
            <h3><Score :score="score" /></h3>
            <!-- https://stackoverflow.com/questions/67861840/vue-js-problem-with-incrementing-value-by-one-in-parent-component-using-emit -->
          </div>
        </div>
    </div>   
  </div>
</template>

<script>
import anagrams from "../../src/helpers/anagrams.js";
import Score from './Score';
import {randInt} from '../helpers/gameplay.js';

export default {
  name: "PrototypeAnagrams",
  components: {
    Score
  },
  data: function() {
    return {
      // anagrams: anagrams,
      match: false,
      // anagramsLeft: 0,
      answer: ''.toLowerCase(),
      anagram: true,
      score: 0,
      anagramsLeft: Object.values(anagrams)[0][0].length - 1, // Maybe set a default number like 3? 
      anagramsGuessed: [],
      randomWord: Object.values(anagrams)[0][0][randInt(0,4)],
      // randomOuter: '',
      wordsChosen: []
      // randomOuter?
      
      // List correct answers somewhere below input
      // Change to display the number of anagrams remaining   
    }
  },
  props: {
          /*
https://michaelnthiessen.com/avoid-mutating-prop-directly/
The important thing here, is that v-model is mutating the value that you give to it.
This means that you can't use props with v-model,
          */
          /*
Only the component can change it's own state
Only the parent of the component can change the props
      */
    // randomWord: String,
    // anagrams: Array
  },
  beforeCreate() {
    this.$nextTick(() => this.$refs.answer.focus());
    // let outerArray = Object.values(anagrams)[0];
    // this.randomOuter = Object.values(anagrams)[0][randInt(0, outerArray.length - 1)];
    // this.wordsChosen.push(randomOuter.slice(this.randomWord));
    // this.randomWord = Object.values(anagrams)[0][0][randInt(0,4)];
  },
  methods: {
  // Methods are functions that can be called as normal JS functions,
  // but computed properties will be “re-calculated” anytime some data changes in the component.
  // Unlike computed properties, the return values of methods are never cached and the function will do its job every time it is called.
  // For this reason, you should use a computed property if the value returned is likely to be relatively static.
    isAnagram(anagram, answer) {
      // answer has to be in the correct array so the user can't use fake words
      anagram = document.getElementById('anagram');
      answer = document.getElementById('answer');
      anagram = anagram.innerText.replace(/[\W_]+/g, "");
      answer = answer.innerText.replace(/[\W_]+/g, "");
      const anagramSorted = anagram.split("").sort().join("");
      const answerSorted = answer.split("").sort().join("");
      let outerArray = Object.values(anagrams)[0];
      let randomOuter = Object.values(anagrams)[0][randInt(0, outerArray.length - 1)];
      this.randomWord = Object.values(randomOuter)[randInt(0,randomOuter.length - 1)];
      // let innerArray = Object.values(anagrams)[0][0];
      // let firstWord = Object.values(anagrams)[0][0][0];
      // Try to find length of each sub-array to select a random word
      // Splice method to remove array so it can't be repeated
      // Try chooseArray and chooseWord methods below
      // this.randomWord = Object.values(anagrams)[0][randInt(0,outerArray.length-1)][randInt(0,innerArray.length-1)];
      
      // let randomOuter = Object.values(anagrams)[0][randInt(0, outerArray.length - 1)];
      // console.log("randomOuter: " + randomOuter)
      // console.log("randomOuter[0]: " + randomOuter[0]);
      // console.log("randomOuter.length: " + randomOuter.length);
      // let randomWord = Object.values(randomOuter)[randInt(0,innerArray.length-1)];
      // let randomWord = Object.values(randomOuter)[randInt(0,randomOuter.length - 1)];
      // console.log("randomWord " + randomWord);
      console.log("this.randomWord: " + this.randomWord);
      if (anagramSorted === answerSorted && !(this.anagramsGuessed.includes(answer)) && !(answer === anagram) && !(this.wordsChosen.includes(anagram))) {
        this.score++;
        this.answer = '';
        this.anagramsGuessed.push(answer);
        this.anagramsLeft -= 1;
        console.log("this.anagramsGuessed: " + this.anagramsGuessed);
        this.$nextTick(() => this.$refs.answer.focus());
      } else if (this.anagramsGuessed.includes(answer) || answer === anagram) { 
        this.answer = '';
        this.$nextTick(() => this.$refs.answer.focus());
      } else {
        this.answer = '';
        this.$nextTick(() => this.$refs.answer.focus());
      }
      if (this.anagramsLeft < 1) {
        // let wordsChosen = [];
        let randomOuter = Object.values(anagrams)[0][randInt(0, outerArray.length - 1)];
        console.log("this.randomOuter: " + randomOuter);
        this.wordsChosen.push(randomOuter.slice(this.randomWord));
        console.log("this.wordsChosen: " + this.wordsChosen);
        this.randomWord = Object.values(randomOuter)[randInt(0,randomOuter.length - 1)];
        
        // console.log("randomOuter.slice(this.randomWord): " + randomOuter.slice(this.randomWord));
        // console.log("randomOuter.findIndex(this.randomWord): " + randomOuter.findIndex(this.randomWord));
        let index = randomOuter.findIndex(word => word === this.randomWord);
        // console.log("randomOuter.splice(this.randomWord): " + randomOuter.splice(this.randomWord));
        console.log("Array position of this.randomWord: " + index);
        this.anagramsGuessed = [];
        this.anagramsLeft = randomOuter.length - 1;
        // case statement for each word length ex. (anagrams)[1], (anagrams)[2]
      }
      // console.log("this.anagramsLeft: " + this.anagramsLeft);
      // console.log("this.anagramsGuessed.length" + this.anagramsGuessed.length);
      return anagramSorted === answerSorted;
      },
    chooseArray() {
      // You will first select a random array from the outer array.
      // Be sure to only choose from arrays that contain words with the specified number of letters. 
    },
    chooseWord() {
      // Then select a random word from that array. See randomWord below.
      // You should display that word along with the number of anagrams it has
    },
    changeWord() {
      // let outerArray = Object.values(anagrams)[0];
      // let innerArray = Object.values(anagrams)[0][0];
      // console.log("word changed");
      // console.log("************");
      // let randomOuter = Object.values(anagrams)[0][randInt(0, outerArray.length - 1)];
      // console.log("randomOuter: " + randomOuter)
      // console.log("randomOuter[0]: " + randomOuter[0]);
      // console.log("randomOuter.length: " + randomOuter.length);
      // let randomWord = Object.values(randomOuter)[randInt(0,innerArray.length-1)];
      // let randomWord = Object.values(randomOuter)[randInt(0,randomOuter.length - 1)];
      // console.log("randomWord: " + randomWord);
      // console.log("this.randomWord: " + this.randomWord);
      // console.log("this.randomWord.length: " + this.randomWord.length);
      // this.anagramsGuessed = [];
      // this.anagramsLeft = randomOuter.length;
      // console.log("innerArray: "innerArray);
      // this.randomWord = Object.values(anagrams)[0][randInt(0,outerArray.length-1)][randInt(0,innerArray.length-1)];
      // innerArray.splice(this.randomWord); // remove word from array so it doesn't get chosen again.
      // Once a word is chosen from array, remove entire array, not just the word
      // innerArray.splice(this.randomWord) leaves an empty array --
      // then select an array with length greater than 0
      // console.log("getOwnPropertyNames: " + Object.getOwnPropertyNames(this.randomWord));
      // console.log(innerArray);
      // this.anagramsLeft = Object.values(anagrams)[0][0].length - 1;
      // this.anagramsLeft = 0;
      // this.anagramsLeft = Object.values(anagrams[0][1].length - 1 );
      // As soon as the user guesses all of the possible anagrams in the current array of words,
      // another random array with words of the same length should be grabbed and a new word should be displayed.
    }
  },
  computed: {
  // Methods are functions that can be called as normal JS functions,
  // but computed properties will be “re-calculated” anytime some data changes in the component.
  // Any time you have a piece of dynamic data that can be calculated based on other data in the template,
  // you should consider making it into a computed property.
  /*
    randomWord: function() {
      return Object.values(anagrams)[0][0][randInt(0,4)];
    }
  */
  // When remaining anagrams reaches 0, choose a new word of the same length
  } 
}
</script>

<style scoped>

</style>