print("*****Welcome To TIP Caluclator*****")
Bill_amount=float(input("What's the Bill Amount:$ "))
Num_of_persons=int(input("Number of Persons Attended: "))
Tip = int(input("How Much Tip Would You Like To Give (5%,10%,15%,20%..) ?: "))
Tip_amount= Bill_amount* (Tip/100)
Total_Bill = Tip_amount+Bill_amount
Each_person = float(Total_Bill/Num_of_persons)
print(f"Your FinalBill is ${Total_Bill} & Each Person should Pay ${Each_person}")