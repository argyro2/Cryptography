import time
def FastPower(B,e,m):
  result=1
  while (e>0) :
    if e%2==1 :
      result = result * B % m
    e=e//2
    B=(B**2)%m
  return result
b=5
e=77
m=19
res = FastPower(b,e,m)
start = time.time()
print(5**77,"mod 19 =",res)
