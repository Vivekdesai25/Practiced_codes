# A superior element in an array is one that is greater than all elements to its right.
# The rightmost element is always superior.


n=int(input("enter no of elements\n"))
a=[]

element=input("en element\n").split(',')
for i in range(n):
  a.append(int(element[i]))
# a=[1,8,5,0,6]
sup=float('-inf')
c=0
for i in range(len(a)-1,-1,-1):
  if a[i]>sup:
    c+=1
    sup=a[i]
    
print(c)
