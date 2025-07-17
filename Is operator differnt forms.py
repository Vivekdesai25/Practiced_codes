import sys

a = 100
b = 1000
print(a is 100)       # True (small number up to -5 to 255)
print(a == 100)       # True
print(b is 1000)      # False (large number)

s1 = "ok"
s2 = "ok"
print(s1 is s2)       # True (small string)

l1 = "this is long"
l2 = "this is long"
print(l1 is l2)       # False (large string)

i1 = sys.intern("this is interned")
i2 = sys.intern("this is interned")
print(i1 is i2)       # True (forced interned string)

A=1000
B=A
Print(A is B ) # True
