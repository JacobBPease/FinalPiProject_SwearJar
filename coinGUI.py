######################################
# FINAL PI ACTIVITY // GROUP PROJECT #
######################################

# importing necessary libraries including our created module
from Tkinter import *
import coinCheck

# inherits from the frame class to house all the buttons
class MainGUI(Frame):
    # constructor that takes the parameter for the GUI
    def __init__(self, master):
        Frame.__init__(self, master)
        self.createMain(master)

    # function that opens the file, reads and adds it to a list and then closes the file		
    # tht build in "type" could be a different name as its only a parameter understood to be for the individual coin choice
    def openCoinsFile(self, type):
        # opens the file through a relative path using the read mode
        f = open("Coins.txt", 'r')
        #initialize the list
        Coins = []
        #read each line and add it to the list
        fl = f.readlines() # It needed to look at f1 because f.readlines puts the file into a list format, meaning we can append it properly 
        for x in fl:
            Coins.append(int(x))
        #stores list in local variables for accessibility
        pennies = Coins[0]
        nickels = Coins[1]
        dimes = Coins[2]
        quarters = Coins[3]
        
        # closes after the file is read into the list
        f.close()
        
        return Coins[type]

    # function that creates the main buttons for each of the coins	
    def createMain(self, master):
        
        # configure rows and columns of the Frame to adjust to the window
        # 4 rows
        for row in range(4):
            Grid.rowconfigure(self, row, weight=2)
        # 4 columns
        for col in range(3):
            Grid.columnconfigure(self, col, weight=2)

        # All coin buttons are white and the other functions are default.
        # Penny button
        penny = PhotoImage(file="images/penny.gif")
        pennyImage = penny.subsample(1, 1)
        self.buttonPenny = Button(master, text="Pennies", bg="white", image=pennyImage, compound=LEFT, borderwidth=1, font=("Elephant", 20), command=lambda: self.display(0))
        # not repetition, just keeping another reference because tkinter loses the image
        self.buttonPenny.image = pennyImage
        self.buttonPenny.grid(row=0, column=0, sticky=N+S+E+W)
        #self.buttonPenny.pack(fill=BOTH)

        # Nickel button
        nickel = PhotoImage(file="images/nickel.gif")
        nickelImage = nickel.subsample(5, 5)
        self.buttonNickel = Button(master, text="Nickels", bg="white", image=nickelImage, compound=LEFT, borderwidth=1, font=("Elephant", 20), command=lambda: self.display(1))
        # same thing, just another reference
        self.buttonNickel.image = nickelImage
        self.buttonNickel.grid(row=1, column=0, sticky=N+S+E+W)
        #self.buttonNickel.pack(fill=BOTH)

        # Dime button
        dime = PhotoImage(file="images/dime.gif")
        dimeImage = dime.subsample(2, 2)
        self.buttonDime = Button(master, text="Dimes", bg="white", image=dimeImage, compound=LEFT, borderwidth=1, font=("Elephant", 20), command=lambda: self.display(2))
        # same thinggg
        self.buttonDime.image = dimeImage
        self.buttonDime.grid(row=2, column=0, sticky=N+S+E+W)
        #self.buttonDime.pack(fill=BOTH)

        # Quarter button
        quarter = PhotoImage(file="images/quarter.gif")
        quarterImage = quarter.subsample(8, 8)
        self.buttonQuarter = Button(master, text="Quarters", bg="white", image=quarterImage, compound=LEFT, borderwidth=1, font=("Elephant", 20), command=lambda: self.display(3))
        self.buttonQuarter.image = quarterImage
        self.buttonQuarter.grid(row=3, column=0, sticky=N+S+E+W)
        #self.buttonQuarter.pack(fill=BOTH)

        # Total amount button
        self.buttonTotal = Button(master, text="Total Amount", borderwidth=1, font=("Elephant", 25), command=lambda: self.display('t'))
        self.buttonTotal.grid(row=3, column=2, sticky=N+S+E+W)
        #self.buttonTotal.pack(side=BOTTOM, fill=BOTH)

        # Add button
        self.buttonAdd = Button(master, text="Add", borderwidth=1, font=("Elephant", 25), command=lambda: self.Prompt(1))
        self.buttonAdd.grid(row=0, column=2, sticky=N+S+E+W)
        #self.buttonAdd.pack(side=LEFT, fill=BOTH)

        # Remove button
        self.buttonRemove = Button(master, text="Remove", borderwidth=1, font=("Elephant", 25), command=lambda: self.Prompt(0))
        self.buttonRemove.grid(row=3, column=2, rowspan=2, columnspan=2, sticky=N+S+E+W)
        #self.buttonRemove.pack(side=RIGHT, fill=BOTH)


