#dodac samochow
#ocenic samochow
#oznaczyc jako przetestowany
# wypisac wszystkie samochody
# filtrowac
# zapamietywac dane do pliku

class Car():

    def __init__ (self, marka, model, rocznik, powypadkowy):

        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.powypadkowy = powypadkowy

baza_danych = []

def add_car(marka, model, rocznik, powypadkowy):

    new_car = Car(marka, model, rocznik, powypadkowy)
    baza_danych.append(new_car)

def print_database(car):
    print("{:10} | {:10} | {:10} | {:10}".format(car.marka, car.model, car.rocznik, car.powypadkowy))

def add_car_from_input():
    marka = input("Podaj marke auta: ")
    model = input("Podaj model auta: ")
    rocznik = int(input("Rocznik auta: "))
    powypadkowy = input("Czy auto jest powypadkowe [Y/N]:")
    if powypadkowy == "Y":
        powypadkowy = True
    elif powypadkowy == "N":
        powypadkowy = False
    else:
        powypadkowy = "brak danych"

    new_car = Car(marka, model, rocznik, powypadkowy)
    baza_danych.append(new_car)


add_car("BMW", "M5", 2005, False)
add_car("Mercedes", "SLC", 2011, True)
add_car_from_input()

for car in baza_danych:
    print_database(car)
