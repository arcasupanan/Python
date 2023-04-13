

"""
Codecademy - Learn Python
Area Calculator
"""

print("Starting the calculator")

name = input("What's your name? ")
option = input("Enter C for Circle or T for Triangle: ")
if option == 'C':
    radius = float(input("Enter radius: "))
    area = 3.14159 * radius ** 2
    print("Area %f" % area)
elif option == 'T':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area %f" % area)
else:
    print("Error! Invalid shape.")
print("Exiting the Area Calulator")