#  function to set variables from the text file equal to their respective coin		
    def display(self, type):
        if (type == 0):
            penny = self.openCoinsFile(0) 
            # zero to tell which index from Coins list to return, in this case penny.
            if (self.buttonPenny['text'] == 'Pennies'):
                    self.buttonPenny.configure(text = "{}".format(penny))
            else:
                    self.buttonPenny.configure(text = "Pennies")
        
        elif (type == 1):
            nickel = self.openCoinsFile(1)
            #1 = nickel's index in Coins list
            if (self.buttonNickel['text'] == 'Nickels'):
                    self.buttonNickel.configure(text = "{}".format(nickel))
            else:
                    self.buttonNickel.configure(text = "Nickels")		
                
        elif (type == 2):
            dime = self.openCoinsFile(2)
            #2 = dime value index in Coins list
            if (self.buttonDime['text'] == 'Dimes'):
                    self.buttonDime.configure(text = "{}".format(dime))
            else:
                    self.buttonDime.configure(text = "Dimes")

        elif (type == 3):
            quarter = self.openCoinsFile(3)
            #3 = quarter value index in Coins list
            if (self.buttonQuarter['text'] == 'Quarters'):
                    self.buttonQuarter.configure(text = "{}".format(quarter))
            else:
                    self.buttonQuarter.configure(text = "Quarters")

        else:
            #only other option is total
            #imports all values if list Coins
            penny = self.openCoinsFile(0) 
            nickel = self.openCoinsFile(1)
            dime = self.openCoinsFile(2)
            quarter = self.openCoinsFile(3)
            total = 0
    
            float(total)
            total= penny*0.01 + nickel*0.05 + dime*0.1 + quarter*0.25
            subtotal = '%.2f' % total
                
            if (self.buttonTotal['text'] == 'Total Amount'):
                    self.buttonTotal.configure(text = "${}".format(subtotal))
            else:
                    self.buttonTotal.configure(text = "Total Amount")

    # creates the prompt in a individual window
    def Prompt(self, function):
        window = Tk()
        prompt = Prompt(window, function)
        window.mainloop()

# creates another window after clicking on a certain button
class Prompt(Frame):
    def __init__(self, master, function): # function serves as 1 or 0 to rep add or remove 
        Frame.__init__(self, master)
        self.function = function
        self.createPrompt(master, function)
        
    def createPrompt(self, master, function):
        self.prompt = Label(master, text='Please select which type of coin you would like to remove.', font="Elephant")
        self.prompt.grid(row=0, column=0, columnspan=4)
        # note for jacob // I'm pretty sure I could do it, but I didn't want to break anything.. this is just a note to tell you fix the prompt for the add function, it comes up as remove.
        if (function):
                self.prompt = Label(master, text='Please select which type of coin you would like to add.', font="Elephant")

        self.buttonPenny = Button(master, text='Penny', bg="white", font=("Elephant"), command=lambda: self.calc(0, function))
        self.buttonPenny.grid(row=1, column=0, sticky=N+S+E+W)
        
        self.buttonNickel = Button(master, text='Nickel', bg="white", font=("Elephant"), command=lambda: self.calc(1, function))
        self.buttonNickel.grid(row=1, column=1)
        
        self.buttonDime = Button(master, text='Dime', bg="white", font=("Elephant"), command=lambda: self.calc(2, function))
        self.buttonDime.grid(row=1, column=2)
        
        self.buttonQuarter = Button(master, text='Quarter', bg="white", font=("Elephant"), command=lambda: self.calc(3, function))
        self.buttonQuarter.grid(row=1, column=3)
        
        
    #check function calls the function that determines how many coins were added to the jar
    #type variable holds the value that tells the calculator which coin it's identifying
    def check(self, type):
        n = importTest.coinCheck(50, type)
        return n
        
    def calc(self, type, function):
        coinCheck.coinCalc(type, function)

# - - - - MAIN - - - - #

#initializes window
window = Tk()
# sets a custom title for the window
window.title("GROUP PROJECT // COIN COUNTER")
# makes the instance of the class MainGUI and passes in the tkinter window as a parameter
coinGUI = MainGUI(window)
# window stays open until user closes it
window.mainloop()


# SO FAR:
# I added comments in places lacking, re-organized some of the functions to make
# more sense logically.. along with renaming some variable names for less confusion
# and fixed spacing

# LEFT:
# add images and reorganize the gui to look nice
# try to get the windows to close out after.


        
        
    
