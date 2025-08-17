num=int(input("Please Enter decimal no "))


def bi(n):
  bi="" #empty string 
  if n==0:
    return "0"
  while n>0:
    bi=str(n%2)+bi
    n//=2
  return bi
k=bi(num)
print (k)
print ()

#inbuilt functions
print ("binary inbuilt fun ",bin(num)[2:])
print ("formate inbuilt fun ",format(num,'b'))
print (f"fstring binary {num :b} ")
