import numpy as np

def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1


def genBoard():
   r=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63

      r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
      r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
      r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*3] = i+getPiece("king")
      else:
         r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*4] = i+getPiece("king")

      for j in range(0,8):
         r[shift+factor*(j+8)] = i+getPiece("pawn")

   return r


def printBoard(board):
   accum="       ---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"       ---- WHITE SIDE ----   "
   print(accum)   
#    return accum

def printPositions():
    accum="       ---- BLACK SIDE ----\n"
    max=63
    for j in range(8,0,-1):
        # for i in range(max - j*8,max-j*8-8,-1):
        for i in range(1,9,1):
            accum=accum+'{0: <5}'.format(j*8 - i)
        accum=accum+"\n"
    accum=accum+"       ---- WHITE SIDE ----   "


def getPlayerPositions(board,player):
   #If the player isn't white or black it's invalid
   if ((player !=10) and (player != 20)):
      return False
   #White
   if player == 10:
      i = 0
      accum = []
      while i<len(board):
         for k in range(10,16,1):
            if (board[i] == k):
               accum += [i]
         i += 1
      return accum
   #Black
   if player == 20:
      p = 0
      accum = []
      while p<len(board):
         for s in range(20,26,1):
            if (board[p] == s):
               accum += [p]
         p += 1

      return accum

def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1

def isEmpty(board,position):
    val = True
    if board[position] != 0:
        val = False
    return val

def isOnTeam(board,player,position):
    opp = "20"
    if player == 20:
        opp = "10"
    
    check = str(board[position])
    if check[0] == opp[0] or board[position] == 0:
        return False
    return True


def getPawnMoves(board,player,position):
    factor = 1
    opp = 20
    if player == 20:
        factor = -1
        opp = 10

    pawn = getPiece("pawn")
    rval = []
    
    if isEmpty(board,position + factor*8):
        rval.append(position + factor*8)            
    if ((position>=8 and position<=15) or (position>=48 and position<=55)) and (isEmpty(board,position + factor*16) and isEmpty(board, position + factor*8)):
        rval.append(position + factor*16)

    # check eat moves
    if player == 10:
        if position % 8 == 0 and (not isOnTeam(board,player,position + 9)):
            rval.append(position + 9)
        if position % 8 == 7 and (not isOnTeam(board,player,position + 7)):
            rval.append(position + 7)
    
    if player == 20:
        if position % 8 == 0 and (not isOnTeam(board,player,position - 7)):
            rval.append(position - 7)
        if position % 8 == 7 and (not isOnTeam(board,player,position - 9)):
            rval.append(position - 9)
    
    if (position % 8 != 0) and (position % 8 != 7):
        if (not isOnTeam(board,player,position + factor*9)):
            rval.append(position + factor*9)
        if (not isOnTeam(board,player,position + factor*7)):
            rval.append(position + factor*7)

    return sorted(rval)


def getBishopMoves(board,player,position):
    factor = 1
    opp = 20
    if player == 20:
        factor = -1
        opp = 10

    # get moves (before filtering vacancies)
    rval = []
    for i in range(position+9,64,9):
        if not isEmpty(board,i):
            if not isOnTeam(board,player,i):
                rval.append(i)
                break
            break
        else:
            rval.append(i)

    for j in range(position-9,0,-9):
        if not isEmpty(board,j):
            if not isOnTeam(board,player,j):
                rval.append(j)
                break
            break
        else:
            rval.append(j)

    for k in range(position-7,0,-7):
        if not isEmpty(board,k):
            if not isOnTeam(board,player,k):
                rval.append(k)
                break
            break
        else:
            rval.append(k)
    
    for h in range(position+7,64,+7):
        print(h)
        if not isEmpty(board,h):
            if not isOnTeam(board,player,h):
                rval.append(h)
                break
            break
        else:
            rval.append(h)
    

def getKnightMoves(board,player,position):

    rval = []
    for i in range(position-17,position+18,1):
        dist = (position - i)

        if i < 0 or i > 63 or i == position:
            continue

        diff = [17,15,10,6]
        if position % 8 >= 2 and position % 8 <= 5:
            if abs(dist) in diff and (not isOnTeam(board,player,i)):
                rval.append(i)
        
        elif position % 8 == 1:
            if dist == -6 or dist == 10:
                continue
            elif abs(dist) in diff and (not isOnTeam(board,player,i)):
                rval.append(i)
        
        elif position % 8 == 0:
            if dist == -6 or dist == 10 or dist == 17 or dist == -15:
                continue
            elif abs(dist) in diff and (not isOnTeam(board,player,i)):
                rval.append(i)
        
        elif position % 8 == 6:
            if dist == 6 or dist == -10:
                continue
            elif abs(dist) in diff and (not isOnTeam(board,player,i)):
                rval.append(i)
        
        elif position % 8 == 7:
            if dist == 6 or dist == -10 or dist == -17 or dist == 15:
                continue
            elif abs(dist) in diff and (not isOnTeam(board,player,i)):
                rval.append(i)           

    return sorted(rval)


