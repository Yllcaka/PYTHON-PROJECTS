import os
from numpy import reshape


def board():
    a = 1
    rv = f""
    for i in range(1,4):
        if i >1:
            a = a + 3
        rv += f" {a} | {a+1} | {a+2} \n"
        if i ==3:
            continue
        rv += "============\n"
    return rv

def checker(b):
    for i in ["============\n","\n"," "]:
        b = b.replace(i,"|")
    b = b.split("|")
    b = [i for i in b if i != ""]
    b = reshape(b,(3,3))
    for i in range(3):
        if (b[i][0] == b[i][1] == b[i][2]) or\
           (b[0][i] == b[1][i] == b[2][i]) or\
           (b[0][0] == b[1][1] == b[2][2]) or\
           (b[0][2] == b[1][1] == b[2][0]):
            return True
    return False

def playerSetup():
    selectPlayer = input("'X' or '○'").upper()
    player1 = "○" if selectPlayer == "O" else "X"
    player2 = "X" if player1 == "○" else "○"
    return (player1,player2)

def game(p1,p2):
    turn = p2
    inputs = [str(i) for i in range(1,10)]
    currentBoard = board()
    print(currentBoard)
    while inputs != []:
        turn = p1 if turn == p2 else p2
        action = input(f"Enter {turn} ")
        while action not in inputs:
            action = input(f"Please enter {turn} ")
        currentBoard = currentBoard.replace(action,turn)
        inputs.remove(action)
        os.system("cls" if os.name == "nt" else "clear")
        print(currentBoard)
        if checker(currentBoard):
            print(f"========= \"{turn}\" WON =========")
            return
    print("========= DRAW =========")


player1,player2 = playerSetup()
game(player1,player2)
again = input("Do you wanna play again? (Y/N) ").upper()

while not again.startswith("N"):
    player1 , player2 = playerSetup()
    game(player1 , player2)
    again = input("Do you wanna play again? (Y/N) ").upper()

print("Have a nice day.".upper())