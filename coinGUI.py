from Tkinter import *
import coinCheck

class App(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.createMain(master)
		
		
	def createMain(self, master):	
		self.buttonPenny = Button(master, text="Pennies", command=lambda: self.display('pennies'))
		self.buttonPenny.pack(side=TOP, fill=X)
		
		self.buttonNickel = Button(master, text="Nickels", command=lambda: self.display('nickels'))
		self.buttonNickel.pack(side=TOP, fill=X)
		
		self.buttonDime = Button(master, text="Dimes", command=lambda: self.display('dimes'))
		self.buttonDime.pack(side=TOP, fill=X)
		
		self.buttonQuarter = Button(master, text="Quarters", command=lambda: self.display('quarters'))
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
		Values = []
		#read each line and add it to the list
		fl = f.readlines()
		for x in fl:
			Values.append(int(x))
		#transfers values into a coins dictionary for ease of access
		Coins = {}
		Coins['pennies'] = Values[0]
		Coins['nickels'] = Values[1]
		Coins['dimes'] = Values[2]
		Coins['quarters'] = Values[3]
		#closes file to preserve memory
		f.close()
		
		return Coins[type]
			
	def display(self, type):
		if (type == 'pennies'):
			penny = self.openCoinsFile('pennies') 
			# zero to tell which index from Coins list to return, in this case penny.
			if (self.buttonPenny['text'] == 'Pennies'):
				self.buttonPenny.configure(text = "{}".format(penny))
			else:
				self.buttonPenny.configure(text = "Pennies")
		
		elif (type == 'nickels'):
			nickel = self.openCoinsFile('nickels')
			#1 = nickel's index in Coins list
			if (self.buttonNickel['text'] == 'Nickels'):
				self.buttonNickel.configure(text = "{}".format(nickel))
			else:
				self.buttonNickel.configure(text = "Nickels")		
			
		elif (type == 'dimes'):
			dime = self.openCoinsFile('dimes')
			#2 = dime value index in Coins list
			if (self.buttonDime['text'] == 'Dimes'):
				self.buttonDime.configure(text = "{}".format(dime))
			else:
				self.buttonDime.configure(text = "Dimes")

		elif (type == 'quarters'):
			quarter = self.openCoinsFile('quarters')
			#3 = quarter value index in Coins list
			if (self.buttonQuarter['text'] == 'Quarters'):
				self.buttonQuarter.configure(text = "{}".format(quarter))
			else:
				self.buttonQuarter.configure(text = "Quarters")

		else: #only other option is total
			#imports all values if list Coins
			penny = self.openCoinsFile('pennies') 
			nickel = self.openCoinsFile('nickels')
			dime = self.openCoinsFile('dimes')
			quarter = self.openCoinsFile('quarters')
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
		self.createPrompt(master, function)
		
	def createPrompt(self, master, function):
		self.prompt = Label(master, text='Please select which type of coin you would like to remove.')
		self.prompt.grid(row=0, column=0, columnspan=4)
		if (function):
			self.prompt['text'] = 'Please select which type of coin you would like to add.'
	
		self.buttonPenny = Button(master, text='Penny', command=lambda: self.calc(0, function))
		self.buttonPenny.grid(row=1, column=0)
		
		self.buttonNickel = Button(master, text='Nickel', command=lambda: self.calc(1, function))
		self.buttonNickel.grid(row=1, column=1)
		
		self.buttonDime = Button(master, text='Dime', command=lambda: self.calc(2, function))
		self.buttonDime.grid(row=1, column=2)
		
		self.buttonQuarter = Button(master, text='Quarter', command=lambda: self.calc(3, function))
		self.buttonQuarter.grid(row=1, column=3)
		
		
	#check function calls the function that determines how many coins were added to the jar
	#type variable holds the value that tells the calculator which coin it's identifying
	def check(self, type):
		n = importTest.coinCheck(50, type)
		return n
		
	def calc(self, type, function):
		coinCheck.coinCalc(type, function)

		
		
################## MAIN		
window = Tk() #initializes window
app = App(window)
window.mainloop() #constantly checks for you doing something
