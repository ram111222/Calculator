# Welcome to the basic calculator. This is an example to be showing python power. Everything attached is tested and
#  throws no errors. Find anything let us know https://github.com/ram111222/Calculator/issues To run make
# sure all files are located in the same directory. Enjoy

# Imports the file named DEFINED in the local directory
import Defined

# Creates an inf loop
while True:
    # Instead of Immediately erroring out. It has a way to keep running
    try:
        # Gathers user number/Equation inputs
        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))
        sgn = input("What operation are you doing? (add): ")
        # Starts checking to see if any inputs match
        if sgn == "add":
            # Pulls info from the DEFINED file to do equations
            Ans = Defined.add(a, b)
            # Prints results using F. F basically just looks at what is located in the parent function
            print(f"The sum of {a} and {b} is {Ans}.")
        elif sgn == "divide":
            Ans = Defined.divide(a, b)
            print(f"the Answer of {a} and {b} divided is {Ans}")
        elif sgn == "multiply":
            Ans = Defined.multiply(a, b)
            print(f"the answer of {a} and {b} Multiplied is {Ans}")
        elif sgn == "subtract":
            Ans = Defined.sub(a, b)
            print(f"The answer of {a} and {b} subtracted is {Ans}")
        else:
            print("Invalid operation.")
    # If an error is thrown, these catch it and print out an end statement instead of some random error
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        break
    except ZeroDivisionError:
        print("It is not possible to divide by zero. Were not the ftc team 9791")
        break
    finally:
        print("Have a good day!")
        break
