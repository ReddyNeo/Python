num = int(input("Enter Number : "))
factorial = 1
if num < 0:
    print("Enter Positive Number")
elif num == 0:
    print("Factorial is = 1 ")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)
