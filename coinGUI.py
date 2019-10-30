from Tkinter import *
import coinCheck

class App(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.createMain(master)
		
		
	def createMain(self, master):	
		self.buttonPenny = Button(master, text="Pennies", command=lambda: self.display(0))
		self.buttonPenny.pack(side=TOP, fill=X)
		
		self.buttonNickel = Button(master, text="Nickels", command=lambda: self.display(1))
		self.buttonNickel.pack(side=TOP, fill=X)
		
		self.buttonDime = Button(master, text="Dimes", command=lambda: self.display(2))
		self.buttonDime.pack(side=TOP, fill=X)
		
		self.buttonQuarter = Button(master, text="Quarters", command=lambda: self.display(3))
		self.buttonQuarter.pack(side=TOP, fill=X)
		
		self.buttonTotal = Button(master, text="Total Amount", command=lambda: self.display('t'))
		self.buttonTotal.pack(side=RIGHT, fill=Y)
		
		self.buttonAdd = Button(master, text="Add", command=lambda: self.Prompt(1))
		self.buttonAdd.pack(side=RIGHT, fill=Y)
		
		self.buttonRemove = Button(master, text="Remove", command=lambda: self.Prompt(0))
		self.buttonRemove.pack(side=RIGHT, fill=Y)
			
	def openCoinsFile(self, type):
		#opens file
		f= open("Coins.txt", 'r')
		#initialize the list
		Coins = []
		#read each line and add it to the list
		fl = f.readlines()
		for x in fl:
			Coins.append(int(x))
		#closes file to preserve memory
		f.close()
		
		return Coins[type]
			
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
			
	def Prompt(self, function):
		window = Tk()
		prompt = Prompt(window, function)
		window.mainloop()

class Prompt(Frame):
	def __init__(self, master, function): # function serves as 1 or 0 to rep add or remove 
		Frame.__init__(self, master)
		self.function = function
		self.createPrompt(master)
		
	def createPrompt(self, master):
		self.prompt = Label(master, text='Please select which type of coin you would like to add or remove.')
		self.prompt.grid(row=0, column=0, columnspan=4)
	
		self.buttonPenny = Button(master, text='Penny', command=lambda: self.calc(0))
		self.buttonPenny.grid(row=1, column=0)
		
		self.buttonNickel = Button(master, text='Nickel', command=lambda: self.calc(1))
		self.buttonNickel.grid(row=1, column=1)
		
		self.buttonDime = Button(master, text='Dime', command=lambda: self.calc(2))
		self.buttonDime.grid(row=1, column=2)
		
		self.buttonQuarter = Button(master, text='Quarter', command=lambda: self.calc(3))
		self.buttonQuarter.grid(row=1, column=3)
		
		
	#check function calls the function that determines how many coins were added to the jar
	#type variable holds the value that tells the calculator which coin it's identifying
	def check(self, type):
		n = importTest.coinCheck(50, type)
		return n
		
	def calc(self, type):
		coinCheck.coinCalc(type)

		
		
################## MAIN		
window = Tk() #initializes window
app = App(window)
window.mainloop() #constantly checks for you doing something
