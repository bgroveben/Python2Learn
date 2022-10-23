# Python2Learn

### In this project, you will use your new knowledge of Python to create Python versions of the two Play2Learn games (Anagram Hunt and Math Facts Practice) that can be played from the console.


## TODO:

### Bug In Anagram Hunt that I can't reproduce
-- try to test for if
-- maybe get rid of pynput.keyboard and use MathFacts ending?

>The word is: CRATES
There are 4 unguessed anagrams.
You have 3.0 seconds left.
Make a guess: bnf
Time is up!
Sorry, you didn’t get that last one in on time.
You got 9 anagrams for 6-letter words
*********************************************
BNF is not a valid anagram. Please try again.
['carets', 'caters', 'crates', 'reacts', 'traces'] Ch3@t3r
The word is: CRATES
There are 4 unguessed anagrams.
You have 0.0 seconds left.
Make a guess: bgt
Press Enter to play again.



Use keyboard interrupt in MathFacts?
Fix Math Facts division.
Complete tests.

The assignment instructions for Anagram Hunt specify:

>The game should end when the timer runs out or when you get through all of the anagram sets for the specified length. If you check the time and it is up, you can display a message like this:

`Time is up!`
`You got 7 anagrams for 5-letter words!`
`Press Enter to play again.`

>If the time is already up when you submit an answer, you should get a message like this:`

`Time is up!`
`Sorry, you didn’t get that last one in on time.`
`You got 7 anagrams for 5-letter words!`
`Press Enter to play again.`

I tried to make a timer that would print both messages, but failed several times.
So I created a threading.Timer object that calls a function which displays a  single message when time runs out.
There is a game timer (started at the same time) running on the main thread that displays the game time remaining to the user.
I also wrote a function that cancels the threading.Timer object and prints out congratulations and the score to the user.
