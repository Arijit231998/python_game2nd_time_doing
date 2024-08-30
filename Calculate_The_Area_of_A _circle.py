import math
def area_of_a_sphere(radius):
    area= 4*math.pi*radius**2
    return area
def volume_of_a_sphere(radius):
    volume = (4/3) * math.pi * radius**3
    return volume
def Diameter_of_a_sphere(radius):
    diameter=2*radius
    return diameter
def area_of_a_circle(radius):
    area=math.pi*radius**2
    return area
def Circumference_of_a_Circle(radius):
    circumference= 2*math.pi*radius
    return circumference
def diameter_of_a_Circle(radius):
    diameter=2*radius
    return diameter
radius=float(input("please insert a  value  with a floating  point:  "))
print("area_of_a_sphere_is:",area_of_a_sphere(radius))
print("volume_of_a_sphere_is:",volume_of_a_sphere(radius))
print("diameter_of_sphere_is:",Diameter_of_a_sphere(radius))
print ("area_of_a_circle_is:",area_of_a_circle(radius))
print("Circumference_of_a_Circle_is:",Circumference_of_a_Circle(radius))
print("diameter_of_a_Circle:",diameter_of_a_Circle(radius))
