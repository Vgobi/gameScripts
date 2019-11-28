import datetime
import time
import subprocess

X = ["410", "553", "578", "703", "874", "993", "851", "698", "823", "967", "1129"]
Y = ["440", "534", "336", "429", "316", "401", "428", "590", "670", "585", "494"]


class FapCeo:

    def __init__(self, number_of_clicks=10, level_up=True, sell_company=True, hire_new_girls=True, girls_number=11,
                 chest_event=False):
        print("Script start {}".format(datetime.datetime.now()))
        self.number_of_clicks = number_of_clicks
        self.level_up = level_up
        self.sell_company = sell_company
        self.girls_number = girls_number
        self.hire_new_girls = hire_new_girls
        self.chest_event = chest_event
        self.start_time = datetime.datetime.now()

    def girls_level_up(self):
        subprocess.call(["xdotool", "mousemove", "1180", "816", "click", "1"])

    def hire_girls(self):
        i = 0
        print("Hire new girls")
        time.sleep(20)
        subprocess.call(["xdotool", "mousemove", "1168", "530", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "1158", "206", "click", "1"])
        time.sleep(5)
        subprocess.call(["xdotool", "mousemove", "893", "357", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "1158", "206", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "893", "357", "click", "1"])
        #Ustawianie pod levelovanie
        time.sleep(20)
        while i < 11:
            subprocess.call(["xdotool", "mousemove", X[i], Y[i], "click", "1"])
            i += 1
        time.sleep(10)
        subprocess.call(["xdotool", "mousemove", "1180", "816", "click", "1"])
        time.sleep(10)
        subprocess.call(["xdotool", "mousemove", X[0], Y[0], "click", "1"])
        time.sleep(10)
        subprocess.call(["xdotool", "mousemove", "1180", "816", "click", "1"])
        time.sleep(10)


    def try_sell_company(self):
        print("Try Sell Company")
        subprocess.call(["xdotool", "mousemove", "1326", "179", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "868", "595", "click", "1"])
        time.sleep(10)
        subprocess.call(["xdotool", "mousemove", "1307", "505", "click", "1"])

    def girls(self):
        i = 0
        while i < len(X):
            subprocess.call(["xdotool", "mousemove", X[i], Y[i], "click", "1"])
            if self.level_up is True:
                self.girls_level_up()
            i += 1


    def click_private_show(self):
        click_nr = 0
        while click_nr < self.number_of_clicks:
            self.girls()
            click_nr += 1

    def click_chest_event(self):
        print("Time to Click on chest box")
        chest_clicks = 0
        while chest_clicks < 100:
            subprocess.call(["xdotool", "mousemove", "1254", "662", "click", "1"])
            chest_clicks += 1

    def chest_event_deltatime(self):
        actual_time = datetime.datetime.now()
        print(self.start_time.strftime("%H:%M:%S"))
        time_to_next_chest = self.start_time + datetime.timedelta(hours=2, minutes=2)
        if actual_time > time_to_next_chest:
            print("Actual time: {} is bigger that delta time: {}".format(actual_time, time_to_next_chest))
            self.click_chest_event()
            print("Set new start time")
            self.start_time = datetime.datetime.now()
