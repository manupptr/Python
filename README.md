# This Repository is used to showcase my day to day practice on Python-Core

## Introduction to python

**Executing the program by inserting the below code into the file named hello.py**
```
print("Hello Manu!")
```
**Output:** Hello Manu!

**Practicing the own python codes**
```
print("Hello Manu!")
Print("How Are You?")
```
**Output:** Hello Manu!
        How Are You?

```
if 10 > 5:
print("10 is greater than 5")
```
**Output:** 10 is greater than 5

**Creating and Executing the python intro message**
```
name = ("Manu")
state = ("Andhra pradesh")
print("\n")
print("we are welcoming you")
print(f"Hello, {name}! It's great to hear that you are from {state}.")
print("Let's start exploring together!")
```
**Output:**

we are welcoming you

Hello, Manu! It's great to hear that you are from Andhra pradesh.

Let's start exploring together!


## Variables and DataTypes

**Personal Information Collecting project**
Creating the Personal-info-collector.py and adding the below code into the file
```
name = input("Name: ")
age = int(input("Age: ")) #converting the string into integer
height = float(input("Height: "))
is_student = input("Are You a Student? (yes/No): ").lower() == "yes"

# printing the collected information below
print("\n Personal Information summary")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Student: {is_student}")
```
Output:
Name: Manu

Age: 24

Height: 1.75

Are You a Student? (yes/No): yes


 Personal Information summary

Name: Manu

Age: 24

Height: 1.75 meters

Student: True


**Created an Advanced Calculator Using Input/Output, Type Conversion, f-strings, Conditional Statements, Arithmetic Operators (+, -, *, /, %, //, **), Bitwise Operators (&, |, ^, <<, >>), Comparison Operators (==, !=, >, <, >=, <=), Error Handling (Division by Zero), Edge Case Handling (Invalid Operator), Logical Conditions, Bug Fixing (Exponentiation Operator Correction)**

```
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator = input("Enter Operator (+, -, *, /, %, //, **, &, |, ^, ~, <<, >>, ==, !=, <, >, <=, >=): ")

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
```
**Output:**
Enter First Number: 125
Enter Second Number: 126
Enter Operator (+, -, *, /, %, //, **, &, |, ^, ~, <<, >>, ==, !=, <, >, <=, >=): &
Result: 124