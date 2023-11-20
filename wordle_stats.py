import random

ai_guesses = []
word_counter = 0

BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

CORRECT = 1
PRESENT = 2
ABSENT = 3

allowed = [set(), set(), set(), set(), set()]
needed_words = set()
words_list = []
used_words = []

for e in range(5):
    allowed[e].update("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

game_over_ = False

with open("Wordle_Words.txt") as Wordle_File:
    words = Wordle_File.readlines()
    word_set = set()
    for line in words:
        line = line.split()
        for word in line:
            word_set.add(word)
    sorted_word_set = sorted(word_set)

with open("allowed_guesses.txt") as wordle_guesses:
    allowed_words = wordle_guesses.readlines()
    allowed_word_set = set(word.strip() for word in allowed_words if word.strip())
    sorted_allowed_word_set = sorted(allowed_word_set)

the_word = random.choice(sorted_word_set)
the_word = 'sight'

def is_possible(word, allowed, needed_words):
    for i in range(len(word)):
        if word[i] not in allowed[i]:
            return False
        for m in needed_words:
            if m not in word:
                return False
        if word[i] in used_words:
            return False
    return True

def possible_words(sorted_word_set, allowed, needed_words):
    global words_list
    words_list.clear()
    words_list.extend(word for word in sorted_word_set if is_possible(word, allowed, needed_words))
    return [word for word in sorted_word_set if is_possible(word, allowed, needed_words)]

def weights():
    global used_words
    scores = {
        "a": 0, "b": 0,
        "c": 0, "d": 0,
        "e": 0, "f": 0,
        "g": 0, "h": 0,
        "i": 0, "j": 0,
        "k": 0, "l": 0,
        "m": 0, "n": 0,
        "o": 0, "p": 0,
        "q": 0, "r": 0,
        "s": 0, "t": 0,
        "u": 0, "v": 0,
        "w": 0, "x": 0,
        "y": 0, "z": 0,
    }
    word_scores = {}

    for word in words_list:
        for letter in word:
            scores[letter] += 1

    for w in range(len(words_list)):
        word_score = 0
        word1 = []
        for letter in words_list[w]:
            word_score += scores[letter]
            word1.append(letter)

            if word1.count(letter) > 1:
                for letter in word1:
                    word_score -= scores[letter] / 1.5

        word_scores.update({w: word_score})

    max1 = max(word_scores, key=lambda key: word_scores[key])
    used_words.append(words_list[max1])

    if words_list[max1] in used_words:
        word_scores.update({words_list[max1]: 0})

    scores.clear()
    word_scores.clear()
    return words_list[max1]

def AI_guess():
    global words_list
    if word_counter == 0:
        guess = 'slate'
    else:
        possible_words(sorted_word_set, allowed, needed_words)
        guess = weights()
    return guess

def game_over(guess):
    global game_over_
    if guess == the_word:
        print("You won!")
        game_over_ = True 
    elif word_counter == 6:
        print(f"Game Over, the word was {the_word}")
        game_over_ = True

def word_guess():
    global word_counter
    guess = ""
    guess = AI_guess()  # Let AI make the guess
    check_guess(guess)
    word_counter += 1
    game_over(guess)

    return guess

def wordle_digits_from_guess(secret_word, guess):
    secret_word_list = list(secret_word)
    guess_list = list(guess)
    result = [0] * len(guess_list)

    for slots_examined in range(len(secret_word_list)):
        if secret_word_list[slots_examined] == guess_list[slots_examined]:
            result[slots_examined] = CORRECT
            secret_word_list[slots_examined] = "_"

    for slots_examined in range(len(secret_word_list)):
        if result[slots_examined] != 0:
            continue

        g = guess_list[slots_examined]

        try:
            guess_index = secret_word_list.index(g)
        except ValueError:
            guess_index = None

        if guess_index is not None:
            result[slots_examined] = PRESENT
            secret_word_list[guess_index] = "_"
        else:
            result[slots_examined] = ABSENT

    return result

def check_guess(guess):
    global needed_words
    global the_word
    global allowed
    correct_words = []
    
    feedback = wordle_digits_from_guess(the_word, guess)
    
    for i, status in enumerate(feedback):
        g_char = guess[i]
        
        if status == CORRECT:
            print(BG_GREEN + g_char + RESET, end=" ")
            allowed[i] = {g_char}    
            if g_char not in correct_words:
                correct_words.append(g_char)
                
        if status == PRESENT:
            print(BG_YELLOW + g_char + RESET, end=" ")
            needed_words.add(g_char)
            if g_char in allowed[i]:
                allowed[i].remove(g_char)

        if status == ABSENT:
            print(g_char, end=" ")
            for j in range(len(guess)):
                if g_char in allowed[j]:
                    if g_char not in needed_words:
                        if g_char not in correct_words:
                            allowed[j].remove(g_char)
                        else:
                            for pos in allowed:
                                if not(len(pos) == 1 and g_char in pos):
                                    if g_char in pos:
                                        pos.remove(g_char)
    print()

avg_count = []
def main_loop():
    global the_word
    global game_over_
    global word_counter
    
    global needed_words
    global words_list
    global used_words
    global allowed
    global avg_count
    for e in range(len(sorted_word_set)):  # Play 100 rounds
        the_word = sorted_word_set[e]
        game_over_ = False
        word_counter = 0
        print(f"\nPlaying with the word: {the_word}")
        while not game_over_:
            word_guess()
        needed_words.clear()
        words_list.clear
        used_words.clear
        for e in range(5):
            allowed[e].update("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        avg_count.append(word_counter)

    average_guess_length = sum(avg_count) / len(avg_count)
    print(f"\nAverage Guess Length: {average_guess_length}")

main_loop()

