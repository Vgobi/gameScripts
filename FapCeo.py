import os
import datatime
import time
import re
import subprocess

class FapCeo():

    start = 0
    X = []
    Y = []
    def __init__(self, numberOfClicks = 1000, levelUp = False, trySellCompany = False, ):
        print "Script start {}".format(datatime.time.now())
        self.numberOfClicks = numberOfClicks
        self.levelUp = levelUp
        self.trySellCompany = trySellCompany

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "Script end {}".format(datatime.time.now())

    def girlsLevelUp(self):
        print "Level Up Girls"
        subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])

    def trySellCompany(self):
        print "Try Sell Company"
        subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])
        time.sleep(10)
        subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])

    def clickPrivateShow(self, numberOfClicks):
        print "Make {}".format(numberOfClicks)
        while (start < numberOfClicks):
            if self.levelUp == True:
                self.girlsLevelUp()
            subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])

        if levelUp == True and self.trySellCompany == True:
            self.trySellCompany()
        else:
            print "Script made {} cliks".format(numberOfClicks)


game = FapCeo
game.__init__(10, True, True, True)