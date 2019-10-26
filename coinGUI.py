#######################
# Name: Jyran Daigs
# Date: 10/22/19
# Description: GUI
######################
from Tkinter import *

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        #parent.attributes("-fullscreen", True)
        self.setupGUI()
        
    def setupGUI(self):
        initVal = 0.0
        # the display
        self.display = Label(self, text="${}(bank)".format(initVal), borderwidth=1, anchor=E, bg = "white", height=1, font=("TimesNewRoman", 50))   
        self.display.grid(row=0, column=1, columnspan=2, rowspan=2, sticky=E)

            #------------------------#
            # pennies  |     bank    |
            # nickels  |--------------
            # dimes    | additional
            # quarters |
            #-------------------------

        # configure rows and columns of the Frame to adjust to the window
        # 4 rows
        for row in range(4):
            Grid.rowconfigure(self, row, weight=2)
        # 4 columns
        for col in range(4):
            Grid.columnconfigure(self, col, weight=2)

        # pennies
        pennies = 0
        p = Button(self, text="pennies", bg="white", borderwidth=1, activebackground="white", font=("TimesNewRoman", 25))
        p.grid(row=0, column=0, columnspan=1, sticky=N+S+E+W)
        
        # nickels
        n = Button(self, text="nickels", bg="white", borderwidth=1, activebackground="white", font=("TimesNewRoman", 25))
        n.grid(row=1, column=0, columnspan=1, sticky=N+S+E+W)

        # dimes
        d = Button(self, text="dimes", bg="white", borderwidth=1, activebackground="white", font=("TimesNewRoman", 25))
        d.grid(row=2, column=0, columnspan=1, sticky=N+S+E+W)

        # quarters
        q = Button(self, text="quarters", bg="white", borderwidth=1, activebackground="white", font=("TimesNewRoman", 25))
        q.grid(row=3, column=0, columnspan=1, sticky=N+S+E+W)

        # packs everything into the GUI
        self.pack(side=TOP, fill=BOTH, expand=True)

###########################
#WIDTH = 600
#HEIGHT = 520
# create the window        
window = Tk()
#window.geometry("{}x{}".format(WIDTH, HEIGHT))
# title
window.title("Coin Counter")
# generate the GUI
coinGUI = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()
