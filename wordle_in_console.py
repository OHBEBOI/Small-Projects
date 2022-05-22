from random import randint
from conversions import lst_to_string

done = False
WORDS = ['BOAT', 'WORD', 'DUMB', 'READ', 'LOUD', 'CATS', 'DOGS', 'LUCK', 'DUCK']
p1 = []
p2 = []


def choose_word():
    n = randint(0, len(WORDS))
    rand_word = WORDS[n]
    return rand_word

def check(inp_word:str):
    rand_word = chosen_word
    
    for i in inp_word:
        if i in rand_word:
            if i not in p2:
                p2.append(i)

    for i in range(len(rand_word)):
        if inp_word[i] == rand_word[i]:
            p1.append(inp_word[i])

    for i in p2:
        if i in p1:
            p2.remove(i)
    return p1, p2

def feedback():
    
    if inp == chosen_word:
        print("YOU WIN!")
        return 1
    elif tries == 0:
        print("SORRY, YOU LOSE!")
        return -1
    else:
        t = check(inp)
        print("Letters in the word in the correct place: ", lst_to_string(t[0]))
        print("Letters in the word but not in the correct place: ", lst_to_string(t[1]))
        return 0

def choose_diff():
    diff = int(input("Enter 1 for Easy:\n2 for Intermediate:\n3 for Pro:\n"))
    if diff == 1:
        tries = 8
    elif diff == 2:
        tries = 6
    elif diff == 3:
        tries = 4
    return tries

#__main__

chosen_word = choose_word()
tries = choose_diff()
while tries >= 0:
    inp = eval(input("Enter a  4 letter word in caps: "))
    x = feedback()
    
    if x == 1 | x == -1:
        break

    tries -= 1
    print('\n')

