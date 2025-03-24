import sys
import time 
import os


def slow_print(text, delay=0.05):
    """Prints text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() #move to the next line after printing

def pause(secs):
    time.sleep(secs)

def clear():
    os.system("clear")