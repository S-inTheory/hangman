import random


def play():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    unknown_word = random.choice(word_list).lower()
    word_len = len(unknown_word)
    normal_letter = 'abcdefghijklmnopqrstuvwxyz'
    spaces = '-' * word_len
    tries = 8
    word = '-' * word_len
    typed_letters = []
    while tries >= 0:
        if tries == 0:
            print('You are hanged!')
            print()
            break
        elif tries > 0 and unknown_word != word:
            print()
            print(word)
            letter = input('Input a letter: ')
            if letter in typed_letters:
                print('You already typed this letter')
            elif len(letter) > 1 or letter == '':
                print('You should print a single letter')
            elif letter not in normal_letter:
                print('It is not an ASCII lowercase letter')
            elif letter not in unknown_word:
                spaces = list(spaces)
                word = ''.join(spaces).lower()
                print('No such letter in the word')
                tries -= 1
                typed_letters.append(letter)
            elif letter in unknown_word:
                if letter not in word:
                    if unknown_word.count(letter) == 2:
                        letter_index_1 = unknown_word.find(letter)
                        letter_index_2 = unknown_word.rfind(letter)
                        spaces = list(spaces)
                        spaces[letter_index_1] = letter
                        spaces[letter_index_2] = letter
                        word = ''.join(spaces).lower()
                        typed_letters.append(letter)
                        if unknown_word == word:
                            print(f'You guessed the word {word}!')
                            print('You survived!')
                            print()
                            break
                    elif unknown_word.count(letter) == 1:
                        letter_index = unknown_word.find(letter)
                        spaces = list(spaces)
                        spaces[letter_index] = letter
                        word = ''.join(spaces).lower()
                        typed_letters.append(letter)
                        if unknown_word == word:
                            print(f'You guessed the word {word}!')
                            print('You survived!')
                            print()
                            break


print('H A N G M A N')
while True:
    decision = input('Type "play" to play the game, "exit" to quit: ')
    if decision == 'play':
        play()
    elif decision == 'exit':
        break
    else:
        continue

