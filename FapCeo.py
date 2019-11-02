import os
import datetime
import time
import re
import subprocess

start = 0
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class FapCeo():
    
    def __init__(self, numberOfClicks = 1000, levelUp = False, trySellCompany = False, girlsNumber = 11):
    #def __init__(self):
        print ("Script start {}".format(datetime.datetime.now()))
        self.numberOfClicks = numberOfClicks
        self.levelUp = levelUp
        self.trySellCompany = trySellCompany
        self.girlsNumber = girlsNumber
        self.girls(self.girlsNumber)
        self.clickPrivateShow(self.numberOfClicks)


    def __exit__(self, exc_type, exc_val, exc_tb):
        print ("Script end {}".format(datetime.datetime.now()))

    def girlsLevelUp(self):
        print ("Level Up Girls")
      #  subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])

    def trySellCompany(self):
        print ("Try Sell Company")
       # subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])
       # subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])
        time.sleep(10)
      # subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])

    def girls(self, girlsNumber):
        print ("Clicker use {} girls".format(girlsNumber))
        #for i in girls:
         #   X = str(X[i])
          #  Y = str(Y[i])
          #  subprocess.call(["xdotool", "mousemove", "X", "Y", "click", "1"])
        print (X)
        print (Y)
            #if self.levelUp == True:
             #   self.girlsLevelUp()

    def clickPrivateShow(self, numberOfClicks):
        print ("Make {} Clicks".format(numberOfClicks))
        while (start < numberOfClicks):
            self.girls()

        if levelUp == True and self.trySellCompany == True:
            self.trySellCompany()
        else:
            print ("Script made {} cliks".format(numberOfClicks))

def main():
    game = FapCeo()
    game.clickPrivateShow(10)

main()