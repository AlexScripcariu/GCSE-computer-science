name = input("Please enter your name: ")
num = 0
try:
    num = int(input("Please enter a number: "))
except ValueError:
    print("Please enter a number next time!")

for i in range(num):
    print(name)