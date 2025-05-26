num=int(input("Enter a range from 0 to ? :\n"))
# count = 0
prime_numbers = []

print(f"prime numbers from 0 to {num} :\n")
for i  in range(2,num+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        # count += 1
        prime_numbers.append(i)
        #print(i)
print(prime_numbers)

print(f"\n Total prime numbers from 0 to {num} are {len(prime_numbers)}")
