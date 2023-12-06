#Tired of my computer randomly going to sleep while i'm working
#Windows is a piece of shit
#this is a dumb "security" setting

import pyautogui
import time
import sys

def graphic():
    graphic = '''
    

  _  _  ___    _    ___   ___ _  __
 | \\| |/ _ \\  | |  / _ \\ / __| |/ /
 | .` | (_) | | |_| (_) | (__| ' < 
 |_|\\_|\\___/  |____\\___/ \\___|_|\\_\\
_____________________________________
                                              
'''
    print(graphic)


def length_of_time():
    if len(sys.argv) > 1:
        argz = int(sys.argv[1])
    else:
        print("argument must be number of seconds before keyboard event")
    return argz

def main():
    
    graphic()
    print("Program running: Computer will not be auto locked or put to sleep now.")
    while True:
        time.sleep(length_of_time()) 
        pyautogui.press('space')
        pyautogui.press('enter')

if __name__=="__main__":
    main()
    

