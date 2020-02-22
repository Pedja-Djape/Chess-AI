
def bubbleSort_asc(array):
   n = len(array)
   L = list(array)
   swap = True
   while swap:
      swap = False
      for i in range(n-1):
         if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]

            swap = True
   return L

def filter(L,val):
   M = list(L)
   acc = []
   for i in M:
      if i!=val:
         acc += [i]
   return acc

def myabs(x):
   if x>=0:
      return x
   else:
      return -x

def bubbleSort_des(array):
   n = len(array)
   L = list(array)
   swap = True
   while swap:
      swap = False
      for i in range(n-1):
         if L[i] < L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]
            swap = True
   return L

def didFallOff(position):
   if (position > 63) or (position < 0):
      return True
   else:
      return False

def isOnTeam(board,pos,team):
   #team: 0 = White
   #      1 = Black
   #occupant of Position
   occ = board[pos]
   if occ == 0:
      return [False,0]
   #White
   if team == 0:
      if (occ-10 == 0) or (occ-10 == 1) or (occ-10 == 2) or (occ-10 == 3) or (occ-10 == 4) or (occ-10 == 5):
         return [True,-1]
      else:
         return [False,1]
   #Black
   if team == 1:
      if (occ-20 == 0) or (occ-20 == 1) or (occ-20 == 2) or (occ-20 == 3) or (occ-20 == 4) or (occ-20 == 5):
         return [True,-1]
      else:
         return [False,1]

def isEmpty(L):
   if len(L) == 0:
      return True
   else:
      return False



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
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum

def GetPlayerPositions(board,player):
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



def GetPieceLegalMoves(board,position):

   if (position >63 or position <0):
      return -1
   accum = []
   w= 0
   b =1

   #PAWN CASES
   piece = board[position]
   #WHITE
   if (piece == 10):

      rw1 = getPawnMoves(board,position)
      if len(rw1)>0:
         for i in rw1:
            if (isOnTeam(board,i,0))[1] == 0:
               accum += [i]
      #Handle the cases where there's an an opponent on the diag left/right for all rows
      rw2 = getPawnAttack(board,position)
      if len(rw2) > 0:
         for i in rw2:
            if (isOnTeam(board,i,0))[0] == False:
               accum += [i]
      rval1 = []

      rval1 = list(set(accum))
      rval = []
      for i in rval1:
         if (i == position+8) or (i == position +16):
            rval += [i]

      if isEmpty(rval) == True:
         return False
      else:
         return list(set(rval))

   #Black
   elif (piece == 20):
      rb1 = getPawnMoves(board,position)
      if len(rb1) > 0:
         for i in rb1:
            if (isOnTeam(board,i,1))[1] == 0:
               accum += [i]
      #Handle Cases where there's an opponent on the diag left/right for all rows
      rb2 = getPawnAttack(board,position)
      if len(rb2)>0:
         for i in rb2:
            if (isOnTeam(board,i,1))[0] == False:
               accum += [i]
      rval1 = []
      rval1 = list(set(accum))
      rval =[]

      for i in rval1:
         if (i == position-8) or (i == position - 16):
            rval += [i]
      if isEmpty(rval) == True:
         return False
      else:
         return list(set((rval)))


   #BISHOP
   #White
   elif piece == 12:
      rw2 = getBishopMoves(board,position,w)
      if isEmpty(rw2) == True:
         return False
      else:
         accum = rw2
         return accum
   #Black
   elif piece == 22:
      rb2 = getBishopMoves(board,position,b)
      if isEmpty(rb2) == True:
         return False
      else:
         accum = rb2
         return accum
   #ROOK
   #White
   elif piece == 13:
      rw3 = getRookMoves(board,position,w)
      if isEmpty(rw3) == True:
         return False
      else:
         accum = rw3
         return accum
   #Black
   elif piece == 23:
      rb3 = getRookMoves(board,position,b)
      if isEmpty(rb3) == True:
         return False
      else:
         accum = rb3
         return accum
   #QUEEN
   #White
   elif piece == 14:
      rw4 = getQueenMoves(board,position,w)
      if isEmpty(rw4) == True:
         return False
      else:
         accum = rw4
         return accum
   #Black
   elif piece == 24:
      rb4 = getQueenMoves(board,position,b)
      if isEmpty(rb4) == True:
         return False
      else:
         accum = rb4
         return accum
   #KING
   #White
   elif piece == 15:
      rw5 = getKingMoves(board,position,w)
      if isEmpty(rw5) == True:
         return False
      else:
         accum = rw5
         return accum
   #Black
   elif piece == 25:
      rb5 = getKingMoves(board,position,b)
      if isEmpty(rb5) == True:
         return False
      else:
         accum = rb5
         return accum

   #KNIGHT
   #White
   elif piece == 11:
      rw6 = getKnightMoves(board,position,w)
      if isEmpty(rw6) == True:
         return False
      else:
         for i in rw6:
            if isOnTeam(board,i,0)[0] == False:
               accum +=[i]
         return accum
   #Black
   elif piece == 21:
      rb6 = getKnightMoves(board,position,w)
      if isEmpty(rb6) == True:
         return False
      else:
         for i in rb6:
            if isOnTeam(board,i,1)[0] == False:
               accum +=[i]
         return accum

   elif piece == 0:
      return False



