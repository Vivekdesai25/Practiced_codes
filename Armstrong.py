n=int(input ("Enter any random no "))
original=n
pow=len(str(n))
res=0
while n>0:
  m=n%10
  res=res+(m**pow)
  n//=10
print ("Armstrong" if res==original else "not Armstrong" )

''' 
for i in range(1, 1000):
    if function (i):
        print(i)
        
Armstrong no 153,370,371,9474...
example  153 =1³+5³+3³
'''
