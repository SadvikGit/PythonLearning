student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
maxx =0
for i in student_scores :
    if  i >= maxx:
        maxx=i
print(f"The Highest Score Among Given list is {maxx} .")