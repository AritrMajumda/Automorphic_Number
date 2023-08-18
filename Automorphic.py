n=int(input("enter the number "))
n1=n*n
n2=n1
n3=n1
k=0
c=0
k1=0
c1=-1
while n2>0:
    s=int(n2%10)
    k=k+1
    n2=int(n2/10)
while n3>0:
    s1=int(n3%10)
    c1=c1+1
    k1=k1+(s1*(10**c1))
    if(k1==n):
       c=c+1
    n3=int(n3/10)
if(c==1):
    print("automorphic")
else:
    print("not automorphic")