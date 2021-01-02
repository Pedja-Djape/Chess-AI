from chesslib import *
from time import time

class gameTree:

    def __init__(self,board,pts,maxDepth,src,dst):
        self.state = {'eval': pts, 'board': board}
        self.maxDepth = maxDepth
        self.move = [src,dst]
        self.potentMoves, self.children = [],[]

    def material(self,board):
        total = 0
        for i in range(64):
            if board[i] == 15:
                total += 400
            elif board[i] == 25:
                total -= 400
            elif board[i] == 14:
                total += 90
            elif board[i] == 24:
                total -= 90
            elif board[i] == 13:
                total += 50
            elif board[i] == 23:
                total -= 50
            elif board[i] == 12:
                total += 30
            elif board[i] == 22:
                total -= 30
            elif board[i] == 11:
                total += 30
            elif board[i] == 21:
                total -= 30
            elif board[i] == 10:
                total += 10
            elif board[i] == 20:
                total -= 10
        return total

    def countMoves(self,board):
        num = 0
        for i in range(64):
            if board[i] != 0:
                moves = getPieceLegalMoves(board,i)
                if (board[i] - 20) >= 0:
                    num -= 0.5 * len(moves)
                else:
                    num += 0.5 * len(moves)
        return num
    
    def gameStatus(self,board):
        total = 0
        if isInCheck(board,10):
            total -= 30
        if isInCheck(board,20):
            total += 30
        if isCheckmate(board,10):
            total -= 550
        if isCheckmate(board,20):
            total += 550

        return total

    def evalBoard(self,board):
        return (self.material(board) + self.countMoves(board) + self.gameStatus(board))

    def genFutureStates(self,player,stateNode,maxDepth):
        
        self.futureHelp(player,stateNode,maxDepth,0,time())
        return True
    
    def futureHelp(self,player,stateNode,maxDepth,currentDepth,begin):
        if (time() - begin) > 5:
            currentDepth = maxDepth
            print("Time limit reached")
        if currentDepth == maxDepth:
            return True
        board = stateNode.state['board']
        currentDepth += 1
        opp = 20
        if player == 20:
            opp = 10
        playerPos = getPlayerPositions(board,player)
        for pos in playerPos:
            playerMoves = getPieceLegalMoves(board,pos)
            for mov in playerMoves:
                tmpState = list(board)
                tmpState[mov], tmpState[pos] = tmpState[pos], 0
                nextState = gameTree(board=tmpState,pts=0,maxDepth=maxDepth-1,src=pos,dst=mov)
                nextState.state['eval'] = nextState.evalBoard(nextState.state['board'])
                (stateNode.potentMoves).append([[pos,mov],nextState.state['eval']])
                (stateNode.children).append(nextState)
                self.futureHelp(opp,nextState,maxDepth,currentDepth,begin)
        return True
    
    def getFutureStates(self):
        return self.children
    
    def getPotentMoves(self):
        return self.potentMoves

    def getState(self):
        return self.state 

