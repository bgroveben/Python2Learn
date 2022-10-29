# Python2Learn

### Python versions of the two Play2Learn games (Anagram Hunt and Math Facts Practice) that can be played from the console.

==**INSTRUCTIONS:**==
Just open your console, cd to either the math_facts or anagram_hunt directory and type:
> `-> python math_facts.py`

or:
> `-> python anagram_hunt.py`

to give your brain some exercise.
The length of the games is hard-coded for this assignment.
Want a longer or shorter game?
Go to `MathFacts.py`, `run_game()`, line 185 and change `cls._game_length = 30`.
`cls._game_length` in `AnagramHunt.py` is in `gameplay()` on line 72.

*Cheat Codes:*
- ~~Up, Up, Down, Down, Left, Right, Left, Right, B, A, Start~~
- Want to cheat on your math? Go to `MathFacts.py`, `do_math()`,  line 74 and uncomment (decomment?)  `# print(answer)`
- Want a shorter list of anagrams? Go to `AnagramHunt.py`, `read_anagrams()`,  line 40, and change the code to:
`with open('../data/fewer_anagrams.json', 'r') as f:`
- Want to see all of the anagrams for each word? Go to `AnagramHunt.py`, `gameplay()`, line 86 and uncomment `print(f"{random_inner} Ch3@t3r")`
