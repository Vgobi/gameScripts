import random

def ten():

    numbers={0:"zero", 1:"ichi", 2:"ni", 3:"san", 4:"yon", 5:"go", 6:"roku", 7:"nana", 8:"hachi", 9:"kyuu",10: "juu"}
    losowanie = random.randrange(11)
    print(numbers[losowanie])
    poda_liczbe = input("Podaj cyfre: ")
    if int(poda_liczbe) is int(losowanie):
        print("Zgadłeś")
    else:
        print("dupa")

ten()