def leap(a):
    if(a%4==0 and a%100 != 0) or a%400==0:
        return True
    else:
        return False
        
a=int(input("Enter any year "))
r=leap(a)
print("leap year ? ",r)
