num1=239
num2=799999
def cary(n1,n2):
  a,b,c,x=0,0,0,0
  
  carry=0
  while n1>0 or n2>0:
    a= n1 %10
    b= n2 %10
    c=a+b+carry
    if c>9:
      x+=1
      carry=1
    else:
      carry=0
      
    
    n2//=10
    n1//=10
    
  return x
print(cary(num1,num2))
