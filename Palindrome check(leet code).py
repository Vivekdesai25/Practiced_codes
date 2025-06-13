import math
def rev(n):
    num=0
    while n>0:
        rem=n%10
        num=num*10+rem
        #math.ceil(n/10)
        n=n//10
    return num
        
n=int(input("en no"))
if(n==rev(n)):
    print("wow ,its palindrome")
else:
    print('Oh its not palindrome')
    