def getPawnMoves(board,position):
   #WHITE
   if (board[position] == 10):
      accum = []
      #Address the first move of a pawn where they can either move 1 or
      # spaces
      if (position<=15 and position>=8):
         np = 0
         if board[position+8] !=0:
            accum = []
         else:
            for i in range(position+8,position+17,1):
               np = i - position
               if (np % 8 == 0):
                  for j in range(20,26,1):
                     if (board[i] != j):
                        accum += [i]

      #All other moves (without capturing)
      elif (position>15 and position<56):
         for x in range(20,26,1):
            if board[position+8] != x:
               accum += [position+8]
      if board[position+8] !=0:
         s1 = filter(accum,position+8)
         s2 = filter(accum,position+16)
         accum = list(set(s1+s2))

      return accum

   #BLACK
   elif board[position] == 20:
      accum = []
      #Address the first move of a pawn where they can either move 1 or
      # 2 spaces
      if (position<=55 and position>=48):
         if board[position-8] != 0:
            accum = []
         else:
            np = 0
            for i in range(position-16,position-7,1):
               np = i - position
               if (np % 8 == 0):
                  for j in range(20,26,1):
                     if board[i] != j:
                        accum += [i]

      #All other moves (without capturing)
      elif (position<48 and position>7):
         for b in range(10,16,1):
            if board[position-8] != b:
               accum += [position-8]

      if (board[position-8]) !=0:
         s1 = filter(accum,position-8)
         s2 = filter(accum,position-16)
         accum = list(set(s1+s2))


      return accum

def getPawnAttack(board,position):
   #White Team
   if board[position] == 10:
      accum = []
      #RightDiag
      opp1 = position+7
      #LeftDiag
      opp2 = position+9
   #row 1
      if (position<15 and position > 8):
         for i in range(20,26,1):
            if board[opp1] == i:
               accum += [opp1]
            if board[opp2] == i:
               accum += [opp2]


   #Row2
      elif (position<23 and position>16):
         for i in range(20,26,1):
            if board[opp1] == i:
               accum += [opp1]
            if board[opp2] == i:
               accum += [opp2]
   #Row3
      elif (position<31 and position>24):
         for i in range(20,26,1):
            if board[opp1] == i:
               accum += [opp1]
            if board[opp2] == i:
               accum += [opp2]

   #Row4
      elif (position<39 and position>32):
         for i in range(20,26,1):
            if board[opp1] == i:
               accum += [opp1]
            if board[opp2] == i:
               accum += [opp2]
   #Row5
      elif (position<47 and position>40):
         for i in range(20,26,1):
            if board[opp1] == i:
               accum += [opp1]
            if board[opp2] == i:
               accum += [opp2]
   #Row6
      elif (position<55 and position>48):
         for i in range(20,26,1):
            if board[opp1] == i:
               accum += [opp1]
            if board[opp2] == i:
               accum += [opp2]
   #Vertical Ends
      for i in range(8,49,8):
         if (position == i):
            for q in range(20,26,1):
               if board[opp2] == q:
                  accum += [opp2]
      for e in range(15,56,1):
         if (position ==e):
            for y in range(20,26,1):
               if board[opp1] == y:
                  accum += [opp1]
      return accum




   #BLACK
   if board[position] == 20:
      accum = []
      #RightDiag
      opp3 = position - 9
      #LeftDiag
      opp4 = position - 7
      #row 1
      if (position<15 and position > 8):
         for i in range(10,16,1):
            if board[opp3] == i:
               accum += [opp3]
            if board[opp4] == i:
               accum += [opp4]

      #Row2
      elif (position<23 and position>16):
         for i in range(10,16,1):
            if board[opp3] == i:
               accum += [opp3]
            if board[opp4] == i:
               accum += [opp4]
      #Row3
      elif (position<31 and position>24):
         for i in range(10,16,1):
            if board[opp3] == i:
               accum += [opp3]
            if board[opp4] == i:
               accum += [opp4]

      #Row4
      elif (position<39 and position>32):
         for i in range(10,16,1):
            if board[opp3] == i:
               accum += [opp3]
            if board[opp3] == i:
               accum += [opp3]
      #Row5
      elif (position<47 and position>40):
         for i in range(10,16,1):
            if board[opp3] == i:
               accum += [opp3]
            if board[opp4] == i:
               accum += [opp4]
      #Row6
      elif (position<55 and position>48):
         for i in range(10,16,1):
            if board[opp3] == i:
               accum += [opp3]
            if board[opp4] == i:
               accum += [opp4]
      #Vertical Ends
      for i in range(8,49,8):
          if (position == i):
             for q in range(10,16,1):
                if board[opp4] == q:
                   accum += [opp4]
      for e in range(15,56,1):
         if (position ==e):
            for y in range(10,16,1):
               if board[opp3] == y:
                  accum += [opp3]
      return accum


