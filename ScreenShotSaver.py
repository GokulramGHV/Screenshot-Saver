import datetime
import pyautogui
from pynput.keyboard import Key, Listener
import os


def on_press(key):
    check_key(key)
    if key in exit_combination:
        currently_pressed.add(key)
        #print(f"pressed {key}")
        if currently_pressed == exit_combination:
            #print("Exit condition has been activated.")
            listener.stop()



def on_release(key):  
    try:
        currently_pressed.remove(key)
    except KeyError:
        pass 
   

# if key is ptrscn
def check_key(key):
    if key == Key.print_screen:
        #print("pressed")
        
        now = datetime.datetime.now()
        timenow = now.strftime("%H_%M_%S")
        path = "c://Users//"+os.getlogin()+"//Desktop//Screenshots//"+str(datetime.date.today())
        try:
            pyautogui.screenshot(path+'//'+timenow+'.png')
        except FileNotFoundError:  
            os.makedirs(path)
            pyautogui.screenshot(path+'//'+timenow+'.png')
            

#exit conditions : Ctrl_l + PtrScn
exit_combination = {Key.ctrl_l, Key.print_screen}
currently_pressed = set()


#create folder
path="c://Users//"+os.getlogin()+"//Desktop//Screenshots//"+str(datetime.date.today())
try:
    os.makedirs(path)
except FileExistsError:
    pass

# Collect events until released
    with Listener(on_press=on_press,on_release=on_release) as listener:

        listener.join()
