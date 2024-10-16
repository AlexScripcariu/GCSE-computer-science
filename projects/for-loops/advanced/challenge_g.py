num = 51
while num not in range(0, 51):
    num = int(input("Please enter a number between 1-50: "))

for i in range(num, -1, -1):
    print(i)