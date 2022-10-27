# Python2Learn

### In this project, you will use your new knowledge of Python to create Python versions of the two Play2Learn games (Anagram Hunt and Math Facts Practice) that can be played from the console.


## TODO:
Remove or comment out cheat codes.
Make sure game length is correct and you use the full list of anagrams.
Make sure console output is correct.
Clean up code and check for bugs.

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
Otherwise, user input is interrupted.
It's basically the same kind of Timer object that is used for both games.
