# importing only those functions 
# which are needed 
from Tkinter import * 
  
# creating tkinter window 
root = Tk() 
  
# Adding widgets to the root window 
Label(root, text = 'Pennies', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
  
# Creating a photoimage object to use image 
photo = PhotoImage(file = "images/penny.gif") 
  
# here, image option is used to 
# set image on button 
Button(root, text = 'Click Me !', image = photo).pack(side = TOP) 
  
mainloop()

# WITH TEXT AND IMAGE AS THE BUTTON
