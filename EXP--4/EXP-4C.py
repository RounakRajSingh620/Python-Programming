from _tkinter import *

def key(event):
    print( "pressed"),repr(event.char)
def callback(event):
    frame.focus_set()
    print("clicked at"), event.x, event.y
    frame = frame( width=100, height=100)
    frame.bind("<Key>", key)
    frame.bind("<Button-1>", callback)
    frame.pack()

