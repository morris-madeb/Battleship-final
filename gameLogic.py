# imports the board and os packages. imports * (all) from player package so you dont have to write player.function
import board
import os
from player import *

# this is the full game code
class Battleship():
  # checks a guess and see's if its a hit or miss and prints accordingly
  def __checkHit(self, guess):
    checkedP = (self.curPlayer + 1) % 2
    
    if self.PBArray[checkedP].board[guess] != 0:
      print("Hit! go again!")
      self.PBArray[self.curPlayer].used.append(guess)
      self.PBArray[self.curPlayer].guessBoard[guess] = "H"
      self.PBArray[self.curPlayer].lives -= 1
    else:
      print("Miss!")
      self.PBArray[self.curPlayer].used.append(guess)
      self.PBArray[self.curPlayer].guessBoard[guess] = "M"
      self.tStatus = False

  # checks the guess/action of the player and does the respective action, returns 0 if action is invalid
  def __actionCheck(self, action):
    if action == "":
      return 0
    
    action = action[0:3]
    
    if len(action) >= 2 and action[1:] not in board.VALID_DIGITS or len(action) < 2:
        return 0
    elif len(action) >= 2 and action[0].upper() in board.INDEXES and action[1:] in board.VALID_DIGITS:
      guess = board.INDEXES_CONVERSION[action[0].upper()] + int(action[1:])
      if guess not in self.PBArray[self.curPlayer].used:
        self.__checkHit(guess)
      return 0
  
  # checks if any player wins
  def __winStatus(self):
    for i in range(0,2):
      if self.PBArray[i].lives == 0:
        return True

  # starts the game
  def __runGame(self):
    action = ""
    os.system("clear")

    # if the game is not won yet
    print(board.HEADER, end= "")
    while not self.__winStatus(): 
      print("\nIt's " + self.pArray[self.curPlayer].name + "'s turn")
      input("Take the computer so your opponent can't cheat!\nPress enter to continue")
      os.system("clear")
      # player can guess until they miss or they win
      while self.__actionCheck(action) == 0 and self.tStatus and not self.__winStatus():
        
        print(board.HEADER + "\nIt's " + self.pArray[self.curPlayer].name + "'s turn")
        self.PBArray[self.curPlayer].printBoard(self.PBArray[self.curPlayer].guessBoard)
        action = input("what square would you like to guess?\n")
      # if the player misses, end turn and print final guess board for BOTH players to see
      if not self.__winStatus():
        os.system("clear")
        print(board.HEADER + "\nMISS! Lose Your Turn!\npress enter to see the final guess board\nand pass computer to your opponent")
        input()
        os.system("clear")
        print(board.HEADER + "\nFinal Guess board for " + self.pArray[self.curPlayer].name)
        self.PBArray[self.curPlayer].printBoard(self.PBArray[self.curPlayer].guessBoard)
      
      if not self.__winStatus():
        self.curPlayer = (self.curPlayer + 1) % 2
      self.tStatus = True
      action = ""

    # once someone wins, add w to winning player and l to losing player and print out their w/l ratios and w percentage
    os.system("clear")
    self.curPlayer = (self.curPlayer + 1) % 2
    self.pArray[self.curPlayer].addL()
    self.curPlayer = (self.curPlayer + 1) % 2
    self.pArray[self.curPlayer].addW()
    print(board.HEADER + "\n" + self.pArray[self.curPlayer].name + " is our winner! congratulations!\n\nPlayer stats:\n" + self.pArray[0].__str__() + "\n" + self.pArray[1].__str__())

  # initializes the game by taking in the two players, creating new boards for each to setup, and getting other variables prepared for gameplay
  def __init__(self, p1, p2):
    self.PBArray = [board.Board(p1), board.Board(p2)]
    self.pArray = [p1, p2]
    self.curPlayer = 0
    self.tStatus = True
    self.__runGame()
