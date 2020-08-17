import pyautogui
import time
import simplejson as json

# Bot Chain Function Dictionary

functions = {
    1: "open_close_inv()",
    2: "rightclick_hotbar()",
    3: "leftclick_hotbar()"
}

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

# Bot Chains

def create_bot_chain():
    bot_chain = input("Chain : ").split(", ") # ==> Will be changed in a while cause of UI ==> smarter Input

    with open("bot_chain.txt", "w") as file:
        json.dump(bot_chain, file)

def read_bot_chain(bot_chain_file):
    with open(bot_chain_file, "r") as file:
        bot_chain = json.load(file)

        for i in bot_chain:
            print(functions[int(i)])

        return bot_chain

# General Functions

def get_data():
    with open("data.txt", "r") as file:
        inv = json.load(file)
        return inv

def main():
    inv = get_data()
    create_bot_chain()
    chain = read_bot_chain("bot_chain.txt")
    print(chain)

main()
