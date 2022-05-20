<template>
  <main id="main-container">
    <div v-if="screen === 'config'" id="config-container">
      <h1 class="text-center mb-3">Anagram Hunt</h1>
      <ol>
        <li>Choose word length.</li>
        <li>Press Play button.</li>
        <li>Find as many anagrams as you can.</li>
      </ol>
      <SelectInput :currentValue="maxNumber" label="Choose Word Length"
        id="max-number" v-model="maxNumber" :options="numbers" />
      <PlayButton @play-button-click="play" />
    </div>
    <div v-else-if="screen === 'play'" id="game-container" class="text-center">
      <transition name="slide">
        <template v-if="timeLeft === 0">
          <div>
            <h2>Time's Up!</h2>
            <strong class="big">You Answered</strong>
            <div class="huge">
              {{score}}
            </div>
            <strong class="big">Questions Correctly</strong>
            <button class="btn btn-primary form-control m-1"
              v-on:click="restart()">
                Play Again with Same Settings
            </button>
            <button class="btn btn-secondary form-control m-1"
              v-on:click="config()">
                Change Settings
            </button>
          </div>
        </template>
      </transition>
      <transition name="slide-right">
        <template v-if="timeLeft > 0">
          <div>
            <div class="row border-bottom" id="scoreboard">
              
              <div class="col px-3 text-left">
                <Score :score="score" />
              </div>

              <div class="col px-3 text-right">
                <Timer :timeLeft="timeLeft" />
              </div>
            </div>
            <div class="mt-3">
              <h3>Anagram:</h3>
            </div>
            <div class="row border-bottom">
              <div class="col text-center">
                <h3 class="fw-bold text-primary" id="anagram">{{anagram}}</h3>
                <h3 class="fw-bold text-success" id="answer">{{answer}}</h3>
                <div>
                  <div class="my-3">
                    <h3>Answer Here:</h3>
                    <input type="text" class="form-control" v-model="answer" ref="answer" placeholder="Your Answer" aria-label="Answer" id="answer" aria-describedby="Answer" />
                  </div>
                </div>
                <InputButton @is-anagram="isAnagram" />
                <Anagrams :anagramsGuessed="anagramsGuessed" :anagramsLeft="anagramsLeft" />
              </div>
            </div>
          </div>
        </template>
      </transition>
    </div>
  </main>
</template>

