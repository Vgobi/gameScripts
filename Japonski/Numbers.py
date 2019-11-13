import random

def guess_japan_number():

    numbers={0:"zero", 1:"ichi", 2:"ni", 3:"san", 4:"yon", 5:"go", 6:"roku", 7:"nana", 8:"hachi", 9:"kyuu",10: "juu"}
    in_row = 0
    while 1:

        losowanie = random.randrange(11)
        print(numbers[losowanie])
        try:
            poda_liczbe = int(input("Podaj cyfre: "))
        except ValueError:
            print("Prosze podać cyfre")

        if poda_liczbe is int(losowanie):
            print("Zgadłeś")

        else:
            print("dupa")
            break
        in_row = in_row + 1
    print("Zgadles {} pod rzad".format(in_row))

guess_japan_number()