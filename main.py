import pyautogui
import time
import simplejson as json

# Bot Chain Functions

def open_close_inv():
    pyautogui.write("e")

def rightclick_hotbar(slot):
    pyautogui.write(str(slot))
    pyautogui.click(button="right")

def leftclick_hotbar(slot):
    pyautogui.write(str(slot))
    pyautogui.click(button="left")

def loop_hotbar(modus, duration):
    if modus.lower() == "none":
        for i in range(9):
            i += 1
            pyautogui.write(str(i))
            time.sleep(duration)
    if modus.lower() == "leftclick":
        for i in range(9):
            i += 1
            pyautogui.write(str(i))
            pyautogui.click(button="left")
            time.sleep(duration)
    if modus.lower() == "doubleclick":
        for i in range(9):
            i += 1
            pyautogui.write(str(i))
            pyautogui.doubleClick(button="left")
            time.sleep(duration)
    if modus.lower() == "rightclick":
        for i in range(9):
            i += 1
            pyautogui.write(str(i))
            pyautogui.click(button="right")
            time.sleep(duration)
    if modus.lower() == "drop":
        for i in range(9):
            i += 1
            pyautogui.write(str(i))
            pyautogui.write("q")
            time.sleep(duration)
    if modus.lower() == "dropall":
        for i in range(9):
            i += 1
            pyautogui.write(str(i))
            pyautogui.keyDown("ctrl")
            pyautogui.write("q")
            pyautogui.keyUp("ctrl")
            time.sleep(duration)

def loop_inv(modus, duration, inv):
    if modus.lower() == "none":
        for i in inv:
            pyautogui.moveTo(i)
            time.sleep(duration)
    if modus.lower() == "drop":
        for i in inv:
            pyautogui.moveTo(i)
            pyautogui.write("q")
            time.sleep(duration)
    if modus.lower() == "dropall":
        for i in inv:
            pyautogui.moveTo(i)
            pyautogui.keyDown("ctrl")
            pyautogui.write("q")
            pyautogui.keyUp("ctrl")
            time.sleep(duration)

def grab_item(start_slot, end_slot, inv):
    start_slot -= 1
    end_slot -= 1
    pyautogui.moveTo(inv[start_slot])
    pyautogui.dragTo(inv[end_slot][0], inv[end_slot][1], button="left")
    pyautogui.click(button="left")

# Actual Chain Function
 
def bot_chain(inv):
    time.sleep(5)
    grab_item(1, 36, inv)

# General Functions

def get_data():
    with open("data.txt", "r") as file:
        inv = json.load(file)
        return inv

def main():
    inv = get_data()
    bot_chain(inv)

main()
