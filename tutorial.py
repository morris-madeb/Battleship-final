# a constant tutorial text to print when the user asks for it
TUTORIAL_TEXT = """-----------------------BATTLESHIP TUTORIAL-----------------------
THE GOAL OF THE GAME: Defeat your opponent by finding the 
                      positions of their ships and sinking them.

HOW TO WIN: Be the first player to sink all of your opponents 
            ships!

THE BOARD: your board is a 10x10 grid of spaces where you can
           place ships.

SETUP: Both players will begin by placing ships on to their 
       secret board.
       
PLACING A SHIP: Before the game begins, you will be prompted
                to place your ships on the BOARD. To place a 
                ship, choose a position on the board where you 
                want your ship to be. This will be where the 
                HEAD of your ship will go. The head of the ship is
                the first stud position. That means that 
                depending on the ship's orientation (vertical or
                horizontal) the position chosen will decide 
                where the piece will start.
                
                example:
                if Isaac places a carrier ship in position a1 and the 
                orientation is horizontal the board will look 
                like this:
                0   1   2   3   4   5   6   
                ____________________________
                
                A | C   C   C   C   C   0   

                B | 0   0   0   0   0   0

"""

# an easy way to print the tutorial and manage the input bs here
def Print_Tutorial():
  print(TUTORIAL_TEXT)
  input("enter to go back to placing ships")
