from chesslib import *
from gt import *
from abPrune import *
from random import randint

def chessAI(board,player):

    gt = gameTree(board,0,3,None,None)
    gt.genFutureStates(player,gt)

    alphaBeta = abPrune(gt)
    top = alphaBeta.abGen(alphaBeta.gt,player)
    # if there is no proper evaluation of a top move, choose randomly
    if top == None:
        tmpMov = []
        positions = getPlayerPositions(board,player)
        for pos in positions:
            movs = getPieceLegalMoves(board,pos)
            if len(movs) != 0:
                for m in movs:
                    threat = isPositionUnderThreat(board,player,m)
                    if not threat:
                        tmpMov.append([pos,m])
        idx = randint(0,len(tmpMov)-1)
        move = tmpMov[idx]
        potentMoves = getPieceLegalMoves(board,move[0])
        return [move,potentMoves]
    else:
        return [top.getTopMove(),top.getPotentMoves()]

