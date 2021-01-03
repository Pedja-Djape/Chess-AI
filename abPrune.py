from chesslib import *
from gt import gameTree


class abPrune:
    def __init__(self,gt):
        self.gt = gt 
        self.children = gt.getFutureStates
    
    def abGen(self,stateNode,player):
        inf = float("inf")
        top = -inf
        beta = inf 
        childs = self.getChildren(stateNode)
        topState = None
        for kid in childs:
            value = self.minPlayer(stateNode,top,beta)
            if value > top:
                top = value
                topState = kid
        return topState



    def minPlayer(self,stateNode,alpha,beta):
        if self.isLeaf(stateNode):
            return self.getStatePts(stateNode)
        inf = float('inf')
        value = inf
        childs = self.getChildren(stateNode)
        for kid in childs:
            value = min(value,self.minPlayer(kid,alpha,beta))
            if value <= beta:
                return value
            alpha = min(value,alpha)
        return value

    def maxPLayer(self,stateNode,alpha,beta):
        if self.isLeaf(stateNode):
            return self.getStatePts(stateNode)
        inf = float('inf')
        value = -inf
        childs = self.getChildren(stateNode)
        for kid in childs:
            value = max(value,self.minPlayer(kid,alpha,beta))
            if value >= beta:
               return beta
            alpha = max(value,alpha)
        return value

    def getStatePts(self,stateNode):
        return stateNode.state['eval']

    def isLeaf(self,stateNode):
        if len(stateNode.getFutureStates()) == 0:
            return True
        return False
    
    def getChildren(self,stateNode):
        if stateNode != None:
            return stateNode.getFutureStates() 

