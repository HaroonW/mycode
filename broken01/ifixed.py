#!usr/bin/python3

calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != "q"):
    print("\nwhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    calc1 = calc1.upper()
    if calc1 == "Q":
        break
    calc1 = float(calc1)
    print("\nwhat is the second operator? or, enter q to quit: ")
    calc2 = input()
    calc2 = calc2.upper()
    if calc2 == "Q":
        break
    calc2 = float(calc2)
    print("enter n operation to perform on the two operator (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 - calc2))
    else: 
        print("\n not a valid entry. restarting...")
