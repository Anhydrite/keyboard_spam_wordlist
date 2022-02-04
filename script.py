from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()
wordlist = open("./dict.txt", "r")

def on_press(key):
    if key != Key.up:
        return
    print("press")
    for i in range(100):
        keyboard.type(wordlist.readline())
        keyboard.press(Key.enter)
    


def on_release(key):
    print("stop")
    if key == Key.esc:
        # Stop listener
        return False

with Listener(
        on_press=on_press,
       on_release=on_release) as listener:
   listener.join()
