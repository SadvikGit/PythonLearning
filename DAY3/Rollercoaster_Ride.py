print("*** Welcome to My RollerCoaster Ride ***")
height = int(input("Enter Your Height in (cm) : "))
bill = 0 
if height >= 120:
    age=int(input("Enter your Age:"))

    if age <= 12:
        bill += 5
        print("\nYes,You Can Go For The Ride.Price Of Ticket is $5")
    
    elif age <= 18:
        bill += 7
        print("\nYes,You Can Go For The Ride.Price Of Ticket is $7")
        
    else:
        bill += 12
        print("\nYes,You Can Go For The Ride.Price Of Ticket is $12")
    
    photo = str(input("You Need A Photo (y/n) :")).lower()
    if photo == "y":
        bill += 3
    print(f"\nYour Total Bill Is ${bill}. \nThank You Have A Safe And Great Ride!!")


else:
    print("**SORRY!!NOT ALLOWED** \nYou Need To Grow taller Before Entering a Ride.")