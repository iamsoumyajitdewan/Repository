import time
import pyautogui #as ss
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'D:/VS Code Programs/C C++/{}.png'.format(name)
    #name = '{}.png'.format(name)
    #time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

#screenshot()
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame, 
    text="Take Screenshot", 
    command=screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(
    frame, 
    text="QUIT", 
    command=quit)
close.pack(side=tk.LEFT)

root.mainloop()
