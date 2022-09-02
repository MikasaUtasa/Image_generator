from PIL import Image
import numpy as np

def Create():

    image = Image.open('ryan.jpg')
    image = image.convert('RGB')
    #image.thumbnail((200, 200))
    data = np.asarray(image)
    data = data[0::6]
    string = ""
    chars = {0:" ", 1:"^", 2:"/", 3:"#", 4:"⠿"}
    with open('Obraz.txt', 'w', encoding="utf-8") as f:
        for row in data:
            line = ""
            for char in row:
                line += chars[(sum(char//3))//60]
            f.write(line + '\n')

def Print():
    image = Image.open('ryan.jpg')
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
if __name__ == '__main__':
    Print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
