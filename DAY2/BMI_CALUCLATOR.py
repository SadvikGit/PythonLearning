#BMI CALUCLATOR
print("***WELCOME TO BMI CALUCLATOR***")
weight=int(input("Enter Your Weight(kgs): "))
height=float(input("Enter Your Height(m): "))
BMI=weight/height**2
print(f"your BMI is {BMI}")
if BMI>=18.5:
    if BMI<25:
        print("Normal Weight")
    else:
        print("Over Weight")
else:
    print("Under Weight")