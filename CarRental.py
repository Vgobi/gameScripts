"""
Aplikacja do wypożyczania aut

!!! Info o autach !!!
1. Marka
2. Model
3. Rok produkcji
4. Właściciel
5. Info o wypożyczajacym
6. Klasa auta

!!! Zarzadzanie !!!
1. Pobieranie informacji o autach w wypożyczalni
2. Dodawanie nowych aut
3. Modyfikowanie parametrów bazy
4. Filtrowanie po atrybutach
5. Data zwrotu auta

Obsługa przez konsole i http
"""

class CarRental():

    baza_danych = []

    def __init__(self, marka="", model="", rok_produkcji=1900, owner="", wypozyczajacy="", klasa_auta=""):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.owner = owner
        self.wypozyczajacy = wypozyczajacy
        self.klasa_auta = klasa_auta



    def print_database(self,car):
        print("{:10} | {:10} | {:10} | {:10} | {:10} | {:10}".format(car.marka, car.model, car.rok_produkcji, car.owner,
                                                   car.wypozyczajacy, car.klasa_auta))

    def addCar(self, marka, model, rok_produkcji, owner, wypozyczajacy, klasa_auta):

        car = CarRental(marka, model, rok_produkcji, owner, wypozyczajacy, klasa_auta)
        self.baza_danych.append(car)

    def add_car_via_input(self):
        marka = input("Marka auta: ")
        model = input("model auta: ")
        rok_produkcji = input("Rok Produkcji: ")
        owner = input("Owner: ")
        wypozyczajacy = input("Wypozyczajacy:")
        klasa_auta = input("Klasa auta: ")
        car = CarRental(marka, model, rok_produkcji, owner, wypozyczajacy, klasa_auta)
        self.baza_danych.append(car)

    def modify_owner(self, index, parameter, new_value):
        new = self.baza_danych[index]
        if parameter == "owner":
            new.owner = new_value
        #new.parameter = new_value




    def filter(self):
        pass


car = CarRental()
car.addCar("BMW", "M5", 1999, "Adam", "Bartek", "A")
car.addCar("Mercedes", "CLK", 2015, "Bogdan", "Manio", "Sport")
# car.add_car_via_input()
for car in car.baza_danych:
    print(car.print_database(car))
car.modify_owner(0, "owner", "Pampkin")
for car in car.baza_danych:
    print(car.print_database(car))