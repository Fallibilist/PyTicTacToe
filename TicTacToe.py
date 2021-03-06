def determineStartPlayer():
    userResponse = input("\nPlease pick first player, marker 'X' or 'O': ")

    while (userResponse.upper() != 'X' and userResponse.upper() != 'O'):
        userResponse = input("Invalid Reponse\nPlease pick first player, marker 'X' or 'O': ")

    return userResponse.upper()


def promptToPlayAgain():
    userResponse = input("Would you like to play again? (Y/N): ")

    while (userResponse.upper() != 'Y' and userResponse.upper() != 'N'):
        userResponse = input("Invalid Reponse\nWould you like to play again? (Y/N): ")

    if userResponse.upper() == 'Y':
        ticTacToe()


def printBoard(board):
    EMPTYROW = " *     *     *     *"
    DIVIDER = " * * * * * * * * * *"
    INPUTROWSECTION1 = " *  "
    INPUTROWSECTION2 = "  *  "
    INPUTROWSECTION3 = "  *  "
    INPUTROWSECTION4 = "  *"
    NL = '\n'

    builtBoardString = ""

    builtBoardString += DIVIDER + NL
    builtBoardString += EMPTYROW + NL
    builtBoardString += INPUTROWSECTION1 + board[0][0]
    builtBoardString += INPUTROWSECTION2 + board[0][1]
    builtBoardString += INPUTROWSECTION3 + board[0][2] + INPUTROWSECTION4 + NL
    builtBoardString += EMPTYROW + NL
    builtBoardString += DIVIDER + NL
    builtBoardString += EMPTYROW + NL
    builtBoardString += INPUTROWSECTION1 + board[1][0]
    builtBoardString += INPUTROWSECTION2 + board[1][1]
    builtBoardString += INPUTROWSECTION3 + board[1][2] + INPUTROWSECTION4 + NL
    builtBoardString += EMPTYROW + NL
    builtBoardString += DIVIDER + NL
    builtBoardString += EMPTYROW + NL
    builtBoardString += INPUTROWSECTION1 + board[2][0]
    builtBoardString += INPUTROWSECTION2 + board[2][1]
    builtBoardString += INPUTROWSECTION3 + board[2][2] + INPUTROWSECTION4 + NL
    builtBoardString += EMPTYROW + NL
    builtBoardString += DIVIDER

    print(builtBoardString)


def printInstructions():
    instructionBoard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    printBoard(instructionBoard)


def cellNumToBoardIndex(cellNum):
    boardMap = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }

    return boardMap[cellNum]


def validUserSelection(userResponse, board):
    try:
        userResponse = int(userResponse)
    except ValueError:
        print('Response must be an integer between 1 and 9')
        return False

    if (userResponse < 1 or userResponse > 9):
        print('Response must be between 1 and 9')
        return False

    boardIndexTuple = cellNumToBoardIndex(userResponse)
    if board[boardIndexTuple[0]][boardIndexTuple[1]] != ' ':
        print('Cell already chosen!')
        return False

    return True


def checkIfAPlayerWon(board, currentPlayer):
    for interator in range(3):
        if board[0][interator] == currentPlayer and board[1][interator] == currentPlayer and board[2][
            interator] == currentPlayer:
            return True
        if board[interator][0] == currentPlayer and board[interator][1] == currentPlayer and board[interator][
            2] == currentPlayer:
            return True
    if board[0][0] == currentPlayer and board[1][1] == currentPlayer and board[2][2] == currentPlayer:
        return True
    if board[0][2] == currentPlayer and board[1][1] == currentPlayer and board[2][0] == currentPlayer:
        return True


def swapPlayer(currentPlayer):
    if currentPlayer == 'X':
        return 'O'
    else:
        return 'X'


def ticTacToe():
    gameInProgress = True
    currentPlayer = determineStartPlayer()
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    roundNumber = 1

    printInstructions()

    while gameInProgress:
        print("\nRound " + str(roundNumber))
        userResponse = input("Player " + currentPlayer + " - Enter a number corresponding to an available cell (1-9): ")
        if validUserSelection(userResponse, board):
            boardIndexTuple = cellNumToBoardIndex(int(userResponse))
            board[boardIndexTuple[0]][boardIndexTuple[1]] = currentPlayer
            printBoard(board)

            if checkIfAPlayerWon(board, currentPlayer):
                gameInProgress = False
                print('\nPlayer ' + currentPlayer + ' just won!\n')
                break
            elif roundNumber == 9:
                gameInProgress = False
                print("\nIt's a draw!\n")
                break
            currentPlayer = swapPlayer(currentPlayer)
            roundNumber += 1

    promptToPlayAgain()


ticTacToe()
