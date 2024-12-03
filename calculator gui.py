import tkinter as tk
from tkinter import ttk

#gets calculator window
from calculator import Calculator
calc = Calculator()

#main window
root = tk.Tk()
root.withdraw() #hides main window initially

#font and size options
def GuiSettings():
    fontwindow = tk.Toplevel()
    fontwindow.title("Select Font and Size")
    fontwindow.geometry("400x200")

    tk.Label(fontwindow, text="Select Font:").pack(pady=5)
    defaultFont = tk.StringVar(value="Arial")
    fontOptions = ttk.Combobox(fontwindow, textvariable=defaultFont, values=["Arial", "Courier", "Helvetica", "Times"])
    fontOptions.pack()

    tk.Label(fontwindow, text="Select Font Size:").pack(pady=5)
    defaultSize = tk.IntVar(value=18)
    sizeOption = ttk.Combobox(fontwindow, textvariable=defaultSize, values=[12, 14, 16, 18, 20, 24, 28])
    sizeOption.pack()
    

    def applySetting():
        font = defaultFont.get()
        size = defaultSize.get()
        fontwindow.destroy()
        openCalculator(font,size)
        
    
    tk.Button(fontwindow, text="Apply", command=applySetting).pack(pady=10)
    

def openCalculator(font, size):
    root.deiconify()
    root.title("Calculator")

    #display area
    display = tk.Entry(root, width=20, borderwidth=5, font=(font, size))
    display.grid(row=0, column=0, columnspan=4)

    def buttonClick(value):
        current = display.get()
        display.delete(0,tk.END)
        display.insert(0, current + str(value))
    
    def clearDisplay():
        display.delete(0, tk.END)

    def buttonEquals():
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    calcLayout = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1)
        ]
    
    for text, row, col in calcLayout:
        tk.Button(root, text=text, padx=20, pady=20, font=(font, size),
            command=lambda text=text: buttonClick(text)).grid(row=row, column=col)

    #operation buttons    
    tk.Button(root, text="+", padx=20, pady=20, font=(font, size), command=lambda: buttonClick('+')).grid(row=1, column=3)
    tk.Button(root, text="-", padx=20, pady=20, font=(font, size), command=lambda: buttonClick('-')).grid(row=2, column=3)
    tk.Button(root, text="*", padx=20, pady=20, font=(font, size), command=lambda: buttonClick('*')).grid(row=3, column=3)
    tk.Button(root, text="/", padx=20, pady=20, font=(font, size), command=lambda: buttonClick('/')).grid(row=4, column=3)

    #add utility buttons
    tk.Button(root, text="C", padx=20, pady=20, font=(font, size), command=clearDisplay).grid(row=4, column=0)
    tk.Button(root, text="=", padx=20, pady=20, font=(font, size), command=buttonEquals).grid(row=4, column=2)





GuiSettings()
root.mainloop()