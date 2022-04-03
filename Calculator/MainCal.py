from Calculator import Calculator

Operator = input("Enter your operator E.g (Add,Sub,Mul,Div,All)")
Val1 = int(input("Enter First Value: "))
Val2 = int(input("Enter Second Value: "))

cal = Calculator()
if Operator == "Add":
    print("=======================")
    cal.addition(Val1,Val2)
   # print("Result: ",cal.addition(Val1,Val2))
elif Operator == "Sub":
    print("=======================")
    cal.subtraction(Val1,Val2)
elif Operator == "Mul":
    print("=======================")
    cal.Multiply(Val1, Val2)
    #print("Result: ",cal.subtraction())
elif Operator == "Div":
    print("=======================")
    cal.division(Val1,Val2)
elif Operator == "All":
    print("=======================")
    cal.addition(Val1, Val2)
    cal.subtraction(Val1, Val2)
    cal.Multiply(Val1, Val2)
    cal.division(Val1, Val2)
    print("=======================")
else:
    print("Sorry your operator is not Found")