<script>
  import SelectInput from './SelectInput';
  import PlayButton from './PlayButton';
  import InputButton from './InputButton.vue';
  import Score from './Score';
  import Timer from './Timer';
  import Anagrams from './Anagrams';
  import anagrams from "../../src/helpers/anagrams.js";
  import {randInt} from '../helpers/gameplay.js';
  export default {
    name: 'Main',

    components: {
      SelectInput,
      PlayButton,
      Score,
      Timer,
      Anagrams,
      InputButton
    },
    data: function() {
      return {
        operations: [
          ['5'],['6'],['7'],['8']
        ],
        screen: 'config',
        input: '',
        maxNumber: '5',
        anagrams: anagrams,
        outerArray: [1],
        // randomOuter: [1],
        randomOuter: Object.values(anagrams)[randInt(0,3)][randInt(0,8)],
        anagram: [],
        answer: '',
        anagramsLeft: Object.values(anagrams)[0][0][randInt(0,4)],
        anagramsGuessed: [],
        answered: false,
        score: 0,
        gameLength: 90,
        timeLeft: 0
      }
    },
    methods: {

      chooseAnagram() {
        console.log();
        console.log("chooseAnagram() called");
        console.log("this.maxNumber: "+ this.maxNumber);
        console.log();

        if (this.outerArray.length === 0 && this.randomOuter.length === 0) {
            this.timeLeft = 1;
            this.answer = 'You Win!';
            console.log("********** WINNER *********");
            return true;
        }

        this.chooseWordLength();
        console.log("this.chooseWordLength() called");
        console.log("this.outerArray.length: " + this.outerArray.length);
        console.log("this.randomOuter.length: " + this.randomOuter.length);
        console.log();
        this.outerArray.splice(this.outerArray.indexOf(this.randomOuter), 1); // remove sub-array from parent
        this.answer = '';
        this.$nextTick(() => this.$refs.answer.focus());
        this.anagramsGuessed = [];

      if (typeof(this.anagram) === 'undefined') {  // out of words? find another array
        this.randomOuter = Object.values(anagrams)[0][randInt(0, this.outerArray.length-1)];
        this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
        this.answer = '';
        this.$nextTick(() => this.$refs.answer.focus());
        this.anagramsGuessed = [];
      }
        this.randomOuter.splice(this.randomOuter.indexOf(this.anagram), 1); // remove chosen anagram from array
        this.anagramsLeft = this.randomOuter.length;
        console.log("this.randomOuter: " + this.randomOuter);
        console.log();
      },

      isAnagram() {

        console.log("this.randomOuter.length: " + this.randomOuter.length);
        console.log();
        console.log("this.randomOuter in isAnagram(): " + this.randomOuter);
        console.log()
        
      if (this.randomOuter.includes(this.answer)) {
        this.anagramsGuessed.push(this.answer);
        this.randomOuter.splice(this.randomOuter.indexOf(this.answer), 1); // remove chosen anagram from array 
        this.score++;
        this.answer = '';
        this.$nextTick(() => this.$refs.answer.focus());
        this.anagramsLeft -= 1;
        console.log("this.randomOuter after correct answer in isAnagram(): " + this.randomOuter);
      }
      if (this.randomOuter.length < 1) {
        this.chooseAnagram();
        this.answer = '';
        this.$nextTick(() => this.$refs.answer.focus());
        this.anagramsGuessed = [];
      }
        this.answer = '';
        this.$nextTick(() => this.$refs.answer.focus());        
      },

      config() {
        this.screen = "config";
      },

      chooseWordLength() {
        let ary = this.maxNumber;
        switch (ary) {
          case '5':
            this.outerArray = Object.values(anagrams)[0]
            this.randomOuter = this.outerArray[randInt(0, this.outerArray.length-1)];
            this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
            break;
          case '6':
            this.outerArray = Object.values(anagrams)[1];
            this.randomOuter = this.outerArray[randInt(0, this.outerArray.length-1)];
            this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
            break;
          case '7':
            this.outerArray = Object.values(anagrams)[2];
            this.randomOuter = this.outerArray[randInt(0, this.outerArray.length-1)];
            this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
            break;
          case '8':
            this.outerArray = Object.values(anagrams)[3]
            this.randomOuter = this.outerArray[randInt(0, this.outerArray.length-1)];
            this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
            break;
        }
      },

      play() {
        this.screen = "play";
        this.startTimer();
        this.$nextTick(() => this.$refs.answer.focus());
        this.chooseAnagram();
      },

      clear() {
        this.input = '';
      },
 
      startTimer() {
        window.addEventListener('keyup', this.handleKeyUp);
        this.timeLeft = this.gameLength;
        if (this.timeLeft > 0) {
          this.timer = setInterval(() => {
            this.timeLeft--;
            if (this.timeLeft === 0) {
              clearInterval(this.timer);
              window.removeEventListener('keyup', this.handleKeyUp);
            }
          }, 1000)
        }
      },
      restart() {
        this.score = 0;
        this.startTimer();
      },

    },
    computed: {
      numbers: function() {
        const numbers = [];
        for (let number = 5; number <= 8; number++) {
          numbers.push([number, number]);
        }
        return numbers;
      }
    }
  }
  
</script>

<style scoped>
  #main-container {
    margin: auto;
    width: 380px;
  }

  button.number-button {
    border-radius: .25em;
    font-size: 3em;
    height: 2em;
    margin: .1em;
    text-align: center;
    width: 2em;
  }

  #clear-button {
    border-radius: .25em;
    font-size: 3em;
    height: 2em;
    margin: .1em;
    text-align: center;
    width: 4.2em;
  }
  
  #scoreboard {
    font-size: 1.5em;
  }

  .big {
    font-size: 1.5em;
  }

  .huge {
    font-size: 5em;
  }

  .slide-leave-active,
  .slide-enter-active {
    position: absolute;
    top: 56px;
    transition: 1s;
    width: 380px;
  }

  .slide-enter {
    transform: translate(-100%, 0);
    transition: opacity .5s;
  }

  .slide-leave-to {
    opacity:0;
    transform: translate(100%, 0);
  }

  .slide-right-leave-active,
  .slide-right-enter-active {
    position: absolute;
    top: 56px;
    transition: 1s;
    width: 380px;
  }

  .slide-right-enter {
    transform: translate(100%, 0);
    transition: opacity .5s;
  }

  .slide-right-leave-to {
    opacity:0;
    transform: translate(-100%, 0);
  }
</style>