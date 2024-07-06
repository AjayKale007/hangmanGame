import random
words_list=["apple","banana","mango","orange","watermelon","pumpkin","papaya"]
lives =6

chosen_word=random.choice(words_list)
print(chosen_word)

display=[]
#for i in range(len(chosen_word)):
for letter in chosen_word:
    display +='_'
print(display)
game_over =False
while not game_over:
    guessed_letter = input("Guess the letter: ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guessed_letter:
            display[i] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You Loose !")

    if '_' not in display :
        game_over = True
        print("Congratulation You Win The Game !")