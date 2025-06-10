n=6
for i in range (0,n+1):
  print(" "*(n-i),end="")
  k=1
  for j in range (0,i+1):
    print(k," ",end="")
    k=k*(i-j)//(j+1)
    import math

'''
value = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))  

nCr or import fact function from math
print(value, end=" ")
1 
121 
1331
14641 ...
'''
        
