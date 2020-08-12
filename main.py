import pyautogui
import time

x_inv = []
y_inv = []

def get_data():
    with open("xdata.txt", "r") as file:
        file_content = file.read()
        x_inv = file_content.split(",")

    with open("ydata.txt", "r") as file:
        file_content = file.read()
        y_inv = file_content.split(",")

    return x_inv, y_inv

def mc_action(x_inv, y_inv):
    counter = 1
    for i in range(9):
        time.sleep(1)
        pyautogui.write(str(counter))
        pyautogui.click(button="right")
        counter += 1

    pyautogui.write("e")
    for ix in x_inv[18]:
        for iy in y_inv[18]:
            pyautogui.keyDown("shift")
            pyautogui.click(int(ix), int(iy))

def main():
    x_inv, y_inv = get_data()
    time.sleep(5)
    mc_action(x_inv, y_inv)

main()
