print("*****Welcome To Python pizza Deliveries*****")
size=input("What Size Of Pizza You Need (S , M , L) ?: ").lower()
Cheese =str(input("You want Extra Cheese (Y or N)? :")).lower()
bill = 0
if size == "s":
    bill +=15
elif size == "m":
    bill += 20
elif size=="l":
    bill += 25
else:
    print("You Entered Wrong Size")

pepperoni = input("Do You Need Pepperoni (Y Or N)? :").lower()
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if Cheese == "y":
    bill += 1
print(f"your Total bill is:${bill}")