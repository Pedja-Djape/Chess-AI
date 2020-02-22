from chessPlayer_queue import *
from chessPlayer_helperChess import *

class tree:

   def __init__(self,x):
      self.store = [x,[]]

   def AddSuccessor(self,x):
      self.store[1] = self.store[1] + [x]
      return True

   def Print_DepthFirst(self):
      return self.depth_help("")

   def depth_help(self,indent):
      print(str(indent)+str(self.store[0]))
      for e in self.store[1]:
          i = indent + "   "
          e.depth_help(i)
      return True

   def Get_LevelOrder(self):
      tree = queue()
      tree.add(self.store)
      rval = []
      while True:
         liste = tree.disc()
         if (liste != False):
            rval += [liste[0]]
            for i in liste[1]:
               tree.add(i.store)
         else:
            break
      return rval
