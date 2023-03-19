n=10
m=n-2
count=1
for i in range(n,1,-1):
    print(" "*(n-i),end=" ")
    for j in range(i):
        if j==1 or j==i-1:
            print(count,end=" ")            
        else:
            print(" ",end=" ")
    print("\r")
    count+=1
for i in range(3,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        if j==1 or j==i-1:
            print(m,end=" ")
        else:
            print(" ",end=" ")
    print("\r")
    m-=1