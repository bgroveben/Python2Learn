# Python2Learn

### In this project, you will use your new knowledge of Python to create Python versions of the two Play2Learn games (Anagram Hunt and Math Facts Practice) that can be played from the console.


## TODO:
Make sure game length is correct and you use the full list of anagrams.
Make sure console output is correct.
Clean up code and check for bugs.
Make a note about the following:
>100 / 2 = ?:
50.0
You have 0.0 seconds left.
Enter an answer:
Time is up!
Sorry, you didn’t get that answer in on time.
Press Enter to see your score...



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

I created a threading.Timer object that calls a function which displays a  single message when time runs out.
There is a game timer (started at the same time) running on the main thread that displays the game time remaining to the user.
If the user guesses all of the anagrams, the timer is cancelled.