def getBishopMoves(board,position,team):

   #Moves Diagonally and cannot go over teammates
   #bigF
   f = position % 8
   #bigG
   g = 7 - (position %8)
   #TopLeft
   opp1 = position
   #TopRight
   opp2 = position
   #BottomLeft
   opp3 = position
   #BottomRight
   opp4 = position
   accum1 = []
   accum2 = []
   accum3 = []
   accum4 = []
   acc1 = []
   acc2 = []
   acc3 = []
   acc4 = []
   accum = []
   a1 = []
   a2 = []
   a3 = []
   a4 = []

   for i in range(0,f,1):
      opp2 += 7
      opp4 -=9
      if didFallOff(opp2) == False:
         accum1 += [opp2]
         a1 = bubbleSort_asc(accum1)
      if didFallOff(opp4) == False:
         accum2 += [opp4]
         a2 = bubbleSort_des(accum2)
   for i in range(0,g,1):
      opp1 +=9
      opp3 -=7
      if didFallOff(opp1) == False:
         accum3 += [opp1]
      a3 = bubbleSort_asc(accum3)
      if didFallOff(opp3) == False:
         accum4 += [opp3]
      a4 = bubbleSort_des(accum4)

   if (team == 0) or (team == 1):
      #Upper Right Diagonal
      if len(a1)>0:
         ind_fed = []
         ind_team = []
         ind_0 = []
         for i in a1:
            if isOnTeam(board,i,team)[1] == 1:
               ind_fed+=[i]
         for i in a1:
            if isOnTeam(board,i,team)[1] == -1:
               ind_team +=[i]
         for i in a1:
            if isOnTeam(board,i,1)[1] == 0:
               ind_0 += [i]
         if isEmpty(ind_team) == False and isEmpty(ind_fed) == False:
            if ind_team[0] < ind_fed[0]:
               up_to = ind_team[0]
               for i in a1:
                  if i < up_to:
                     acc1 += [i]
            elif ind_fed[0] < ind_team[0]:
               up_to = ind_fed[0]
               for i in a1:
                  if i <= up_to:
                     acc1 += [i]
         elif (isEmpty(ind_fed) == True) and (isEmpty(ind_team) == False):
            up_to = ind_team[0]
            for i in a1:
               if i < up_to:
                  acc1 +=[i]
         elif (isEmpty(ind_team) == True) and (isEmpty(ind_fed) == False):
            up_to = ind_fed[0]
            for i in a1:
               if i <= up_to:
                  acc1 +=[i]
         elif ((isEmpty(ind_team) == True) and (isEmpty(ind_fed) == True)):
            acc1+= ind_0
         accum+=acc1
      #Upper Left Diagonal
      if len(a3)>0:

         ind_fed = []
         ind_team = []
         ind_0 = []
         for i in a3:
            if isOnTeam(board,i,team)[1] == 1:
               ind_fed+=[i]
         for i in a3:
            if isOnTeam(board,i,team)[1] == -1:
               ind_team +=[i]
         for i in a3:
            if isOnTeam(board,i,team)[1] == 0:
               ind_0 += [i]
         if isEmpty(ind_team) == False and isEmpty(ind_fed) == False:
            if ind_team[0] < ind_fed[0]:
               up_to = ind_team[0]
               for i in a3:
                  if i < up_to:
                     acc3 += [i]
            elif ind_fed[0] < ind_team[0]:
               up_to = ind_fed[0]
               for i in a3:
                  if i <= up_to:
                     acc3 += [i]
         elif (isEmpty(ind_fed) == True) and (isEmpty(ind_team) == False):
            up_to = ind_team[0]
            for i in a3:
               if i < up_to:
                  acc3 +=[i]
         elif (isEmpty(ind_team) == True) and (isEmpty(ind_fed) == False):
            up_to = ind_fed[0]
            for i in a3:
               if i <= up_to:
                  acc3 +=[i]
         elif ((isEmpty(ind_team) == True) and (isEmpty(ind_fed) == True)):
            acc3+= ind_0
         accum += acc3
      #Bottom Left Diagonal
      if len(a4) >0:
         ind_fed = []
         ind_team = []
         ind_0 = []
         for i in a4:
            if isOnTeam(board,i,team)[1] == 1:
               ind_fed+=[i]
         for i in a4:
            if isOnTeam(board,i,team)[1] == -1:
               ind_team +=[i]
         for i in a4:
            if isOnTeam(board,i,team)[1] == 0:
               ind_0 += [i]
         if isEmpty(ind_team) == False and isEmpty(ind_fed) == False:
            if ind_team[0] > ind_fed[0]:
               up_to = ind_team[0]
               for i in a4:
                  if i > up_to:
                     acc4 += [i]
            elif ind_fed[0] > ind_team[0]:
               up_to = ind_fed[0]
               for i in a4:
                  if i >= up_to:
                     acc4 += [i]
         elif (isEmpty(ind_fed) == True) and (isEmpty(ind_team) == False):
            up_to = ind_team[0]
            for i in a4:
               if i > up_to:
                  acc4 +=[i]
         elif (isEmpty(ind_team) == True) and (isEmpty(ind_fed) == False):
            up_to = ind_fed[0]
            for i in a4:
               if i >= up_to:
                  acc4 +=[i]
         elif ((isEmpty(ind_team) == True) and (isEmpty(ind_fed) == True)):
            acc4+= ind_0

         accum += acc4
      #Bottom Right Diagonal
      if len(a2) > 0:
         ind_fed = []
         ind_team = []
         ind_0 = []
         for i in a2:
            if isOnTeam(board,i,team)[1] == 1:
               ind_fed+=[i]
         for i in a2:
            if (isOnTeam(board,i,team))[1] == -1:
               ind_team +=[i]
         for i in a2:
            if isOnTeam(board,i,team)[1] == 0:
               ind_0 += [i]
         if isEmpty(ind_team) == False and isEmpty(ind_fed) == False:
            if ind_team[0] > ind_fed[0]:
               up_to = ind_team[0]
               for i in a2:
                  if i > up_to:
                     acc2 += [i]
            elif ind_fed[0] > ind_team[0]:
               up_to = ind_fed[0]
               for i in a2:
                  if i >= up_to:
                     acc2 += [i]
         elif (isEmpty(ind_fed) == True) and (isEmpty(ind_team) == False):
            up_to = ind_team[0]
            for i in a2:
               if i > up_to:
                  acc2 +=[i]
         elif (isEmpty(ind_team) == True) and (isEmpty(ind_fed) == False):
            up_to = ind_fed[0]
            for i in a2:
               if i >= up_to:
                  acc2 +=[i]
         elif ((isEmpty(ind_team) == True) and (isEmpty(ind_fed) == True)):
            acc2+= ind_0
         accum += acc2
      rval = []
      rval = bubbleSort_asc(accum)
      return rval



