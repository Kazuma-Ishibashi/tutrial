import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_________                ",
              "|                        ",
              "|        |               ",
              "|        O               ",
              "|       /|\              ",
              "|       / \              ",
              "|                        "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter in words:"
        char = input(msg)
        if char in rletters:
            print("Correct!")
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            print("Incorrect answer.")
            wrong +=1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You are Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("You are lose! the answer is {}.".format(word))

q_list = ["cat", "dog", "orange", "coffee", "phone", "movie", "mouse"]

hangman(q_list[random.randint(0,len(q_list)-1)])