import random
from PIL import Image
import time

hiragana = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so", "ta", "tci", "tsu",
            "te","to", "na", "ni", "nu", "ne", "no", "ha", "hi", "hu", "he", "ma", "mi", "mu", "me", "mo", "ya", "yu",
            "yo", "ra", "ri", "ru", "re", "ro", "wa", "o", "n"]
print(len(hiragana))
i = 0
number = int(input("number of sights: "))
while i < number:

    print("{:3}|{}".format(i, hiragana[random.randrange(0, len(hiragana))]))
#    img = Image.open("a.jpg")
#    img.show()
    i += 1
#    enter = input("Press enter")
#    print(enter)
    time.sleep(5)
