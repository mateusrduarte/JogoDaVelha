import os

board = [' '] * 10
gameState = True
announce = ''

def resetBoard():
    global board, gameState
    board = [' '] * 10
    gameState = True

def displayBoard():
    os.system('clear') or None

    print(" "+ board[7] +" |"+ board[8] +" | " + board[9] +" ")
    print("------------")
    print(" "+ board[4] +" |"+ board[5] +" | " + board[6] +" ")
    print("------------")
    print(" "+ board[1] +" |"+ board[2] +" | " + board[3] +" ")

def winCheck(board, player):
    if (board[7] == board[8] == board[9] == player) or \
        (board[4] == board[5] == board[6] == player) or \
        (board[1] == board[2] == board[3] == player) or \
        (board[7] == board[4] == board[1] == player) or \
        (board[8] == board[5] == board[2] == player) or \
        (board[9] == board[6] == board[3] == player) or \
        (board[1] == board[5] == board[9] == player) or \
        (board[3] == board[5] == board[7] == player):

        return True
    else:
        return False

def fullBoardCheck(board):
    if " " in board[1:]:
        return False
    else:
        return True

def askPlayer(mark):
    global board

    req =  'Choose where  to pleas you: ' + mark + '\n'
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("Sorry, please input  a number between 1 - 9.")
            continue
        
        if choice not in range(1, 10):
            print("Sorry, please input  a number between 1 - 9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("That space isn't empty!")
            continue

def playerChoice(mark):
    global board, gameState, announce

    announce = ''
    mark = str(mark)
    askPlayer(mark)

    if winCheck(board, mark):
        os.system('clear') or None
        displayBoard()
        announce = mark + " Wins! Congatulations"
        gameState = False

    os.system('clear') or None
    displayBoard()

    if fullBoardCheck(board):
        announce = "Tie!"
        gameState = False

    return gameState, announce

def playGame():
    resetBoard()
    global announce

    X = 'X'
    O = 'O'

    while True:
        os.system('clear') or None
        displayBoard()

        gameState, announce = playerChoice(X)
        print(announce)
        if gameState == False:
            break

        gameState, announce = playerChoice(O)
        print(announce)
        if gameState == False:
            break

    rematch = input('Would you like  to play again? y/n \n')
    if rematch == 'y':
        playGame()
    else:
        print("Thanks for playing!")

playGame()