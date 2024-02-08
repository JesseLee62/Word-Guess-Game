# Word-Guess-Game
Guess the most common 50 words in the input text file and get the highest score you can!

## Rules:
1. The user have 5 points to start with; the game ends when their total score is negative, or they guess ‘!’ as a letter.
2. If the letter is in the word, get 1 point. However, if the letter is not in the word, subtract 1 from the score.
3. Guessing for a word ends if the user guesses the word or has a negative score.
4. User can keep guessing another word after solve one and keep a cumulative total score.

## Run:
1. put .py file and text file in the same folder
2. use cmd to run the .py file and input the text filename as a argument
```bash
python word-guess-game anat19.txt
```
You can replace "anat19" to any other text file.

## Sample run of the game:
![image](word-guess-game/word-guess-game.jpg)
