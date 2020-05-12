import time
import os

def load_words(filename, type):
    with open(filename) as word_file:
        if type == "set":
            valid_words = set(word_file.read().split())
        if type == "list":
            valid_words = list(word_file.read().split())

    return valid_words
    

def build_4_plus_word_list(english_words):
    with open('words_4plus.txt','w') as f:
        for word in english_words:
            if len(word)>3 and '%' not in word:
                f.write(word+"\n")
                

def build_7plus_7unique_word_list(english_words):
    unique_7letters = {}
    with open('lucky_7s_words.txt','w') as f:
        for word in english_words:
            key = list(set(list(word)))
            key.sort()
            if len(word) > 6 and unique_letters(word) == 7 and str(key) not in unique_7letters:
                unique_7letters[str(key)] = word
                f.write(word+"\n")


def unique_letters(word):
    return len(set(list(word)))
    

def get_lucky_7s_word():
    epoch_time = int(time.time())
    epoch_day = epoch_time // 86400
    lucky_7s_words = load_words('lucky_7s_words.txt',"list")
    word_index = (epoch_day - 18389) % len(lucky_7s_words) #18389
    return lucky_7s_words[word_index]


def find_center_letter(english_words, letters):
    #build words by letter dictionary
    words_by_letter = {}
    for letter in letters:
        words_by_letter[letter] = set()
    valid_words = set()
    for word in english_words:
        if letters >= set(list(word)):
            for char in word:
                words_by_letter[char].add(word)

    min_words = 1000000
    min_letter = ''
    max_words = 0
    max_letter = ''
    for letter in words_by_letter:
        if len(words_by_letter[letter]) > max_words:
            max_words = len(words_by_letter[letter])
            max_letter = letter
        if len(words_by_letter[letter]) < min_words and len(words_by_letter[letter]) >= 25:
            min_words = len(words_by_letter[letter])
            min_letter = letter
            
    if max_words < 25:
        return max_letter, words_by_letter[max_letter]
    return min_letter, words_by_letter[min_letter]
    
    
def start_game(center_letter, valid_words, letters):
    letters.remove(center_letter)
    guessed_words = []
    points = 0
    letter_list = list(letters)
    last_guess = ""
    while True:
        os.system('cls')
        print("******** LUCKY SEVENS WORD GAME *********")
        print(" ")
        print("POINTS:", points)
        print(len(guessed_words), "WORDS FOUND:")
        print(guessed_words)
        print(" ")
        print("   " + letter_list[0].upper() + " " + letter_list[1].upper())
        print("  " + letter_list[2].upper() + " " + center_letter.upper() + " " + letter_list[3].upper())
        print("   " + letter_list[4].upper() + " " + letter_list[5].upper())
        print(" ")
        if last_guess != "":
            print(last_guess)
        guess = str(input())
        if guess == "Q":
            print("WORDS YOU MISSED:")
            print(valid_words)
            break
        if guess in valid_words:
            guessed_words.append(guess)
            points += len(guess)-3
            valid_words.remove(guess)
            last_guess = guess + " IS A VALID WORD! You got " + str(len(guess)-3) + " points!"
            if len(valid_words) == 0:
                print(last_guess)
                print("CONGRATULATIONS! YOU FOUND ALL THE VALID WORDS! YOUR SCORE: " + str(points))
        else:
            last_guess = guess + " IS AN INVALID WORD. TRY AGAIN."
           



if __name__ == '__main__':
    english_words = load_words('words_4plus.txt',"set")
    lucky_7s_words = load_words('lucky_7s_words.txt',"list")
    
    #print('wizardry:',str(unique_letters('wizardry')))
    #print('bananas:',str(unique_letters('bananas')))
    
    #build_4_plus_word_list(english_words)
    #build_7plus_7unique_word_list(english_words)
    
    daily_lucky_7s_word = get_lucky_7s_word()
    letters = set(list(daily_lucky_7s_word))
    center_letter, valid_words = find_center_letter(english_words,letters)
    
    #print("center letter:",center_letter)
    #print("valid words:", valid_words)
    
    start_game(center_letter,valid_words,letters)