<template>
  <div id="body">
    <div>
        <div class="row input-group">
          
            <h4>Anagrams left: {{anagramsLeft}}</h4>
          
          <!--
          <div class="col">
            
            <button class="btn btn-lg btn-success form-control ms-4" @click="isAnagram(anagram, answer)">Enter</button>
            <button class="btn btn-lg btn-success form-control ms-4" @click="$emit(isAnagram(anagram, answer))">Emit</button>
            
            <button class="btn btn-lg btn-success form-control ms-4" @click="$emit(anagramsLeft)">Emit</button>
          </div>
          -->
          <div class="row mt-3">
            <!--<h4>Anagrams guessed: {{Object.values(anagrams)[0][0][0].toString()}}</h4>-->
            <h4>Anagrams guessed: {{anagramsGuessed}}</h4>
          </div>
          <!--
          <div class="mt-3">
            <h3><Score :score="score" /></h3>
            https://stackoverflow.com/questions/67861840/vue-js-problem-with-incrementing-value-by-one-in-parent-component-using-emit
          </div>
          -->
        </div>
    </div>   
  </div>
</template>

<script>

export default {
    name: 'Anagrams',
    props: {
        // anagram: String, // Word chosen by the program
        // answer: String,  // User input
        anagramsGuessed: Array, // Correct answers by user
        anagramsLeft: Number // Number of words left in anagram's array
    },
    methods: {
        /*
        isAnagram(anagram, answer) {
            anagram = document.getElementById('anagram');
            answer = document.getElementById('answer');
            anagram = anagram.innerText.replace(/[\W_]+/g, "");
            answer = answer.innerText.replace(/[\W_]+/g, "");
            const anagramSorted = anagram.split("").sort().join("");
            const answerSorted = answer.split("").sort().join("");
            let outerArray = Object.values(anagrams)[0];
            let randomOuter = Object.values(anagrams)[0][randInt(0, outerArray.length - 1)];
            this.randomWord = Object.values(randomOuter)[randInt(0,randomOuter.length - 1)];
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
            }
            */
        }
    }
</script>