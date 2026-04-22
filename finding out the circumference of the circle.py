#Making a program to create a python function to figure out the circumference of the circle

radius = int(input("Enter the radius of the circle: "))
pi = 3.14
def circumference(radius) :
    result = 2 * pi * radius
    return result

print("The circumference of the circle is", circumference(radius))