import math

opp = input("Enter an operator:")
num1 = float(input("Enter the 1st no:"))
num2 = float(input("Enter the 2nd no:"))


if opp == "+":
    result = num1+num2
    print(f"ans{result}")
elif opp =="-":
    result = num1-num2
    print(f"ans{result}")
elif opp =="*":
    result = num1*num2
    print(f"ans{result}")
elif opp =="/":
    result = num1/num2
    print(f"ans:{round(result,2)}")


