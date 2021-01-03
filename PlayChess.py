from chesslib import *
from errors import *
from chessAI import *




def main():
    board = genBoard()
    # we (CPU) is black, player is white
    cpu = 20
    opp = 10
    
    done = False
    print('Welcome. You will be playing with the white pieces.\n')
    while not done:
        printBoard(board)
        
        src,dst = None,None
        while src is None:
            try:
                oppSrc = int(input("Enter the position of the piece you wish to move: "))
                if not 0 <= oppSrc <= 63:
                    raise PositionNotInRangeError(oppSrc)
                if str(board[oppSrc])[0] != "1":
                    raise NotOnTeamError(board,oppSrc)
                
                if len(getPieceLegalMoves(board,oppSrc)) == 0:
                    raise InertPieceError(oppSrc)

                else: 
                    oppPiece = identifyPiece(board,oppSrc)
                    print(f"You have selected your {oppPiece} at position {oppSrc}.\n")
                    src = oppSrc

            except PositionNotInRangeError:
                print(f"{PositionNotInRangeError(oppSrc).message}")
                print("Try again.\n")
            except NotOnTeamError:
                print(f"{NotOnTeamError(board,oppSrc)}")
                print("Try again.\n")
            except InertPieceError:
                # print('Hi')
                print(f"{InertPieceError(oppSrc).message}")
                print("Try again.")
        playerMoves = getPieceLegalMoves(board,src)
        while dst is None:
            try:
                oppDst = int(input(f"Enter the position in which you want to move your {oppPiece}: "))
                if not 0 <= oppDst <= 63:
                    raise PositionNotInRangeError(oppDst)
                if oppDst not in playerMoves:
                    raise InvalidMoveError(oppDst)
                else:
                    dst = oppDst
            except PositionNotInRangeError:
                print(f"{PositionNotInRangeError(oppDst).message}")
                print("Try again.\n")
            except InvalidMoveError:
                print(f"{InvalidMoveError(oppDst).message}")

        board[src],board[dst] = 0,board[src]
        
        if isCheckmate(board,10):
            print("Checkmate. Black wins!")
            done = True
            break
        elif isCheckmate(board,20):
            print("Checkmate. White wins!")
            done = True
            break
        
        cpuCheck = True
        while cpuCheck:
            [move,potentMoves] = chessAI(board,20)
            tmpBoard = list(board)
            tmpBoard[move[0]],tmpBoard[move[1]] = 0,tmpBoard[move[0]]
            cpuCheck = isInCheck(tmpBoard,20)
        
        board[move[0]],board[move[1]] = 0, board[move[0]]

        printBoard(board)

        if isCheckmate(board,20):
            print("Checkmate. White wins!")
            done = True
            break

        if isCheckmate(board,10):
            print("Checkmate. Black wins!")
            done = True
            break



        # done = True       
                        
    



main()