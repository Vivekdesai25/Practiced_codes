def gcd(a,b):
  if(b==0):
    return a
  return gcd(b,a%b)
a=int(input ("en 1st no "))
b=int(input("en 2nd no "))
r=gcd(a,b)
print("GCD is ",r)
