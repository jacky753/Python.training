
word_list = ["milk","curp","baseball"]

import random


def hangman():
    wrong = 0

    i = random.randint(0,2)

    word = word_list[i]

    stages = ["",
              "________       ",
              "|              ",
              "|              ",
              "|       |      ",
              "|       0      ",
              "|      /|/     ",
              "|      / /     ",
              "|              ",
              ]
    rletters = list(word)
    boad = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a word"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            boad[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(boad))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in boad:
            print("You are winner!")
            print(" ".join(boad))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print ("You are loser! The answer is {}.".format(word))

hangman()        
