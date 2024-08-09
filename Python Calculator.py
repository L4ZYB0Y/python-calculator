class calculator:
    def add (self, x , y):
        return x + y 

    def subtract (self, x , y):
        return x - y

    def multiply (self, x , y):
        return x * y

    def divide(self, x , y):
        if y == 0:
            return "Error: Division by zero"
        else:
            return x / y



        def main():
                 calc = Calculator()

                 print("Addition:", calc.add(5, 3))
                 print("Subtraction:", calc.subtract(5, 3))
                 print("Multiplication:", calc.multiply(5, 3))
                 print("Division:", calc.divide(5, 3))
                 print("Division by zero:", calc.divide(5, 0))

                 if __name__ == " __main__":
                     main()
                 
  
