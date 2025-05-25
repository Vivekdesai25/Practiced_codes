n=int(input (" enter no ")
original=n
pow=len(str(n))
res=0
while n>0:
  n=n%10
  res=res+(n**pow)
  n//=10
print ("Armstrong" if res==original else "not Armstrong" )
