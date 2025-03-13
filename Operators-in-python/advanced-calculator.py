num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator = input("Enter Operator (+, -, *, /, %, //, **, &, |, ^, ~, <<, >>, ==, !=, <, >, <=, >=) ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error! Division by zero."
elif operator == "%":
    result = num1 % num2
elif operator == "//":
    result = num1 // num2
elif operator == "":
    result = num1 ** num2
elif operator == "&":
    result = num1 & num2
elif operator == "|":
    result = num1 | num2
elif operator == "^":
    result = num1 ^ num2
elif operator == ">>":
    result = num1 >> num2
elif operator == "<<":
    result = num1 << num2
elif operator == "==":
    result = num1 == num2
elif operator == "!=":
    result = num1 != num2
elif operator == ">":
    result = num1 > num2
elif operator == "<":
    result = num1 < num2
elif operator == ">=":
    result = num1 >= num2
elif operator == "<=":
    result = num1 <= num2
else:
    result = "Invalid operator!"

print(f"Result: {result}")