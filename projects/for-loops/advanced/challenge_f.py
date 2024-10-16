num = 0
while num not in range(1, 13):
    num = int(input("Please enter a number between 1-12: "))


for i in range(1, 13):
    print(i * num)