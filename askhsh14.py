def FastPower(B,e,m):
  result=1
  while (e>0) :
    if e%2==1 :
      result = (result * B) % m
    e=e//2
    B=(B**2)%m
  return result
m = 3
s = 301
e = 839
N = 899
a = FastPower(s,e,N)
print("a = ",a)
if a == m:
  print("The signature is valid")
else:
  print("The signature is invalid")