def getKnightMoves(board,position,team):
   col_rr = position - 2
   col_r = position - 1
   col_l = position + 1
   col_ll = position + 2
   #NextDown
   d_prr = col_rr // 8
   d_pr = col_r // 8
   d_pl = col_l // 8
   d_pll = col_ll // 8
   #NextUp
   u_prr = 7 - (col_rr // 8)
   u_pr = 7 - (col_r // 8)
   u_pl = 7 - (col_l // 8)
   u_pll = 7 - (col_ll // 8)

   #Down
   opp3 = position -2
   #Up
   opp4 = position -2
   opp5 = position -1
   opp6 = position -1
   opp7 = position +1
   opp8 = position +1
   opp9 = position + 2
   opp10 = position +2


   accum1 = []
   accum2 = []
   accum3 = []
   accum4 = []
   accum5 = []
   accum6 = []
   accum7 = []
   accum8 = []
   #a3 = Down
   #a4 = up  .
   a3a = []
   a4a = []
   a3b = []
   a4b = []
   a3c = []
   a4c = []
   a3d = []
   a4d = []
   #concats of a3 and a4
   a5a = []
   a5b = []
   a5c = []
   a5d = []
   #lists to be summed and then returned
   rlista = []
   rlistb = []
   rlistc = []
   rlistd = []
   #ret list
   accum = []

   #Where all Knight Positions could be open
   if (position >17) and (position < 46):
      if (position % 8 >= 2) and (position % 8 <= 5):
         #2 cols right (a)
         for j in range(0,d_prr,1):
            opp3 -= 8
            if didFallOff(opp3) == False:
               accum1 += [opp3]
         a3a = bubbleSort_des(accum1)
         for k in range(0,u_prr,1):
            opp4 += 8
            if didFallOff(opp4) == False:
               accum2 += [opp4]
         a4a = bubbleSort_asc(accum2)
         a5a = a3a + a4a
         for i in a5a:
            if ((myabs(position - i)) == 10) or ((myabs(position -i)) == 6):
               rlista += [i]



         #1 col right (b)

         for j in range(0,d_pr,1):
            opp5 -= 8
            if didFallOff(opp5) == False:
               accum3 += [opp5]
            a3b = bubbleSort_des(accum3)
         for k in range(0,u_pr,1):
            opp6 += 8
            if didFallOff(opp6) == False:
               accum4 += [opp6]
            a4b = bubbleSort_asc(accum4)
         a5b = a3b + a4b
         for i in a5b:
            if ((myabs(position - i)) == 17) or ((myabs(position -i)) == 15):
               rlistb += [i]

         #1 col left (c)
         for j in range(0,d_pl,1):
            opp7 -= 8
            if didFallOff(opp7) == False:
               accum5 += [opp7]
            a3c = bubbleSort_des(accum5)
         for k in range(0,u_pl,1):
            opp8 += 8
            if didFallOff(opp8) == False:
               accum6 += [opp8]
            a4c = bubbleSort_asc(accum6)
         a5c = a3c + a4c
         for i in a5c:
            if ((myabs(position - i)) == 17) or ((myabs(position -i)) == 15):
               rlistc += [i]

         #2 col left (d)
         for j in range(0,d_pll,1):
            opp9 -= 8
            if didFallOff(opp9) == False:
               accum7 += [opp9]
            a3d = bubbleSort_des(accum7)
         for k in range(0,u_pll,1):
            opp10 += 8
            if didFallOff(opp10) == False:
               accum8 += [opp10]
            a4d = bubbleSort_asc(accum8)
         a5d = a3d + a4d
         for i in a5d:
            if ((myabs(position - i)) == 10) or ((myabs(position -i)) == 6):
               rlistd += [i]
         accum = bubbleSort_asc(rlista + rlistb + rlistc + rlistd)

   #Check Right End
   #Very Right
   if (position % 8 == 0):
      #1 col left (c)
      for j in range(0,d_pl,1):
         opp7 -= 8
         if didFallOff(opp7) == False:
            accum5 += [opp7]
         a3c = bubbleSort_des(accum5)
      for k in range(0,u_pl,1):
         opp8 += 8
         if didFallOff(opp8) == False:
            accum6 += [opp8]
         a4c = bubbleSort_asc(accum6)
      a5c = a3c + a4c
      for i in a5c:
         if ((myabs(position - i)) == 17) or ((myabs(position -i)) == 15):
            rlistc += [i]

      #2 col left (d)
      for j in range(0,d_pll,1):
         opp9 -= 8
         if didFallOff(opp9) == False:
            accum7 += [opp9]
         a3d = bubbleSort_des(accum7)
      for k in range(0,u_pll,1):
         opp10 += 8
         if didFallOff(opp10) == False:
            accum8 += [opp10]
         a4d = bubbleSort_asc(accum8)
      a5d = a3d + a4d
      for i in a5d:
         if ((myabs(position - i)) == 10) or ((myabs(position -i)) == 6):
            rlistd += [i]
      accum = bubbleSort_asc(rlistc + rlistd)
   #Check almost Right
   if (position % 8 == 1):
      #1 col right
      for j in range(0,d_pr,1):
         opp5 -= 8
         if didFallOff(opp5) == False:
            accum3 += [opp5]
         a3b = bubbleSort_des(accum3)
      for k in range(0,u_pr,1):
         opp6 += 8
         if didFallOff(opp6) == False:
            accum4 += [opp6]
         a4b = bubbleSort_asc(accum4)
      a5b = a3b + a4b
      for i in a5b:
         if ((myabs(position - i)) == 17) or ((myabs(position -i)) == 15):
            rlistb += [i]

      #1 col left (c)
      for j in range(0,d_pl,1):
         opp7 -= 8
         if didFallOff(opp7) == False:
            accum5 += [opp7]
         a3c = bubbleSort_des(accum5)
      for k in range(0,u_pl,1):
         opp8 += 8
         if didFallOff(opp8) == False:
            accum6 += [opp8]
         a4c = bubbleSort_asc(accum6)
      a5c = a3c + a4c
      for i in a5c:
         if ((myabs(position - i)) == 17) or ((myabs(position -i)) == 15):
            rlistc += [i]

      #2 col left (d)
      for j in range(0,d_pll,1):
         opp9 -= 8
         if didFallOff(opp9) == False:
            accum7 += [opp9]
         a3d = bubbleSort_des(accum7)
      for k in range(0,u_pll,1):
         opp10 += 8
         if didFallOff(opp10) == False:
            accum8 += [opp10]
         a4d = bubbleSort_asc(accum8)
      a5d = a3d + a4d
      for i in a5d:
         if ((myabs(position - i)) == 10) or ((myabs(position -i)) == 6):
            rlistd += [i]
      accum = bubbleSort_asc(rlistb + rlistc + rlistd)

   #Check Left ends
   #Very Left
   if (position % 8 == 7):
      for j in range(0,d_prr,1):
         opp3 -= 8
         if didFallOff(opp3) == False:
            accum1 += [opp3]
      a3a = bubbleSort_des(accum1)
      for k in range(0,u_prr,1):
         opp4 += 8
         if didFallOff(opp4) == False:
            accum2 += [opp4]
      a4a = bubbleSort_asc(accum2)
      a5a = a3a + a4a
      for i in a5a:
         if ((myabs(position - i)) == 10) or ((myabs(position -i)) == 6):
            rlista += [i]



      #1 col right (b)

      for j in range(0,d_pr,1):
         opp5 -= 8
         if didFallOff(opp5) == False:
            accum3 += [opp5]
         a3b = bubbleSort_des(accum3)
      for k in range(0,u_pr,1):
         opp6 += 8
         if didFallOff(opp6) == False:
            accum4 += [opp6]
         a4b = bubbleSort_asc(accum4)
      a5b = a3b + a4b
      for i in a5b:
         if ((myabs(position - i)) == 17) or ((myabs(position -i)) == 15):
            rlistb += [i]
      accum = bubbleSort_asc(rlista + rlistb)
   #Check almost Left
   if (position % 8) == 6:
      for j in range(0,d_prr,1):
         opp3 -= 8
         if didFallOff(opp3) == False:
            accum1 += [opp3]
      a3a = bubbleSort_des(accum1)
      for k in range(0,u_prr,1):
         opp4 += 8
         if didFallOff(opp4) == False:
            accum2 += [opp4]
      a4a = bubbleSort_asc(accum2)
      a5a = a3a + a4a
      for i in a5a:
         if ((myabs(position - i)) == 10) or ((myabs(position -i)) == 6):
            rlista += [i]



      #1 col right (b)

      for j in range(0,d_pr,1):
         opp5 -= 8
         if didFallOff(opp5) == False:
            accum3 += [opp5]
         a3b = bubbleSort_des(accum3)
      for k in range(0,u_pr,1):
         opp6 += 8
         if didFallOff(opp6) == False:
            accum4 += [opp6]
         a4b = bubbleSort_asc(accum4)
      a5b = a3b + a4b
      for i in a5b:
         if ((myabs(position - i)) == 17) or ((myabs(position -i)) == 15):
            rlistb += [i]

      #1 col left (c)
      for j in range(0,d_pl,1):
         opp7 -= 8
         if didFallOff(opp7) == False:
            accum5 += [opp7]
         a3c = bubbleSort_des(accum5)
      for k in range(0,u_pl,1):
         opp8 += 8
         if didFallOff(opp8) == False:
            accum6 += [opp8]
         a4c = bubbleSort_asc(accum6)
      a5c = a3c + a4c
      for i in a5c:
         if ((myabs(position - i)) == 17) or ((myabs(position -i)) == 15):
            rlistc += [i]
      accum = bubbleSort_asc(rlista + rlistb + rlistc)

   return accum



def getRookMoves(board,position,team):
   #NextLeft
   l_p = position % 8
   #NextRIght
   r_p = 7 - (position % 8)
   #NextDown
   d_p = position // 8
   #NextUp
   u_p = 7 - (position // 8)
   accum=[]
   #Left
   opp1 = position
   #Right
   opp2 = position
   #Down
   opp3 = position
   #Up
   opp4 = position
   accum1 = []
   accum2 = []
   accum3 = []
   accum4 = []
   acc1 = []
   acc2 = []
   acc3 = []
   acc4 = []
   accum = []
   a1 = []
   a2 = []
   a3 = []
   a4 = []
   for i in range(0,l_p,1):
      opp1 -= 1
      if didFallOff(opp1) == False:
         accum1 += [opp1]
      a1 = bubbleSort_des(accum1)
   for m in range(0,r_p,1):
      opp2 += 1
      if didFallOff(opp2) == False:
         accum2 += [opp2]
      a2 = bubbleSort_asc(accum2)
   for j in range(0,d_p,1):
      opp3 -= 8
      if didFallOff(opp3) == False:
         accum3 += [opp3]
   a3 = bubbleSort_des(accum3)
   for k in range(0,u_p,1):
      opp4 += 8
      if didFallOff(opp4) == False:
         accum4 += [opp4]
   a4 = bubbleSort_asc(accum4)

   #a1 = Right
   #a2 = Left .
   #a3 = Down
   #a4 = up  .
   if (team == 0) or (team == 1):
      #Left
      if len(a2) > 0:

         ind_fed = []
         ind_team = []
         ind_0 = []
         for i in a2:
            if isOnTeam(board,i,team)[1] == 1:
               ind_fed+=[i]
         for i in a2:
            if isOnTeam(board,i,team)[1] == -1:
               ind_team +=[i]
         for i in a2:
            if isOnTeam(board,i,1)[1] == 0:
               ind_0 += [i]
         if isEmpty(ind_team) == False and isEmpty(ind_fed) == False:
            if ind_team[0] < ind_fed[0]:
               up_to = ind_team[0]
               for i in a2:
                  if i < up_to:
                     acc2 += [i]
            elif ind_fed[0] < ind_team[0]:
               up_to = ind_fed[0]
               for i in a2:
                  if i <= up_to:
                     acc2 += [i]
         elif (isEmpty(ind_fed) == True) and (isEmpty(ind_team) == False):
            up_to = ind_team[0]
            for i in a2:
               if i < up_to:
                  acc2 +=[i]
         elif (isEmpty(ind_team) == True) and (isEmpty(ind_fed) == False):
            up_to = ind_fed[0]
            for i in a2:
               if i <= up_to:
                  acc2 +=[i]
         elif ((isEmpty(ind_team) == True) and (isEmpty(ind_fed) == True)):
            acc2+= ind_0


         accum+=acc2
      #Up
      if len(a4)>0:

         ind_fed = []
         ind_team = []
         ind_0 = []
         for i in a4:
            if isOnTeam(board,i,team)[1] == 1:
               ind_fed+=[i]
         for i in a4:
            if isOnTeam(board,i,team)[1] == -1:
               ind_team +=[i]
         for i in a4:
            if isOnTeam(board,i,team)[1] == 0:
               ind_0 += [i]
         if isEmpty(ind_team) == False and isEmpty(ind_fed) == False:
            if ind_team[0] < ind_fed[0]:
               up_to = ind_team[0]
               for i in a4:
                  if i < up_to:
                     acc4 += [i]
            elif ind_fed[0] < ind_team[0]:
               up_to = ind_fed[0]
               for i in a4:
                  if i <= up_to:
                     acc4 += [i]
         elif (isEmpty(ind_fed) == True) and (isEmpty(ind_team) == False):
            up_to = ind_team[0]
            for i in a4:
               if i < up_to:
                  acc4 +=[i]
         elif (isEmpty(ind_team) == True) and (isEmpty(ind_fed) == False):
            up_to = ind_fed[0]
            for i in a4:
               if i <= up_to:
                  acc4 +=[i]
         elif ((isEmpty(ind_team) == True) and (isEmpty(ind_fed) == True)):
            acc4+= ind_0
         accum += acc4
      #Right
      if len(a1) >0:
         ind_fed = []
         ind_team = []
         ind_0 = []
         for i in a1:
            if isOnTeam(board,i,team)[1] == 1:
               ind_fed+=[i]
         for i in a1:
            if isOnTeam(board,i,team)[1] == -1:
               ind_team +=[i]
         for i in a1:
            if isOnTeam(board,i,team)[1] == 0:
               ind_0 += [i]
         if isEmpty(ind_team) == False and isEmpty(ind_fed) == False:
            if ind_team[0] > ind_fed[0]:
               up_to = ind_team[0]
               for i in a1:
                  if i > up_to:
                     acc1 += [i]
            elif ind_fed[0] > ind_team[0]:
               up_to = ind_fed[0]
               for i in a1:
                  if i >= up_to:
                     acc1 += [i]
         elif (isEmpty(ind_fed) == True) and (isEmpty(ind_team) == False):
            up_to = ind_team[0]
            for i in a1:
               if i > up_to:
                  acc1 +=[i]
         elif (isEmpty(ind_team) == True) and (isEmpty(ind_fed) == False):
            up_to = ind_fed[0]
            for i in a1:
               if i >= up_to:
                  acc1 +=[i]
         elif ((isEmpty(ind_team) == True) and (isEmpty(ind_fed) == True)):
            acc1+= ind_0

         accum += acc1
      #Down
      if len(a3) > 0:
         ind_fed = []
         ind_team = []
         ind_0 = []
         for i in a3:
            if isOnTeam(board,i,team)[1] == 1:
               ind_fed+=[i]
         for i in a3:
            if (isOnTeam(board,i,team))[1] == -1:
               ind_team +=[i]
         for i in a3:
            if isOnTeam(board,i,team)[1] == 0:
               ind_0 += [i]
         if isEmpty(ind_team) == False and isEmpty(ind_fed) == False:
            if ind_team[0] > ind_fed[0]:
               up_to = ind_team[0]
               for i in a3:
                  if i > up_to:
                     acc3 += [i]
            elif ind_fed[0] > ind_team[0]:
               up_to = ind_fed[0]
               for i in a3:
                  if i >= up_to:
                     acc3 += [i]
         elif (isEmpty(ind_fed) == True) and (isEmpty(ind_team) == False):
            up_to = ind_team[0]
            for i in a3:
               if i > up_to:
                  acc3 +=[i]
         elif (isEmpty(ind_team) == True) and (isEmpty(ind_fed) == False):
            up_to = ind_fed[0]
            for i in a3:
               if i >= up_to:
                  acc3 +=[i]
         elif ((isEmpty(ind_team) == True) and (isEmpty(ind_fed) == True)):
            acc3+= ind_0
         accum += acc3
      rval = []
      rval = bubbleSort_asc(accum)
      return rval



def getQueenMoves(board,position,team):
   accum = []
   bishop = getBishopMoves(board,position,team)
   rook = getRookMoves(board,position,team)
   accum = bishop + rook
   return accum



def getKingMoves(board,position,team):
   accum1 = []
   rval = []
   king_pos = position
   bishop = getBishopMoves(board,position,team)
   rook = getRookMoves(board,position,team)
   accum1 = bishop + rook
   for i in accum1:
      if (myabs(king_pos - i) == 9) or (myabs(king_pos - i) == 8) or (myabs(king_pos - i) == 7) or (myabs(king_pos -i) == 1):
         rval += [i]

   return rval



def IsPositionUnderThreat(board,position,player):
   #Player Notation:
   # White = 10
   # Black = 20

   if player == 10:
      opponent = 20
   elif player == 20:
      opponent = 10
   opp_pawn = []
   opp_pawnMoves = []

   opp_knight = []
   opp_knightMoves = []

   opp_bishop = []
   opp_bishopMoves = []

   opp_rook = []
   opp_rookMoves = []

   opp_queen = []
   opp_queenMoves = []

   opp_king = []
   opp_kingMoves = []

   accum = []
   current_position = position

   opponent_positions = GetPlayerPositions(board,opponent)
   for i in opponent_positions:
      if board[i] % 10 == 0:
         opp_pawn += [i]
      elif board[i] % 10 == 1:
         opp_knight += [i]
      elif board[i] % 10 == 2:
         opp_bishop += [i]
      elif board[i] % 10 == 3:
         opp_rook += [i]
      elif board[i] % 10 == 4:
         opp_queen += [i]
      elif board[i] % 10 == 5:
         opp_king += [i]
   j = 0
   if isEmpty(opp_pawn) != True:
      for j in opp_pawn:
         if GetPieceLegalMoves(board,j) != False:
            opp_pawnMoves += GetPieceLegalMoves(board,j)

   if isEmpty(opp_knight) != True:
      for j in opp_knight:
         if GetPieceLegalMoves(board,j) != False:
            opp_knightMoves += GetPieceLegalMoves(board,j)

   if isEmpty(opp_bishop) != True:
      for j in opp_bishop:
         if GetPieceLegalMoves(board,j) != False:
            opp_bishopMoves += GetPieceLegalMoves(board,j)

   if isEmpty(opp_rook) != True:
      for j in opp_rook:
         if GetPieceLegalMoves(board,j) != False:
            opp_rookMovesMoves += GetPieceLegalMoves(board,j)

   if isEmpty(opp_queen) != True:
      for j in opp_queen:
         if GetPieceLegalMoves(board,j) != False:
            opp_queenMoves += GetPieceLegalMoves(board,j)

   if isEmpty(opp_king) != True:
      for j in opp_king:
         if GetPieceLegalMoves(board,j) != False:
            opp_kingMoves += GetPieceLegalMoves(board,j)

   accum = list(set(bubbleSort_asc(opp_pawnMoves + opp_knightMoves + opp_bishopMoves + opp_rookMoves + opp_queenMoves + opp_kingMoves)))
   cnt = 0
   for i in accum:
      if i == current_position:
         cnt +=1
   if cnt >0:
      return True
   else:
      return False


def canEatPawn(board,player):

   if player == 10:
      opponent = 20
      pawnPiece = 20
   elif player == 20:
      opponent = 10
      pawnPiece = 10
   opp_pawn = []
   accum = []

   opponent_positions = GetPlayerPositions(board,opponent)
   for i in opponent_positions:
      if board[i] % 10 == 0:
         opp_pawn += [i]

   moves = allMoves(board,player)

   if opp_pawn == []:
       return False

   else:
      for i in moves:
         for j in i[1]:
            if board[j] == pawnPiece:
               accum += [[i[0],j]]
      return accum

# --- canEat<Piece> mtds determine if a player can eat opposing <Piece>


def canEatKing(board,player):
   if player != 10 & player != 20:
      return -1
   if player == 10:
      opponent = 20
   elif player == 20:
      opponent = 10

   opp_king = 0
   accum = []

   opponent_positions = GetPlayerPositions(board,opponent)
   for i in opponent_positions:
      if board[i] % 10 == 5:
         opp_king = i

   moves = allMoves(board,player)

   if opp_king == 0:
       return False

   else:
      for i in moves:
         for j in i[1]:
            if board[j] == opp_king:
               accum += [[i[0],j]]
      return accum

def canEatQueen(board,player):
   opponent = 0
   if player == 10:
      opponent = 20
   elif player == 20:
      opponent = 10
   opp_queen = 0
   accum = []

   opponent_positions = GetPlayerPositions(board,opponent)
   for i in opponent_positions:
      if board[i] % 10 == 4:
         opp_queen = i

   moves = allMoves(board,player)

   if opp_queen != 0:
      for i in moves:
         for j in i[1]:
            if board[j] == opp_queen:
               accum += [[i[0],j]]
      return accum
   else:
      return False


def canEatRook(board,player):
   opponent = 0
   if player == 10:
      opponent = 20
      rookPiece = 23
   elif player == 20:
      opponent = 10
      rookPiece = 13
   opp_rook = []
   accum = []

   opponent_positions = GetPlayerPositions(board,opponent)
   for i in opponent_positions:
      if board[i] % 10 == 3:
         opp_rook = i

   moves = allMoves(board,player)

   if opp_rook != []:
      for i in moves:
         for j in i[1]:
            if board[j] == rookPiece:
               accum += [[i[0],j]]
      return accum

   else:
      return False


def canEatKnightorBishop(board,player):
   opponent = 0
   if player == 10:
      opponent = 20
   elif player == 20:
      opponent = 10
   opp_kb = []
   accum = []

   opponent_positions = GetPlayerPositions(board,opponent)
   for i in opponent_positions:
      if board[i] % 10 == 2 or board[i] % 10 == 1:
         opp_kb = i

   moves = allMoves(board,player)

   if opp_kb != []:
      for i in moves:
         for j in i[1]:
            if (board[j] % 10 == 1) or (board[j] % 10 == 2):
               accum == [[i[0],j]]
      return accum
   else:
      return False



def isKingInCheck(board,player):
    #Is <player>'s king in check
    if ((player != 10) & (player != 20)):
        return -1
    if player == 10:
        opponent = 20
    else:
        opponent = 10
# if opponent can eat my King
    if canEatKing(board,opponent) == True:
        return True
    else:
        return False

def isCheckmate(board,player):
    # Basically is <player> going to lose?
    if ((player != 10) & (player != 20)):
        return -1

    if isKingInCheck(board,player) == True:
        # Find king pos
        for i in board:
            if i % 10 == 5:
                kingPos = i
        # Can the king move to new pos and not be under threat
        kingMoves = GetPieceLegalMoves(board,kingPos)
        # Copy the list to see moves if get rid of threat without chaniging Board
        copyB = list(board)
        badMoves = []
        if ((kingMoves != False) and (kingMoves != 1)):
            for i in kingMoves:
                copyB[kingPos],copyB[i] = 0,cobyB[kingPos]
                if isKingInCheck(copyB,player) == True:
                    badMove += [i]
            if len(kingMoves) > len(badMoves):
                return False
            elif len(kingMoves) == len(badMoves):
                return True


def isStalemate(board,player):
    # --- For the player whose turn it is --- #
    if ((player != 10) & (player != 20)):
        return -1
    if player == 10:
        opponent = 20
    else:
        opponent = 10

    playerPos = GetPlayerPositions(board,player)
    playerMoves = []
    for i in playerPos:
        if GetPieceLegalMoves(board,i) != False:
            playerMoves += GetPieceLegalMoves(board,i)

    if isKingInCheck(board,player) == True:
        return False
    elif ((isKingInCheck(board,player) == False) and (len(playerMoves) == 0)):
        return True


def allMoves(board,player):
    playerPos = GetPlayerPositions(board,player)
    moves = []
    for pos in playerPos:
        pieceMove = GetPieceLegalMoves(board,pos)
        if pieceMove != False:
            moves += [[pos,pieceMove]]
    if moves != []:
        return moves
    else:
        return False


def genWinningMove(board,player):
    if player == 10:
        opponent = 20
    else:
        opponent = 10
    moves = allMoves(board,player)
    copyBoard = list(board)
    winningMoves = []

    if allMoves != False:
        for element in moves:
            for move in element[1]:
                copyBoard[element[0]],copyBoard[move] = 0,copyBoard[element[0]]
                if isCheckmate(copyBoard,opponent) == True:
                    winningMoves += [[element[0],element[1][0]]]
    else:
        return False
    return winningMoves

def genNonLosing(board,player):
    if player == 10:
        opponent = 20
    else:
        opponent = 10

    copyBoard = list(board)
    nonLosing = []
    oppMoves = allMoves(board,opponent)
    playerMoves = allMoves(board,player)

    pos = 0
    for i in board:
        if ((i % 10 == 5) and (i - player == 5)):
            kingPos = pos
        pos += 1

    if isKingInCheck(board,player) == True:
        for move in oppMoves:
            for oppDestination in move[1]:
                if oppDestination == kingPos:
                    for element in playerMoves:
                        for movp in element[1]:
                            if movp == oppDestination:
                                nonLosing = [element[0],movp]

    elif isKingInCheck(board,player) == False:

        if (canEatRook(board,player) != False) or (canEatPawn(board,player) != False) or (canEatKnightorBishop(board,player) != False) or (canEatQueen(board,player) != False) or (canEatKing(board,player) != False):
            eatRook = canEatRook(board,player)
            eatPawn = canEatPawn(board,player)
            eatKB = canEatKnightorBishop(board,player)
            eatKing = canEatKing(board,player)
            eatQueen = canEatQueen(board,player)

            accum = []
            if eatKing != False:
                accum += eatKing
            if eatQueen != False:
                accum += eatQueen
            if eatRook != False:
                accum += eatRook
            if eatKB != False:
                accum += eatKB
            if eatPawn != False:
                accum += eatPawn
            if accum != []:
                nonLosing = accum[0]

        elif (canEatRook(board,player) == False) and (canEatPawn(board,player) == False) and (canEatKnightorBishop(board,player) == False) and (canEatQueen(board,player) == False) and (canEatKing(board,player) == False):
            noLose = []
            pMoves = blessMoves(board,player)
            ratings = []
            for i in pMoves:
                ratings += [i[1]]
            maxRating = max(ratings)

            for i in pMoves:
                if i[1] == maxRating:
                    noLose += [i[0]]
            import random
            nonLosing = [random.choice(noLose)]


    else:
        return False

    return nonLosing



def possMoves(board,player):
   accum = []
   perhaps = []
   safer = []
   team_pos = GetPlayerPositions(board,player)
   copyBoard = list(board)

   for i in team_pos:
      s = GetPieceLegalMoves(board,i)
      if s != False:
         perhaps += s
   for j in perhaps:
       copyBoard[i],copyBoard[j] = 0,copyBoard[i]
       if IsPositionUnderThreat(copyBoard,j,player) == False:
          safer+=[j]
     # if there are no safe moves theres only risky moves
   if safer == []:
       return perhaps
   for c in safer:
      for i in team_pos:
         g = GetPieceLegalMoves(board,i)
         if g != False:
            for m in g:
               if m == c:
                  accum += [[i,c]]

   return accum


def blessMoves(board,player):
    # --- Gives ratings for each move safe move--- #
   to_eval = possMoves(board,player)
   accum = []
   rating_base = 1.0

   checkmate = 99.99
   king = 3.75

   queen = 3.50

   rook = 2.75
   knight_bishop = 2.25

   pawn = 1.30

   preratacc = []
   ratacc = []
   #If you can eat someone else your supaaaa blessed
   for i in range(0,len(to_eval)):
      preratacc += [to_eval[i][1]]

   bigMove = genWinningMove(board,player)
   if bigMove != []:
      for i in to_eval:
         for e in bigMove[1]:
            if i == [bigMove[0],bigMove[e]]:
               ratacc += [rating_base*checkmate]


   for i in preratacc:
      if board[i] == OppKing(player):
        ratacc += [rating_base*king]
     #Check if it equals the Queen
      elif board[i] == OppQueen(player):
        ratacc += [[to_eval[i],rating_base*queen]]
     #Check if it equals the rook
      elif board[i] == OppRook(player):
        ratacc += [rating_base*rook]
     #Check if is equals the Knight or Bishop
      elif board[i] == OppKnight(player) or board[i] == OppBishop(player):
        ratacc += [rating_base*knight_bishop]
     #Check if it equals the Pawn
      elif board[i] == OppPawn(player):
        ratacc += [rating_base*pawn]
      elif board[i] == 0:
        ratacc += [rating_base*1.0]

      for i in to_eval:
         for j in ratacc:
            accum += [[i,j]]

      return accum



def chooseMove(bless):
   L = list(bless)
   m = L[0][0]
   return m


def OppKing(player):
   if player == 10:
      return 25
   elif player == 20:
      return 15

def OppQueen(player):
   if player == 10:
      return 24
   elif player == 20:
      return 14

def OppRook(player):
   if player == 10:
      return 23
   elif player == 20:
      return 13

def OppBishop(player):
   if player == 10:
      return 22
   elif player == 20:
      return 12

def OppKnight(player):
   if player == 10:
      return 21
   elif player == 20:
      return 11

def OppPawn(player):
   if player == 10:
      return 20
   elif player == 20:
      return 10
