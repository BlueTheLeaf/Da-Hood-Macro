print(">> Scroll Wheel Da Hood Macro\n>> Warning: This may cause lag\n>> Press Q to toggle\n>> Made by maZ")

from pynput import mouse, keyboard
import time
import threading

toggle, toggle_lock = False, threading.Lock()

def spam_scrolling():
    while True:
        with toggle_lock:
            if toggle:
                    mouse.Controller().scroll(0, 1)
                    time.sleep(0.001)
                    mouse.Controller().scroll(0, -1)
                    time.sleep(0.001)
        time.sleep(0.001)

def on_press(key):
    global toggle
    if hasattr(key, 'char') and key.char == 'q':
        with toggle_lock:
            toggle = not toggle

scrolling_thread = threading.Thread(target=spam_scrolling, daemon=True)
scrolling_thread.start()

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()