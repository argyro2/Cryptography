import math
import time
gamma =  0.577
 
def sumOfDivisors(n):   
 c=round(math.sqrt(n)) 
 list = []    
 for i in range(2,c+1):
     if n%i==0:
         list.append(i)
         list.append(n//i)
 return list 
         

def experiment():
  count =0
  m = 0
  for n in range(3, 2**20, 2):
   m+=1
   s =sum(sumOfDivisors(n))/n 
   a = math.exp(gamma) / 2
   b = math.log(math.log(n))
   c = 0.74/(math.log(math.log(n)))
   if (s<a*b +c):
     count+=1
  if (count == m):
    result = "true"
  else:
     result = "false"
  
  return result
    
start = time.time()

print("Status : ",experiment(),"\nExecution Time : ",time.time()-start,"seconds")


