name = input("Name: ")
age = int(input("Age: ")) #converting the string into integer
height = float(input("Height: "))
Is_student = input("yes").lower() == "yes"

# printing the collected information below
print("\n Personal Information summary")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Student: {Is_student}")