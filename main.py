import pyautogui
import time
import simplejson as json

def get_data():
    with open("data.txt", "r") as file:
        inv = json.load(file)
        return inv

def specific_mc_action(inv):
    time.sleep(2)

    #for i in range(8):
    #    i += 1
    #    pyautogui.write(str(i))
    #    pyautogui.click(button="right")
    #    time.sleep(0.25)

    on = True
    fslot = 18
    lslot = fslot + 2
    while on:
        pyautogui.write("e")
        pyautogui.keyDown("shift")

        for i in inv[17:21]:
            pyautogui.click(i)
            time.sleep(1)

        pyautogui.keyUp("shift")

        on = False

def main():
    inv = get_data()
    specific_mc_action(inv)

main()
