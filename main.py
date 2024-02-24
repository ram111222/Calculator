import Defined

while True:
    try:
        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))
        sgn = input("What operation are you doing? (add): ")

        if sgn == "add":
            Ans = Defined.add(a, b)
            print(f"The sum of {a} and {b} is {Ans}.")
        elif sgn == "divide":
            Ans = Defined.divide(a, b)
            print(f"the Answer of {a} and {b} divided is {Ans}")
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("It is not possible to divide by zero. Were not the ftc team 9791")
    finally:
        print("Have a good day!")
        break


