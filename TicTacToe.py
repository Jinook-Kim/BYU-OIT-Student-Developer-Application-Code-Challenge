from random import randint

# make sure user input 1 or 2
def validCheck(prompt):
     while True:
          num = input(prompt)
          if num == '1' or num == '2' : break
          else: print("Please enter 1 or 2.\n")

     return num

def winTest():
     #if someone win
     for i in winList:
          if all(x == "X" for x in (i[0], i[1], i[2])):
               showGameBoard()
               print("You Won! Do you want to play again?") 
               return 1

          elif all(x == "O" for x in (i[0], i[1], i[2])):
               showGameBoard()
               print("You Lost! Do you want to play again?")
               return 1
     
     #draw
     if all([isinstance(i, str) for i in gameBoard]):
          showGameBoard()
          print("Draw! Do you want to play again?")
          return 2
     
     return 0

def updateWinList(num, char):
     for i in range(8):
          for j in range(3):
               if winList[i][j] == num : winList[i][j] = char
               
def showGameBoard():
     cnt = 0
     print("")
     for i in gameBoard:
          cnt += 1
          print(i, end=" ")
          if cnt%3 == 0 : print("")

playAgain = True
while playAgain:
     gameBoard = [1,2,3,4,5,6,7,8,9]
     winList = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

     whoFirst = validCheck("1. I want to go fisrt.\n2. The computer can go first.\nEnter your answer: ")

     #when the computer goes first
     if whoFirst == "2" :
          randNum = randint(0,8)
          gameBoard[randNum] = "O"
          updateWinList(randNum+1, "O")
     
     cnt = 0 
     while True:
          showGameBoard()
          
          #user turn
          while True:
               play = input("Enter where you want to play: ")
               while True:
                    try:
                         play = int(play)
                         break
                    except:
                         play = input("Please enter valid number: ")
                         
               if play > 9 or not (play == gameBoard[play-1]):
                    print("You cannot play there.")     
               else:
                    gameBoard[play-1] = "X"
                    updateWinList(play, "X")
                    break

          #chock if the game is over
          if winTest() != 0:
               answer = validCheck("1. Yes\n2. No\nEnter your answer: ")
               if answer == "2" : 
                    playAgain = False
                    break
               else: 
                    break

          #Computer turn
          #try to win
          played = False
          for i in winList:
               if i.count("O") == 2 and i.count("X") == 0 :
                    for j in i:
                         if j != "O" and j != "X": 
                              gameBoard[j-1] = "O"
                              updateWinList(j, "O")
                              played = True
                              break
               if played : break

          #block user
          if not played :
               for i in winList:
                    if i.count("X") == 2 :
                         for j in i:
                              if j != "X" and j != "O": 
                                   gameBoard[j-1] = "O"
                                   updateWinList(j, "O")
                                   played = True
                                   break
                    if played : break
               
          #Make it two
          if not played :
               for i in winList:
                    if i.count("O") == 1 and i.count("X") == 0 :
                         for j in i:
                              if j != "O" and j != "X": 
                                   gameBoard[j-1] = "O"
                                   updateWinList(j, "O")
                                   played = True
                                   break
                    if played : break
                         
          #play randomly
          if not played:
               while True:
                    randNum = randint(0,8)
                    if gameBoard[randNum] != "X" and gameBoard[randNum] != "O":
                         gameBoard[randNum] = "O"
                         updateWinList(randNum, "O")
                         played = True
                         break
                         
          #chock if the game is over
          if winTest() != 0:
               answer = validCheck("1. Yes\n2. No\nEnter your answer: ")
               if answer == "2" :
                    playAgain = False
                    break
               else:
                    break