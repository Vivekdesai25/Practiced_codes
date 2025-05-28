n=6
for i in range (1,n+1):
    print(" "*(n-i),end="")
    for j in range (1,i+1):
        print(chr(j+96),"",end="")
    print()
for i in range (n,0,-1):
    print(" "*(n-i),end="")
    for j in range (1,i+1):
        print(chr(j+47),"",end="")
    print()
    ------
    a-97
    A-65
    0-48
    ----
