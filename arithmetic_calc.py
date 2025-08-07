a=int(input("enter first number: "))
b=int(input("enter second number: "))

print("=======================================")

print(" + -> for addition ")
print(" - -> for subtraction ")
print(" * -> for multiplication ")
print(" / -> for division ")

print("=======================================")

choice=input("enter arithmetic operation to be performed: ")

while True:
    if choice == "+":
        print(a, choice, b, "=", a+b)
    elif choice == "-":
        print(a, choice, b, "=", a-b)
    elif choice == "*":
        print(a, choice, b, "=", a*b)
    elif choice == "/":
        if b==0:
            print("division by zero cannot be performed!!")
        else:
            print(a, choice, b, "=", a/b)
    else:
        print("invalid choice of arithmetic operator!!!")

    break

print("=======================================")

print("End of the program!")



