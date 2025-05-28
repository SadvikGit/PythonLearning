import random
print("***Lets Find Who Will Pay The Bill Today***")
friends=["Prabhas" , "vijay Deverakonda" , "Hrithik Roshan ", "Sandeep Reddy Vanga", "Mahesh Babu" , "Cr7" ]
num = len(friends)
random_number =  random.randint(0,num+1)
print(f"{friends[random_number]} Will Pay The Bill Today.")
