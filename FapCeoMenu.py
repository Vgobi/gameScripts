import FapCeo

def main():
    loop = 0
    print("FapCeo automatic script")
    print("Version 1.1")
    loops_nr = input("Give loops number: ")
    click_nr = input("Give clicks number: ")
    level_up_girls = input("Level ups girls? True/False: ")
    sell_company = input("Try sell company? True/False: ")
    hire_new_girls = input("Try hire new girls after sold company? True/False: ")
    girls_number = input("How many girls should by click? [1-11]: ")
    game = FapCeo(click_nr, level_up_girls, sell_company, hire_new_girls, girls_number)
    while loop < loops_nr:
        game.click_private_show()
        loop = loop + 1


main()