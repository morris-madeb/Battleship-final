import os
import tutorial

# Constants
HEADER = "--------------------BATTLESHIP by Isaac and Morris--------------------"
SHIPS = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
INDEXES_CONVERSION = {"A": 11,"B": 22,"C": 33,"D": 44,"E": 55,"F": 66,"G": 77,"H": 88,"I": 99,"J": 110}
INDEXES = ("A","B","C","D","E","F","G","H","I","J")
VALID_DIGITS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

# the board class, where the program deals with setup and printing of the gameboard
class Board():
  def printBoard(self, board):
    for i in range(0, len(board), 11):
      j = 0
      print("\t\t", end = "") # Row Padding
      for j in range(0,11):
        if i == 0:
          print(int((board[j]/10) - 1), end = "   ")
          if j == 10:
            print("\n\t\t__________________________________________", end="")
        elif (i + j) % 11 == 0 and board[i+j] > 110:
          print(INDEXES[int((board[i+j] / 10)-12)], end= " | ")
        else:
          print(board[i+j], end = "   ")
        j+=1
      print("\n")

  # Places the ships after checking to make sure all positions are valid
  def placeShip(self, startPosition, ship):
    studnum = 0
    studpos = []
    for stud in range(0, int(SHIPS[ship])):
      if self.orientation == 1: #0 = hor 1 = vert
        if (startPosition + studnum) > 121 or (startPosition + studnum) % 11 == 0 or self.board[startPosition + studnum] != 0:
          print("invalid Position")
          return 0
        else:
          studpos.append(startPosition + studnum)
          studnum += 11 #adding 11 bc index 
      else:
        # self.board[startPosition + studnum] = ship[0]
        if (startPosition + studnum) > 121 or (startPosition + studnum) % 11 == 0 or self.board[startPosition + studnum] != 0:
          return 0
        else:
          studpos.append(startPosition + studnum)
          studnum += 1
    for shippos in studpos:
      self.board[shippos] = ship[0]
    return 1

  # checks the action submitted by the user and does the respective action after confirming it is valid
  def __actionCheck(self, action, ship):
    action = action[0:3].strip()
    print(action)
    if len(action) >= 2 and action[1:] not in VALID_DIGITS:
      return 0
    if action.upper() == "R":
      if self.orientation == 0:
        self.orientation += 1
      else:
        self.orientation -= 1
    elif action.upper() == "T":
      os.system("clear")
      tutorial.Print_Tutorial()
      return 0
    elif len(action) >= 2 and action[0].upper() in INDEXES and action[1:] in VALID_DIGITS:
      if self.placeShip(INDEXES_CONVERSION[action[0].upper()] + int(action[1:]), ship) == 0:
        return 0
      else:
        return 1
    return 0

  # begins the board setup for the player connected to the board
  def __boardSetup(self):
    for ship in SHIPS:
      action = ""
      self.orientation = 0
      while self.__actionCheck(action, ship) < 1:
        os.system("clear")
        print(HEADER)
        self.printBoard(self.board)
        action = input("where would you like to place the HEAD of " + ship + " which spans " + str(SHIPS[ship]) + " studs.\nUse A1 Notation (ex: B8)\t\tTo rotate ship enter r\nShip Orientation: " + ("horizontal" if self.orientation == 0 else "vertical") + "\t" + "To see the tutorial enter t" + "\n")

  # initializes the board class by creating two boards: a guess board and a stored board for the player's ships. 
  # the guess board will be compared to the opponents ship board so that we can check hits and misses (see gameLogic.py)
  def __init__(self, playerObj):
    self.board = [10,20,30,40,50,60,70,80,90,100,110,
                  120,0,0,0,0,0,0,0,0,0,0,
                  130,0,0,0,0,0,0,0,0,0,0,
                  140,0,0,0,0,0,0,0,0,0,0,
                  150,0,0,0,0,0,0,0,0,0,0,
                  160,0,0,0,0,0,0,0,0,0,0,
                  170,0,0,0,0,0,0,0,0,0,0,
                  180,0,0,0,0,0,0,0,0,0,0,
                  190,0,0,0,0,0,0,0,0,0,0,
                  200,0,0,0,0,0,0,0,0,0,0,
                  210,0,0,0,0,0,0,0,0,0,0]
    self.guessBoard = [10,20,30,40,50,60,70,80,90,100,110,
                  120,0,0,0,0,0,0,0,0,0,0,
                  130,0,0,0,0,0,0,0,0,0,0,
                  140,0,0,0,0,0,0,0,0,0,0,
                  150,0,0,0,0,0,0,0,0,0,0,
                  160,0,0,0,0,0,0,0,0,0,0,
                  170,0,0,0,0,0,0,0,0,0,0,
                  180,0,0,0,0,0,0,0,0,0,0,
                  190,0,0,0,0,0,0,0,0,0,0,
                  200,0,0,0,0,0,0,0,0,0,0,
                  210,0,0,0,0,0,0,0,0,0,0]
    self.orientation = 0
    self.lives = 17
    self.used = []
    
    os.system("clear")
    input(HEADER + "\n" + playerObj.name + ", It's time to set up your board!\nTake the computer so your opponent can't cheat!\n\nPress enter to begin.\n")
    self.__boardSetup()