def alongDir(board,player,position,direction):
    opp = '2'
    if player == 20:
        opp = '1'
    factor = 1
    rval = []
    done = False
    while not done:
        # check if off board
        if position + direction*factor < 0 or position + direction*factor > 63:
            done = True
            # break
        elif isOnTeam(board,player,position + direction*factor):
            # print(isOnTeam(board,player))
            done = True
        
        elif str(board[position + direction*factor])[0] == opp:
            # print(str(position+ direction*factor)[0])
            rval.append(position + direction*factor)
            done = True
        elif (position + direction*factor) % 8 == 7 or (position + direction*factor) % 8 == 0:
            rval.append(position + direction*factor)
            done = True
            # break
        else:
            rval.append(position + direction*factor)
            factor += 1
    return rval

def getBishopMoves(board,player,position):

   
    rval = []
    rval += alongDir(board,player,position,-7)
    rval += alongDir(board,player,position,7)
    rval += alongDir(board,player,position,-9)
    rval += alongDir(board,player,position,9)
    


    return sorted(rval)

def getRookMoves(board,player,position):
    rval = []
    rval += alongDir(board,player,position,-8)
    rval += alongDir(board,player,position,8)
    rval += alongDir(board,player,position,-1)
    rval += alongDir(board,player,position,1)
    
    return sorted(rval)

def getQueenMoves(board,player,position):
    rval = getRookMoves(board,player,position) + getBishopMoves(board,player,position)
    
    return sorted(rval)

def getKingMoves(board,player,position):
    rval = []
    bishop = getBishopMoves(board,player,position)
    rook = getRookMoves(board,player,position)
    accum1 = bishop + rook
    for i in accum1:
        if (abs(position - i) == 9) or (abs(position - i) == 8) or (abs(position - i) == 7) or (abs(position - i) == 1):
            rval += [i]
    return sorted(rval)

def getPlayerPositions(board,player):
    team = str(player)[0]
    rval = []
    for i in range(64):
        if str(board[i])[0] == team:
            rval.append(i)
    return rval

def identifyPiece(board,position):
    piece = int(str(board[position])[1])
    if piece == 0:
        return "Pawn"
    if piece == 1:
        return "Knight"
    if piece == 2:
        return "Bishop"
    if piece == 3:
        return "Rook"
    if piece == 4:
        return "Queen"
    if piece == 5:
        return "King"


def getPieceLegalMoves(board,position):
    player = int(str(board[position])[0] + '0')
    
    piece = int(str(board[position])[1])
    rval = []
    if piece == 0:
        rval += getPawnMoves(board,player,position)
    elif piece == 1:
        rval += getKnightMoves(board,player,position)
    elif piece == 2:
        rval += getBishopMoves(board,player,position)
    elif piece == 3:
        rval += getRookMoves(board,player,position)
    elif piece == 4:
        rval += getQueenMoves(board,player,position)
    elif piece == 5:
        rval += getKingMoves(board,player,position)

    return rval

def isPositionUnderThreat(board,player,position):
    opp = 20
    if player == 20:
        opp = 10
    
    oppLocs = getPlayerPositions(board,opp)
    for p in oppLocs:
        tmp = getPieceLegalMoves(board,p)
        if position in tmp:
            return True

    return False 


def isInCheck(board,player):
    for i in range(64):
        if (board[i] - player) == 5:
            check = isPositionUnderThreat(board,player,i)
            return check
    return False

def isCheckmate(board,player):
    for i in range(64):
        if (board[i] - player) == 5:
            check = isPositionUnderThreat(board,player,i)
            if check:
                moves = getPieceLegalMoves(board,i)
                for m in moves:
                    tmp = list(board)
                    tmp[m] = tmp[i]
                    tmp[i] = 0
                    newCheck = isPositionUnderThreat(board,player,m)
                    if not newCheck:
                        return False
                return True
    return False
