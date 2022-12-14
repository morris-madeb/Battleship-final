# defines the Player class which stores name, win loss ratio, and win percent
class Player():
  def __init__(self, name):
    self.name = name.capitalize()
    self.wlRat = [0 , 0]
    self.wpercent = 0.0

  # calculates the win percentage of player over amount of games played
  def __calculate_percent(self):
    self.wpercent = round(self.wlRat[0]/(self.wlRat[0]+self.wlRat[1]) * 100, 2)
  
  # add win to player
  def addW(self):
    self.wlRat[0] +=1
    self.__calculate_percent()

  # add loss to player
  def addL(self):
    self.wlRat[1] +=1
    self.__calculate_percent()

  # creates a string of player to print at the end of a game or if you want to print it yourself whatever you woudl like you can do because functions work. I am incredibly sleep deprived and my life is in shambles. Yours, Morris
  def __str__(self):
    self.__calculate_percent()
    return self.name + " has a win:loss ratio of " + str(self.wlRat[0]) + ":" + str(self.wlRat[1]) + " and a win % of: " + str(self.wpercent) + "%"