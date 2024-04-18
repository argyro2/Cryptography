import math
import time
import random

def F(b,m):
  x=b**2 + 1
  return x%n


def pollard(n):
     
      x = (random.randint(0, 2) % (n - 2))
      y = x
      d = 1
      while d==1 :
        x = F(x,n)
        y = F(F(y,n),n)
        diff = abs(x-y)
        d = math.gcd(diff,n)
        if d==n:
          return pollard(n)    
      return d

start = time.time()
n = 2**257 - 1
print("One of the divisors for", n , "is ",pollard(n),"\nExecution Time :",(time.time()-start)/60,"minutes")
