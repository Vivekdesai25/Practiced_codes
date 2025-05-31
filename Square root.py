import math 
a=float(input("en value a "))
b=float (input("en value b "))
c=float(input("en value c "))

k=(b**2 - 4*a*c)
z=math.sqrt(k)#pow(k,0.5)

r1=(-b+z)/(2*a)
r2=(-b-z)/(2*a)
print("The roots of the quadratic equation are:", r1, "and", r2)
