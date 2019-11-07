import datetime
import time
import subprocess

X = ["410", "553", "578", "703", "874", "993", "851", "698", "823", "967", "1129"]
Y = ["440", "534", "336", "429", "316", "401", "428", "590", "670", "585", "494"]


class FapCeo():

    def __init__(self, number_of_clicks=10, level_up=False, sell_company=False, hire_new_girls=False, girls_number=11):
        print("Script start {}".format(datetime.datetime.now()))
        self.number_of_clicks = number_of_clicks
        self.level_up = level_up
        self.sell_company = sell_company
        self.girls_number = girls_number
        self.hire_new_girls = hire_new_girls

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Script end {}".format(datetime.datetime.now()))

    def girls_level_up(self):
        print("Level Up Girls")
        subprocess.call(["xdotool", "mousemove", "1180", "816", "click", "1"])

    def hire_girls(self):
        print("Hire new girls")
        time.sleep(10)
        subprocess.call(["xdotool", "mousemove", "1168", "530", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "1158", "206", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "893", "357", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "1158", "206", "click", "1"])

    def try_sell_company(self):
        print("Try Sell Company")
        subprocess.call(["xdotool", "mousemove", "1326", "179", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "868", "595", "click", "1"])
        time.sleep(10)
        subprocess.call(["xdotool", "mousemove", "945", "132", "click", "1"])
        if self.hire_new_girls is True:
            self.hire_girls()

    def girls(self):
        i = 0
        print("Clicker use {} girls".format(self.girls_number))
        while i < len(X):
            subprocess.call(["xdotool", "mousemove", X[i], Y[i], "click", "1"])
            if self.level_up is True:
                self.girls_level_up()
            i = i + 1

    def click_private_show(self):
        click_nr = 0
        print("Make {} Clicks".format(self.number_of_clicks))
        while click_nr < self.number_of_clicks:
            self.girls()
            click_nr = click_nr + 1

        if self.level_up is not False and self.sell_company is not False:
            self.try_sell_company()
        else:
            print("Script made {} clicks".format(self.number_of_clicks))


def main():
    game = FapCeo(50, True, True, True)
    game.click_private_show()


main()
