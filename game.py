XorO = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
# The XorO list has the spaces where either X or O goes in the tic tac toe grid
IndexList = [11, 12, 13, 21, 22, 23, 31, 32, 33]
# The IndexList has all the possible numbers that could be in the LocationIndex variable
# and is used to find which index of the XorO list the "X" or "O" should go.
AlreadyUsed = []
# The places that have already been taken by an "X" or "O" are recorded here.
win = 0
p1turn = 0
p2turn = 0
GameRun = 1
replay = ""


def game_win():
    global win
    global p2turn
    global p1turn
    global replay
    global GameRun
    global XorO
    if (XorO[0] == "X" and XorO[1] == "X" and XorO[2] == "X") or (
            XorO[3] == "X" and XorO[4] == "X" and XorO[5] == "X") or (
            XorO[6] == "X" and XorO[7] == "X" and XorO[8] == "X") or (
            XorO[0] == "X" and XorO[4] == "X" and XorO[8] == "X") or (
            XorO[2] == "X" and XorO[4] == "X" and XorO[6] == "X") or (
            XorO[0] == "X" and XorO[3] == "X" and XorO[6] == "X") or (
            XorO[1] == "X" and XorO[4] == "X" and XorO[7] == "X") or (
            XorO[2] == "X" and XorO[5] == "X" and XorO[8] == "X"):
        print("\t1 |", XorO[0], "|", XorO[1], "|", XorO[2], "|\n\t2 |", XorO[3], "|", XorO[4], "|", XorO[5],
                  "|\n\t3 |",
                  XorO[6], "|", XorO[7], "|", XorO[8], "|")
        print("\n", name1, ", you win!!!\n")
        p2turn = 0
        win = 1
        replay = input("Press R to replay, and anything else to quit: ")
        if replay == "R" or replay == "r":
            win = 0
            XorO = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        else:
            GameRun = 0
            XorO = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    elif (XorO[0] == "O" and XorO[1] == "O" and XorO[2] == "O") or (
            XorO[3] == "O" and XorO[4] == "O" and XorO[5] == "O") or (
            XorO[6] == "O" and XorO[7] == "O" and XorO[8] == "O") or (
            XorO[0] == "O" and XorO[4] == "O" and XorO[8] == "O") or (
            XorO[2] == "O" and XorO[4] == "O" and XorO[6] == "O") or (
            XorO[0] == "O" and XorO[3] == "O" and XorO[6] == "O") or (
            XorO[1] == "O" and XorO[4] == "O" and XorO[7] == "O") or (
            XorO[2] == "O" and XorO[5] == "O" and XorO[8] == "O"):
        print("\t1 |", XorO[0], "|", XorO[1], "|", XorO[2], "|\n\t2 |", XorO[3], "|", XorO[4], "|", XorO[5],
                  "|\n\t3 |",
                  XorO[6], "|", XorO[7], "|", XorO[8], "|")
        print("\n", name2, ", you win!!!\n")
        p2turn = 0
        win = 1
        replay = input("Press R to replay, and anything else to quit: ")
        if replay == "R" or replay == "r":
            win = 0
            XorO = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        else:
            GameRun = 0
            XorO = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    elif "_" not in XorO:
        print("\nIt is a stalemate!\n")
        p2turn = 0
        p1turn = 0
        win = 1
        replay = input("\nPress R to replay, and anything else to quit: \n")
        if replay == "R" or replay == "r":
            win = 0
            XorO = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        else:
            GameRun = 0
            XorO = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


print("\nAre you ready to play Tic Tac Toe???")
print("\n\nInstructions: \nTo win you must get three \"X\"s or \"O\"s in a row!\nSelect which row and column you want "
      "to put your x in when asked.\nIf you run out of spaces on the board and nobody has won, then it is a stalemate!")
name1 = str(input("\nWhat is player 1's name? \n\n"))
name2 = str(input("\nWhat is player 2's name? \n\n"))
while GameRun == 1:
    print("\n\nX's:", name1, "\tO's:", name2)
    while win == 0:
        if p1turn == 3:
            p1turn = 0
            p2turn = 1
        else:
            p1turn = 1
            p2turn = 1
        while p1turn == 1:
            print("\t1 |", XorO[0], "|", XorO[1], "|", XorO[2], "|\n\t2 |", XorO[3], "|", XorO[4], "|", XorO[5],
                  "|\n\t3 |",
                  XorO[6], "|", XorO[7], "|", XorO[8], "|")
            print("\t    1   2   3")
            row = int(input(str(name1) + " which row do you want to put your X in? "))
            column = int(input(str(name1) + " which column do you want to put your X in? "))
            LocationIndex = int(str(row) + str(column))
            if LocationIndex in AlreadyUsed:
                print("That was already selected :( ")
                p1turn = 0
                p2turn = 0
                break
            AlreadyUsed.append(LocationIndex)
            XorO.insert(IndexList.index(LocationIndex), "X")
            XorO.pop(IndexList.index(LocationIndex) + 1)
            p1turn = 0
            game_win()
        while p2turn == 1:
            print("\t1 |", XorO[0], "|", XorO[1], "|", XorO[2], "|\n\t2 |", XorO[3], "|", XorO[4], "|", XorO[5],
                  "|\n\t3 |",
                  XorO[6], "|", XorO[7], "|", XorO[8], "|")
            print("\t    1   2   3")
            row = int(input(str(name2) + " which row do you want to put your O in? "))
            column = int(input(str(name2) + " which column do you want to put your O in? "))
            LocationIndex = int(str(row) + str(column))
            if LocationIndex in AlreadyUsed:
                print("That was already selected :( ")
                p1turn = 3
                p2turn = 3
                break
            AlreadyUsed.append(LocationIndex)
            XorO.insert(IndexList.index(LocationIndex), "O")
            XorO.pop(IndexList.index(LocationIndex) + 1)
            p2turn = 0
            game_win()
