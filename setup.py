import pyautogui
import time

def setup(fields_to_scan):
    x_inv = []
    y_inv = []
    counter = 1

    for each in range(fields_to_scan):
        time.sleep(3)
        x, y = pyautogui.position()
        x_inv.append(str(x))
        x_inv.append(",")
        y_inv.append(str(y))
        y_inv.append(",")
        print("#" + str(counter) + " Done! Move on.")
        counter += 1

    x_inv.pop()
    y_inv.pop()

    with open("xdata.txt", "w") as file:
        for i in x_inv:
            file.write(i)
    with open("ydata.txt", "w") as file:
        for i in y_inv:
            file.write(i)

def main():
    print("How many fields of your inventory do you want to scan? (all inventory slots are 36) :")
    fields_to_scan = input(">")
    setup(fields_to_scan)

main()
