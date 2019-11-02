import os
import datatime
import re
import subprocess

class FapCeo():

    start = 0
    def __init__(self, numberOfClicks = 1000, levelUp = False):
        print "Script start"
        self.numberOfClicks = numberOfClicks
        self.levelUp = levelUp

    def girlsLevelUp(self):
        print "Level Up Girls"
        subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])

    def clickPrivateShow(self, numberOfClicks):
        print "Make {}".format(numberOfClicks)
        while (start < numberOfClicks):
            if self.levelUp == True:
                self.girlsLevelUp()
            subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])

