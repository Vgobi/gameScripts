import os
import datetime
import time
import re
import subprocess

start = 0
X = ["410", "553", "578", "703", "874", "993", "851", "698", "823", "967", "1129"]
Y = ["440", "534", "336", "429", "316", "401", "428", "590", "670", "585", "494"]
print(len(X))

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
        i =0
        print ("Clicker use {} girls".format(self.girlsNumber))
        while i < len(X):
            subprocess.call(["xdotool", "mousemove", X[i], Y[i], "click", "1"])
            i = i + 1

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