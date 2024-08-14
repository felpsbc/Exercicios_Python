import math 

pi = round(math.pi, 2 )

print(f"O valor de PI é {pi}")

rad = float(input("What's the circle radius ? "))

circunference = 2*rad*pi

print(f"The value of circle circunference it's: {round(circunference,2 )} ")

area = 2*pi*math.pow(rad, 2)

print(f"The value of the circle area it's: {area}")