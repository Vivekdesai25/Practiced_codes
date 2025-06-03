import math
n=int(input("en no1  "))
n1=int(input("en no2 "))
i=max(n,n1)
while True:
    if(i%n==0 and i%n1==0):
        print ("LCM ",i)
        break
    i+=1
LCM=(n*n1)/math.gcd(n,n1)
print("lCM of given numbers",LCM)
