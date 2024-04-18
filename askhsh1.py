g=3
p=101
a=77
b=91
def FastPower(B,e,m):
  result=1
  while (e>0) :
    if e%2==1 :
      result = (result * B) % m
    e=e//2
    B=(B**2)%m
  return result
A = FastPower(g,a,p)
B = FastPower(g,b,p)
print("Alice's Key : ",A)
print("Bob's Key : ",B)
key1 = FastPower(A,b,p)
key2 = FastPower(B,a,p)
if(key1 == key2):
  print("The key is valid \nKey : 66")
else:
  print("The key is invalid")
