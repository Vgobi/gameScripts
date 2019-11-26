import random
from PIL import Image

hiragana = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "si", "su", "se", "so", "ta", "ti", "tu", "te",
            "to", "na", "ni", "nu", "ne", "no", "ha", "hi", "hu", "he", "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo",
            "ra", "ri", "ru", "re", "ro", "wa", "o", "n"]
print(len(hiragana))
i = 0

while 1:

    print("{:3}|{}".format(i, hiragana[random.randrange(0, len(hiragana))]))
    img = Image.open("a.png")
    img.show
    i += 1
    input("Press enter")
