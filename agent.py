import random

class Agent:
   
   symbol = 'X'
   gameArray = []
   gameMoves = []
   
   def __init__( self, xORo ):
      self.symbol = xORo


   def getMove( self, gameboard):
      playerNum = False
      found = False #if the board state is found in the database
      if self.symbol == 'O':
         playerNum = True
      self.gameArray.append(gameboard)
      if( not playerNum): #player 1
         with open("player1db.txt", "r") as fileRead:
            for line in fileRead:
               if gameboard in line:
                  found = True
                  #print("found it")
                  #print(line)
                  probs = [float(x) for x in line[10:].split(",")] #get the probabilities
                  index = [0,1,2,3,4,5,6,7,8] #get the index of the move
                  moveInd = random.choices(index,weights = probs, k = 1)
                  self.gameMoves.append(moveInd[0])
                  return moveInd[0]
            if not found:
               with open("player1db.txt", "a") as fileWrite:
                  probabilities = []
                  emptySpaces = 0
                  for i in range(9):
                     if(gameboard[i] == '-'):
                        emptySpaces += 1
                  for i in range(9):
                     if(gameboard[i] == '-'):
                        probabilities.append(100/emptySpaces)
                     else:
                        probabilities.append(0)
                  boardString = gameboard
                  for i in range(9):
                     boardString += "," + str(probabilities[i])
                  #print(gameboard, " and ", sum(probabilities))
                  fileWrite.write(boardString + "\n")
                  #probs = [int(x) for x in gameboard[10:len(line)-1].split(",")] #get the probabilities
                  index = [0,1,2,3,4,5,6,7,8] #get the index of the move
                  moveInd = random.choices(index,weights = probabilities, k = 1)
                  self.gameMoves.append(moveInd[0])
                  return moveInd[0]
                  
      else: #player 2
         with open("player2db.txt", "r") as fileRead:
            for line in fileRead:
               if gameboard in line:
                  found = True
                  #print("found it")
                  #print(line)
                  probs = [float(x) for x in line[10:].split(",")] #get the probabilities
                  index = [0,1,2,3,4,5,6,7,8] #get the index of the move
                  moveInd = random.choices(index,weights = probs, k = 1)
                  self.gameMoves.append(moveInd[0])
                  return moveInd[0]
            if not found:
               with open("player2db.txt", "a") as fileWrite:
                  probabilities = []
                  emptySpaces = 0
                  for i in range(9):
                     if(gameboard[i] == '-'):
                        emptySpaces += 1
                  for i in range(9):
                     if(gameboard[i] == '-'):
                        probabilities.append(100/emptySpaces)
                     else:
                        probabilities.append(0)
                  boardString = gameboard
                  for i in range(9):
                     boardString += "," + str(probabilities[i])
                  #print(gameboard, " and ", sum(probabilities))
                  fileWrite.write(boardString + "\n")
                  #probs = [int(x) for x in gameboard[10:len(line)-1].split(",")] #get the probabilities
                  index = [0,1,2,3,4,5,6,7,8] #get the index of the move
                  moveInd = random.choices(index,weights = probabilities, k = 1)
                  self.gameMoves.append(moveInd[0])
                  return moveInd[0]

         
   def endGame( self, status, gameboard ):
      
      # learn from the result... ?
      if status == 1: 
         #self.gameArray.append(gameboard)
         newLines = []
         playerNum = False
         if self.symbol == 'O':
            playerNum = True
         # print(self.gameArray)
         beta = 1
         # print(self.gameMoves)
         if( not playerNum): #player 1
            for i in range(len(self.gameArray)):
               alpha = 2/(2**(len(self.gameArray)-(i+1)))
               with open("player1db.txt", "r") as fileRead:
                  lines = fileRead.readlines()
               with open("player1db.txt", "r") as fileRead:
                  for line in fileRead:
                     if self.gameArray[i] in line:
                        probs = [float(x) for x in line[10:].split(",")]
                        nonEmptySpaces = 0
                        for n in range(len(probs)):
                           if(probs[n] != 0):
                              nonEmptySpaces += 1
                        probs[self.gameMoves[i]] += beta
                        newSum = sum(probs)
                        ratio = newSum/100
                        takeOff = beta/nonEmptySpaces
                        for m in range(len(probs)):
                           if probs[m] != 0:
                              probs[m] = probs[m]/ratio

                        newLine = self.gameArray[i]
                        for j in range(len(probs)):
                           newLine += "," + str(probs[j])
                        newLines.append(newLine)
                        with open("player1db.txt", "w") as fileWrite:
                           for k in lines:
                              if line not in k:
                                 fileWrite.write(k)
                              else:
                                 fileWrite.write(newLine + "\n")  
                        beta+=1   
         else: #player 2
            for i in range(len(self.gameArray)):
               alpha = 2/(2**(len(self.gameArray)-(i+1)))
               with open("player2db.txt", "r") as fileRead:
                  lines = fileRead.readlines()
               with open("player2db.txt", "r") as fileRead:
                  for line in fileRead:
                     if self.gameArray[i] in line:
                        #print(line)
                        p = 0
                        while(line[p] !=  ','):
                              p += 1
                        probs = [float(x) for x in line[p+1:].split(",")]
                        nonEmptySpaces = 0
                        for n in range(len(probs)):
                           if(probs[n] != 0):
                              nonEmptySpaces += 1
                        probs[self.gameMoves[i]] += beta
                        newSum = sum(probs)
                        ratio = newSum/100
                        takeOff = beta/nonEmptySpaces
                        for m in range(len(probs)):
                           if probs[m] != 0:
                              probs[m] = probs[m]/ratio

                        newLine = self.gameArray[i]
                        for j in range(len(probs)):
                           newLine += "," + str(probs[j])
                        newLines.append(newLine)
                        with open("player2db.txt", "w") as fileWrite:
                           for k in lines:
                              if line not in k:
                                 fileWrite.write(k)
                              else:
                                 fileWrite.write(newLine + "\n")  
                        beta+=1   
         # you won the game
         p = 1
      elif status == -1:
         # you lost the game
         newLines = []
         playerNum = False
         if self.symbol == 'O':
            playerNum = True
         beta = 1
         if( not playerNum): #player 1
            for i in range(len(self.gameArray)):
               alpha = 2/(2**(len(self.gameArray)-(i+1)))
               with open("player1db.txt", "r") as fileRead:
                  lines = fileRead.readlines()
               with open("player1db.txt", "r") as fileRead:
                  for line in fileRead:
                     if self.gameArray[i] in line:
                        probs = [float(x) for x in line[10:].split(",")]
                        nonEmptySpaces = 0
                        for n in range(len(probs)):
                           if(probs[n] != 0):
                              nonEmptySpaces += 1
                        probs[self.gameMoves[i]] = abs(probs[self.gameMoves[i]] - beta)
                        newSum = sum(probs)
                        ratio = newSum/100
                        takeOff = beta/nonEmptySpaces
                        for m in range(len(probs)):
                           if probs[m] != 0:
                              probs[m] = probs[m]/ratio

                        newLine = self.gameArray[i]
                        for j in range(len(probs)):
                           newLine += "," + str(probs[j])
                        newLines.append(newLine)
                        with open("player1db.txt", "w") as fileWrite:
                           for k in lines:
                              if line not in k:
                                 fileWrite.write(k)
                              else:
                                 fileWrite.write(newLine + "\n")  
                        beta+=1
         else: #player 2
            for i in range(len(self.gameArray)):
               alpha = 2/(2**(len(self.gameArray)-(i+1)))
               with open("player2db.txt", "r") as fileRead:
                  lines = fileRead.readlines()
               with open("player2db.txt", "r") as fileRead:
                  for line in fileRead:
                     if self.gameArray[i] in line:
                        #print(line)
                        probs = [float(x) for x in line[10:].split(",")]
                        nonEmptySpaces = 0
                        for n in range(len(probs)):
                           if(probs[n] != 0):
                              nonEmptySpaces += 1
                        probs[self.gameMoves[i]] = abs(probs[self.gameMoves[i]] - beta)
                        newSum = sum(probs)
                        ratio = newSum/100
                        takeOff = beta/nonEmptySpaces
                        for m in range(len(probs)):
                           if probs[m] != 0:
                              probs[m] = probs[m]/ratio

                        newLine = self.gameArray[i]
                        for j in range(len(probs)):
                           newLine += "," + str(probs[j])
                        newLines.append(newLine)
                        with open("player2db.txt", "w") as fileWrite:
                           for k in lines:
                              if line not in k:
                                 fileWrite.write(k)
                              else:
                                 fileWrite.write(newLine + "\n")  
                        beta+=1
         p = -1
      else: # status == 0
         # no winner
         p = 0



#db file looks like this:
   #--------- 0,0,0,0,0,0,0,0,0
   #Read in the gameboard 
#getMove things needed:
   #needs to run through whichever file based on self.symbol
   #  #if it doesnt exist, put it in the file with even probability for each open spot
   #