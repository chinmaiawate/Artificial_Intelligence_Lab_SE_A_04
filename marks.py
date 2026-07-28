n1=int(input("enter first subject marks:"))
n2=int(input("enter second subject marks:"))
n3=int(input("enter third subject marks:"))
n4=int(input("enter fourth subject marks:"))
n5=int(input("enter fifth subject marks:"))
avg=(n1+n2+n3+n4+n5)/5
print(avg)
if avg>=90 and avg<100:
 print("first class\n")
elif avg>=70:
 print("second class\n")
elif avg>=50:
 print(" distinction\n")
elif avg>=35:
 print("pass\n")
else:
 print("fail\n")

