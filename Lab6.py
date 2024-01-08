#Alyn Ovell
#Lab 6

#imports tkinter GUI
import tkinter as tk

calculation = ""

#function that allows the numbers to be added and will print the plus symbol
def add_to_calculation(symbol):
  global calculation 
  calculation += str(symbol)
  text_result.delete(1.0,"end")
  text_result.insert(1.0, calculation)

#funtion  that evalutates at the buttons. This will clear the addition and print the result
def evaluate_calculation():
  global calculation
  try:
    result = (str(eval(calculation)))
    calculation = ""
    text_result.delete(1.0, "end")
    text_result.insert(1.0, result)
  except:
    clear_field()
    text_result.insert(1.0, "error")
    
#function that clears any previous calculations or anything in the text box
def clear_field():
  global calculation
  calculation = ""
  text_result.delete(1.0, "end")

  
#displays result of 
root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root, height = 2, width = 16)
text_result.grid(columnspan=5)

#defines and labels all the food options as buttons. Uses a lambda expression in teh command in order ot pass an int value
button1=tk.Button(root, text="Chicken: $10", command = lambda: add_to_calculation(10))
#Places the buttons in a grid postion
button1.grid(row=2,column=0)

button2=tk.Button(root, text="Hamburger: $12", command = lambda: add_to_calculation(12))
button2.grid(row=2,column=1)

button3=tk.Button(root, text="Salmon: $10", command = lambda: add_to_calculation(10))
button3.grid(row=2,column=2)

button4=tk.Button(root, text="Fried Potatoes: $5", command = lambda: add_to_calculation(5))
button4.grid(row=3,column=0)

button5=tk.Button(root, text="Fried Green Beans: $5", command = lambda: add_to_calculation(5))
button5.grid(row=3,column=1)

button6=tk.Button(root, text="Chef Salad: $9", command = lambda: add_to_calculation(9))
button6.grid(row=3,column=2)

button7=tk.Button(root, text="Small Beverage: $3", command = lambda: add_to_calculation(3))
button7.grid(row=4,column=0)

button8=tk.Button(root, text="Large Beverage: $5", command = lambda:add_to_calculation(5))
button8.grid(row=4,column=1)

buttonAdd=tk.Button(root, text ="+", command = lambda: add_to_calculation("+"))
buttonAdd.grid(row=4, column=2)

#this button calls the evaluate function with no lambda so it can be called properly
buttonEqual=tk.Button(root, text ="=", command = evaluate_calculation)
buttonEqual.grid(row=5, column=0)

#Button calls the clear function with no lambdo so it can be called properly
buttonClear=tk.Button(root, text ="Clear", command = clear_field)
buttonClear.grid(row=5, column=2)



root.mainloop()

