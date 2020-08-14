import pyautogui
import time
import simplejson as json

def setup():
    inv = [[] for _ in range(36)]
    inv_y = []
    inv_x = []
    counter = 1

    answer =  input("""Welcome to the setup!
To start you have to make sure that you have the default controls in Minecraft unlocked. Otherwise the script wont work.
Now you just can type 'start' and you will recieve further instructions.\n > """)
    if answer.lower() == "start":
        print("""For the scanning you will have to hover over a certain pattern of your inventory.
First the most left 4 inventory slots then the whole first row. Here a pattern.""")
        time.sleep(5)
        print("<-------><-------><-------><-------><-------><-------><-------><-------><-------><------->")
        print("|       ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("|  1/5  ||   6   ||   7   ||   8   ||   9   ||   10  ||   11  ||   12  ||   13  ||   14  |")
        print("|       ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("<-------><-------><-------><-------><-------><-------><-------><-------><-------><------->")
        print("|       ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("|   2   ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("|       ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("<-------><-------><-------><-------><-------><-------><-------><-------><-------><------->")
        print("|       ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("|   3   ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("|       ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("<-------><-------><-------><-------><-------><-------><-------><-------><-------><------->")
        print("<-------><-------><-------><-------><-------><-------><-------><-------><-------><------->")
        print("|       ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("|   4   ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("|       ||       ||       ||       ||       ||       ||       ||       ||       ||       |")
        print("<-------><-------><-------><-------><-------><-------><-------><-------><-------><------->")
        answer = input("""If you are ready type 'ready' and the scanning will beginn in 3 seconds. After you typed ready jump in Minecraft and hover over the first slot.
The script will show you when to move so you can just relax. \n > """)
        if answer.lower() == "ready":
            for i in range(3):
                i += 1
                print(str(i))
                time.sleep(1)
            print("Go!")
        else:
            exit()
    else:
        exit()

    time.sleep(5)
    for i in range(4):
        x, y = pyautogui.position()
        for i in range(9):
            inv_y.append(y)
        pyautogui.write("etMove", interval=0.1)
        pyautogui.press("esc")
        pyautogui.write("e")
        time.sleep(3)

    for i in range(9):
        x, y = pyautogui.position()
        inv_x.append(x)
        pyautogui.write("etMove", interval=0.1)
        pyautogui.press("esc")
        pyautogui.write("e")
        time.sleep(3)

    counter = 0
    x_counter = 0

    for i in range(36):
        inv[counter].append(inv_x[x_counter])
        inv[counter].append(inv_y[counter])
        x_counter += 1
        counter += 1

        if x_counter >= 9:
            x_counter = 0

    with open("data.txt", "w") as file:
        json.dump(inv, file)

    print("Okay the scanning is finished. Bye :)")
    time.sleep(1)

setup()
