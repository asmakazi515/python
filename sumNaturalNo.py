#sum of natural number upto n:
num=int(input("enter number upto you want to sum:"))
sum=0
while num>0:
    if num%2!=0:
        sum=sum+num
    num-=1

print("sum is",sum)
     