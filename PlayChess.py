import chessPlayer_helperChess

# --- We're playing as the Black side --- #

board = chessPlayer_helperChess.genBoard()
whitePlayer = 10
me = 20
done = False


while not (done):
    print("This is the current Board \n")
    print(chessPlayer_helperChess.printBoard(board))
    print("\n")

    # --- Get White Move --- #
    moveWhite = input("White: Enter piece position and desired position separated by a space! ")
    moveWhiteL = moveWhite.split()
    whiteList = []
    for i in range(0,len(moveWhiteL)):
        whiteList += [int(moveWhiteL[i])]
    # --- whiteList = [initial position, final destination] --- #

    # --- check if valid initial position --- #
    validInit = ((board[whiteList[0]] == 10) | (board[whiteList[0]] == 11) |(board[whiteList[0]] == 12) |(board[whiteList[0]] == 12) |(board[whiteList[0]] == 13) |(board[whiteList[0]] == 14) | (board[whiteList[0]] == 10))
    while not (validInit):
        print("WHITE: Not a valid initial position")
        print(chessPlayer_helperChess.printBoard(board))
        initPos = int(input("What piece do you wish to move? "))
        whiteList[0] = initPos
        validInit = ((board[whiteList[0]] == 10) | (board[whiteList[0]] == 11) |(board[whiteList[0]] == 12) |(board[whiteList[0]] == 12) |(board[whiteList[0]] == 13) |(board[whiteList[0]] == 14) | (board[whiteList[0]] == 10))

    # --- Check if final destination is valid --- #
    possibleMoves = chessPlayer_helperChess.GetPieceLegalMoves(board,whiteList[0])

    while whiteList[1] not in possibleMoves and whiteList[1] != False:
        print("WHITE: Not a legal move for the piece")
        print(chessPlayer_helperChess.printBoard(board))
        finalPos = int(input("Where do you wish to move your piece? "))
        whiteList[1] = finalPos

    # --- Check if Game is Over for me (the AI) --- #
    # --> Will my king be eaten?
    if chessPlayer_helperChess.isCheckmate(board,me) == True:
        print("Checkmate, White won the game. ")
        break
    # --- Check if Game tied (Can I make any moves after he made his while my king isn't in Check) --- #
    if chessPlayer_helperChess.isStalemate(board,me) == True:
        print("Game is in Stalemate")
        break

    # --- Move Players Piece and create empty pos --- #
    board[whiteList[0]],board[whiteList[1]] = 0,board[whiteList[0]]
    print(chessPlayer_helperChess.printBoard(board))

    # ------------------ My Moves ------------------ #
    # Find the most valuable moves: low --> High <> pawn ---> King
    # First check if our move can create a checkmate --> A Winning Move
    possibleMoves = chessPlayer_helperChess.allMoves(board,me)
    winningMoves = chessPlayer_helperChess.genWinningMove(board,me)
    #nonLosingPos protects us from checkmate and picks best move if no check
    nonLosing = chessPlayer_helperChess.genNonLosing(board,me)

    print(winningMoves)
    if (winningMoves != False) and (winningMoves != []):
        board[winningMoves[0][0]],board[winningMoves[0][1]] = 0,board[winningMoves[0][0]]
        print("Black won the game! ")
        break

    elif nonLosing != False:
        board[nonLosing[0][0]],board[nonLosing[0][1]] = 0,board[nonLosing[0][0]]

    if chessPlayer_helperChess.isStalemate(board,whitePlayer) == True:
        print("Game is in Stalemate")
        break

    elif chessPlayer_helperChess.isCheckmate(board,whitePlayer) == True:
        print("Checkmate, Black won the game. ")
        break
