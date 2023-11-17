# wordle_ai

## Overview
This project implements a rudimentary Wordle game in the console along with an AI component. Wordle is a word-guessing game where the player attempts to guess a secret word within a limited number of attempts. In this implementation, an AI is included to make guesses based on feedback from previous attempts.

## Files
wordle.py: The main program file containing the game logic and user interface for playing Wordle.

wordle_stats.py: A companion program for statistical analysis of the AI's performance across all possible wordle words.

Wordle_Words.txt: A text file containing the possible words that can be the Wordle answer.

allowed_guesses.txt: A text file containing the allowed guesses in the Wordle game.

## Usage
-To play the Wordle game, run wordle.py. 

-To analyze the AI's performance, run wordle_stats.py. 

-Ensure that the Wordle_Words.txt and allowed_guesses.txt files are present in the same directory. 

-You don't need wordle_stats.py to run wordle.py, and vice versa. 

## How to Play
1. Run the wordle.py program to start a game. The program will randomly select a word for the player to guess. This can be manually set by altering the value of 'the_word' in the code if, for instance, you wanted to input the wordle for the day. 
2. You can toggle between either you or the AI guessing the word. This can be done by either entering their guess manually or letting the AI make a guess by entering 'A'.
3. After each guess, the program provides feedback, highlighting correct letters in green, present letters in yellow, and incorrect letters in the default color.
4. The game continues until the player correctly guesses the word or exceeds the maximum allowed attempts (6 in this implementation).

## AI Strategy
The AI utilizes a weighted scoring system to prioritize letters that are the most frequently occurring in the remaining possible words. The scoring considers both the frequency of letters in the remaining possible words and penalizes repeated letters in a guessed word.

## Statistical Analysis
The wordle_stats.py program allows for statistical analysis of the AI's performance across multiple rounds. It plays the game with different secret words, recording the number of attempts required for each round. The average guess length is then calculated and displayed at the end.

Currently, the AI has an average guess of 3.627

## Note
This program assumes that the terminal supports ANSI escape codes for colored text.
