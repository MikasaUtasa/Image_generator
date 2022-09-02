from PIL import Image
import numpy as np
import argparse


def Create(args):
    image = Image.open(args.picture)
    image = image.convert('RGB')
    # image.thumbnail((200, 200))
    data = np.asarray(image)
    data = data[0::6]
    string = ""
    chars = {0: " ", 1: "^", 2: "/", 3: "#", 4: "⠿"}
    with open('Obraz.txt', 'w', encoding="utf-8") as f:
        for row in data:
            line = ""
            for char in row:
                line += chars[(sum(char // 3)) // 60]
            f.write(line + '\n')


def Print(args):
    image = Image.open(args.picture)
    image = image.convert('RGB')
    image.thumbnail((200, 200))
    data = np.asarray(image)
    data = data[0::2]
    string = ""
    chars = {0: " ", 1: "^", 2: "/", 3: "#", 4: "⠿"}
    for row in data:
        line = ""
        for char in row:
            line += chars[(sum(char // 3)) // 60]
        print(line)


# Press the green button in the gutter to run the script.
if _name_ == '_main_':
    parser = argparse.ArgumentParser(description='ASCII Image gererator')
    parser.add_argument('-p', '--picture')
    args = parser.parse_args()

    Print(args)