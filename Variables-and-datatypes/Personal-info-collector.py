name = input("Name: ")
age = int(input("Age: ")) #converting the string into integer
height = float(input("Height: "))
is_student = input("Are You a Student? (yes/No): ").lower() == "yes"

# printing and saving the collected information into a file
info = f"""
print("\n Personal Information summary")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Student: {is_student}")
"""
print(info)
with open("manu_info.txt","w") as file:
    file.write(info)
    print("Information collected succesfully in 'manu_info.txt'.")