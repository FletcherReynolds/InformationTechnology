num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
op = input("Enter the operator: ")

if op == "*":
    ans = num1 * num2
elif op == "/":
    ans = num1 / num2
elif op == "-":
    ans = num1 - num2
elif op == "+":
    ans = num1 +num2

print("Answer: ",ans)