import tkinter as tk

class GUI:
    def __init__(self):
        pass
    
    def newWindow(self, windowname):
        master = tk.Tk(className=windowname)
        window = tk.Canvas(master, width=100, height=400, bg='#262626')
        master.mainloop()

GUI().newWindow('Casino Royale')