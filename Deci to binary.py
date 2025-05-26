num=int(input("Enter decimal no "))

def bi(n):
  bi=""
  if n==0:
    return "0"
  while n>0:
    bi=str(n%2)+bi
    n//=2
  return bi
k=bi(num)
print (k)
print ()
print ("binary inbuilt fun ",bin(num)[2:])
print ("formate inbuilt fun ",format(num,'b'))
print (f"fstring binary {num :b} ")
