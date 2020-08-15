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
    slot = 18

    while on:
        pyautogui.write("e")
        pyautogui.keyDown("shift")
        for i in range(2):
            pyautogui.moveTo(inv[slot])
            pyautogui.click(button="left")
            slot += 1
            if slot > 26:
                break
        pyautogui.keyUp("shift")
        pyautogui.write("e")

        for i  in range(2):
            i += 1
            pyautogui.write(str(i))
            pyautogui.click(button="right")

        if slot > 26:
            break

def main():
    inv = get_data()
    specific_mc_action(inv)

main()
