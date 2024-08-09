n=int(input("upto which number:"))
num1=0
num2=1
i=0
print(num1,num2,end=' ')
while i<n-2:
    total=num1+num2
    print(total, end=' ')
    num1=num2
    num2=total
    i+=1


