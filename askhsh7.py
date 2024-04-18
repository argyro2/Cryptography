import math
def TrialDivision(n):
    L = []
    while n % 2 == 0:
        L.append(2)
        n = n // 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            L.append(f)
            n = n // f
        else:
            f = f + 2
    if n != 1:
        L.append(n)
    return L
def PrimeDiv(n):  
  list = TrialDivision(n)
  for i in list:
    if (n-1) % (i-1)!=0:
      return False
  return True
def SquareFree(n):
  list = TrialDivision(n)
  if(len(set(list)) == len(list)):
    return True
  return False

def is_prime(n):
  for i in range(2,int(math.sqrt(n)+1)):
    if (n%i) == 0:
      return False
  return True
def NextCarmichael(n):
    k = 10**int((int(math.log10(n)+1)/3))
    while True:
        N = (6*k + 1)*(12*k + 1)*(18*k + 1)
         
        if is_prime(6*k + 1) and is_prime(12*k+1) and is_prime(18*k+1):
            if(N>n):
                return N
        k+=1
        
    return None 
n1 = 9999109081
n2 = 6553130926752006031481761
if (PrimeDiv(n1) and SquareFree(n1)):
  print(n1,"is a Carmichael number")
else:
  print(n1,"is not a Carmichael number")
if (PrimeDiv(n2) and SquareFree(n2)):
  print(n2,"is a Carmichael number")  
else:
  print(n2,"is not a Carmichael number")
print("A larger Carmichael number is : ",NextCarmichael(n2))
