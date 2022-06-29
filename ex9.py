a=int(input("enter a number: "))
b=int(input("enter a number: "))
for j in range(a,b):
    n=j
    sum=0
    num=n
    while(n>0):
        rem=n%10
        sum=sum+(rem**3)
        z=int(n)/10
        n=int(z)
    if(sum==num):
        print(sum,"is a amstrong no")   
