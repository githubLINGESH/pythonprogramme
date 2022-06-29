arr=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
      
print(arr)
for i in arr:
    if(i%5==0):
        print(i)
