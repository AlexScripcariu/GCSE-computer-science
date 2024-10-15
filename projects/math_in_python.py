import math

# # challenge 28
# num = float(input("Enter a number with a lot of decimal places: "))
# num *= 2
# print(num)

# # challenge 29
# num = 0
# while num < 500:
#     num = int(input("Please enter a number over 500: "))

# num = num ** 0.5

# print(round(num, 2))

# # challenge 30 
# print(round(math.pi, 2))

# # challenge 31
# radius = int(input("Please enter the radius of a circle: "))

# area = math.pi * (radius ** 2)
# print(area)

# # challenge 32

# depth = int(input("How deep is the cylinder: "))
# print(round(area * depth, 3))

# # challenge 33
# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter another number: "))

# int_div = num1 // num2 
# rem = num1 % num2
# print(f"""{num1} integer division {num2} is {int_div} and \
#       its modulo is {rem}""")

# # challenge 34

options = ["square", "triangle"]
selected = -1
while selected != -1:
    for i,v in enumerate(options):
        print(f"{i + 1}) {v.title()}")
    selected = int(input("Please enter one of the options"))
    if not(1 <= selected <= len(options)):
        continue
    elif selected == 1:
        pass
    elif selected == 2:
        pass
