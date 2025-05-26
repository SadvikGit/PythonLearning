num = int(input("Enter a Number :"))
if num <= 1:
    print(f"{num} is not a Prime number")
elif num == 2:
    print(f"{num} is a prime number")
elif num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            print(f"{i} is a factorial of {num}")
            break
    else:
        print(f'{num} is a prime number')