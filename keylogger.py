# keylogger for the game
import keyboard
log_file = 'keystrokes.txt'

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

def keylog():
    keyboard.on_press(on_key_press)

    keyboard.wait()