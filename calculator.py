class Calculator:
    
    def __init__(self):
        self.current_value = ""
        self.total = 0
        self.operator = None
    
    def add(self):
        self.total += int(self.current_value)
        self.current_value = ""

    def subtract(self):
        self.total -= int(self.current_value)
        self.current_value = ""
    
    def multiply(self):
        self.total *= int(self.current_value)
        self.current_value = ""

    def divide(self):
        try:
            self.total /= int(self.current_value)
        except ZeroDivisionError:
            print("Cannot divide by zero")
        self.current_value = ""

    def clear(self):
        self.current_value = ""
        self.total = 0
        self.operator = None
    


def manualcalculator():
    userinput = input("Type a number, S to stop ").strip()
    calc = Calculator()
    
    if userinput == 'S':
            return calc.total
    
    try:
        calc.total = int(userinput)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return


    while True:
        operation = input("+, -, *, /, or C to clear or S to stop ").upper().strip()

        if operation == 'S':
            break
        elif operation == "C":
            calc.clear()
            print("Calculator cleared. Current total:", calc.total)
 
        elif operation in ('+', '-', '*', '/'):
            
            userinput = input("Type a number: ").strip()
            try:
                calc.current_value = int(userinput)  
                if operation == "+":
                    calc.add()
                elif operation == "-":
                    calc.subtract()
                elif operation == "*":
                    calc.multiply()
                elif operation == "/":
                    calc.divide()
                print("Current total:", calc.total) 
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid operation. Choose +, -, *, /, C, or S to stop.")
     
    return calc.total


            

