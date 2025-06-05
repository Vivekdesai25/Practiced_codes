1 2 4 8 16 32 64 ,,,
n=input("Enter binary no ")
def bi(l):
    p=0
    d=0
    for i in reversed(l):
        if i=='1':
            d=d+2**p
        p+=1
    return d
k=bi(n)
print ("Decimal ",k)
