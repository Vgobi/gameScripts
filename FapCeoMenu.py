from FapCeo import *


def main():
    loop = 0
    print("FapCeo automatic script")
    print("Version 1.2")
    loops_nr = int(input("Give loops number: "))
    read_default_configuration = input("Do you want read default configuration? [True/False]: ")
    print(read_default_configuration)
    if read_default_configuration is False:
        write_configuration()
        game = read_configuration()
    else:
        game = read_configuration()
    while loop < loops_nr:
        game.click_private_show()
        loop += 1
        if game.sell_company:
            game.try_sell_company()
        if game.hire_new_girls:
            game.hire_girls()
        if game.chest_event:
            game.chest_event_deltatime()
    print("Script end {}".format(datetime.datetime.now()))


def write_configuration():
    click_nr = input("Give clicks number: ")
    level_up_girls = input("Level ups girls? [True/False]: ")
    sell_company = input("Try sell company? [True/False]: ")
    hire_new_girls = input("Try hire new girls after sold company? [True/False]: ")
    girls_number = input("How many girls should by click? [1-11]: ")
    chest_event = input("Chest event [True/False]")
    default_data = "{};{};{};{};{};{}".format(click_nr, level_up_girls, sell_company, hire_new_girls,
                                              girls_number, chest_event)
    with open('config', 'w') as f:
        for line in default_data:
            f.write(line)


def read_configuration():
    with open('config', "r") as f:
        for line in f:
            read_configuration_from_file = line.split(";")
            print(read_configuration_from_file)
            if read_configuration_from_file[1].lower() == "true":
                read_configuration_from_file[1] = True
            else:
                read_configuration_from_file[1] = False
            if read_configuration_from_file[2] == "True":
                read_configuration_from_file[2] = True
            else:
                read_configuration_from_file[2] = False
            if read_configuration_from_file[3] == "True":
                read_configuration_from_file[3] = True
            else:
                read_configuration_from_file[3] = False
            if read_configuration_from_file[5] == "True":
                read_configuration_from_file[5] = True
            else:
                read_configuration_from_file[5] = False
    game = FapCeo(int(read_configuration_from_file[0]), read_configuration_from_file[1], read_configuration_from_file[2]
                  , read_configuration_from_file[3], int(read_configuration_from_file[4]),
                  read_configuration_from_file[5])
    return game


main()
