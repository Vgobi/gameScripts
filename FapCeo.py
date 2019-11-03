import os
import datetime
import time
import re
import subprocess

start = 0
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class FapCeo():
    
    def __init__(self, numberOfClicks = 10, levelUp = False, SellCompany = False, girlsNumber = 11):
        print ("Script start {}".format(datetime.datetime.now()))
        self.numberOfClicks = numberOfClicks
        self.levelUp = levelUp
        self.SellCompany = SellCompany
        self.girlsNumber = girlsNumber

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

    def girls(self):
        print ("Clicker use {} girls".format(self.girlsNumber))
        for i in X:
            xX = str(X[i])
            yY = str(Y[i])
            print ("X: {} Y: {}".format(xX,yY))
          #  subprocess.call(["xdotool", "mousemove", "X", "Y", "click", "1"])

            #if self.levelUp == True:
             #   self.girlsLevelUp()

    def clickPrivateShow(self):
        start = 0
        print ("Make {} Clicks".format(self.numberOfClicks))
        while (start < self.numberOfClicks):
            self.girls()
            start = start + 1

        if self.levelUp != False and self.SellCompany != False:
            self.trySellCompany()
        else:
            print ("Script made {} cliks".format(self.numberOfClicks))

def main():
    game = FapCeo(10,True,True)
    game.clickPrivateShow()

main()