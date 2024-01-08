#Alyn Ovell
#Simple Food Order Calculator

#imports tkinter GUI
import tkinter as tk

calculation = ""

#function that allows the numbers to be added and will print the plus symbol
def add_to_calculation(symbol):
    global calculation 
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#funtion  that evalutates at the buttons. This will clear the addition and print the result
def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
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
root.title("Simple Calculator")
root.geometry("350x400")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 12))
text_result.grid(columnspan=5, pady=10)

def create_button(text, command, row, column, color):
    button = tk.Button(root, text=text, command=command, bg=color, fg="white", font=("Arial", 10))
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

#defines and labels all the food options as buttons. Uses a lambda expression in the command in order ot pass an int value. It aslo gives the button color
button1 = create_button("Chicken: $10", lambda: add_to_calculation(10), 2, 0, "#4CAF50")
button2 = create_button("Hamburger: $12", lambda: add_to_calculation(12), 2, 1, "#4CAF50")
button3 = create_button("Salmon: $10", lambda: add_to_calculation(10), 2, 2, "#4CAF50")
button4 = create_button("Fried Potatoes: $5", lambda: add_to_calculation(5), 3, 0, "#4CAF50")
button5 = create_button("Fried Green Beans: $5", lambda: add_to_calculation(5), 3, 1, "#4CAF50")
button6 = create_button("Chef Salad: $9", lambda: add_to_calculation(9), 3, 2, "#4CAF50")
button7 = create_button("Small Beverage: $3", lambda: add_to_calculation(3), 4, 0, "#4CAF50")
button8 = create_button("Large Beverage: $5", lambda: add_to_calculation(5), 4, 1, "#4CAF50")

#This button must be pressed between each food items in order to properly add the total amount
buttonAdd = create_button("+", lambda: add_to_calculation("+"), 4, 2, "#FFA500")  # Orange color

#this button calls the evaluate function with no lambda so it can be called properly
buttonEqual = create_button("=", evaluate_calculation, 5, 1, "#008CBA")  # Blue color

#Button calls the clear function with no lambdo so it can be called properly
buttonClear = create_button("Clear", clear_field, 5, 2, "#FF0000")  # Red color

root.mainloop()
