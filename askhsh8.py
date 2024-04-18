import time
import random
 

def calc(b, e, n):
    result = 1
    b = b%n   
    while e>0:
        if e % 2:
            result = (result*b)%n
            e = e-1
        else:
            b = (b**2)%n      
            e = e//2           
    return result%n


def Fermat(n,k):
        for i in range(k):
            p = random.randint(2, n - 2)
            if calc(p,n-1,n) != 1:
                return False             
        return True
    
#https://www.geeksforgeeks.org/fast-exponentiation-in-python/
def optimize(val, power):
    result = pow(val, power//2)
    result = result * result
    if power % 2 != 0:
        result = result * val
    return result
 

def multiply(x,n,d):
    return x * optimize(n,d)             
k = int(input("Give number of iterations : \n"))
start = time.time()

print("Status for Fermat primality for 835335 * 2^39014 - 1 :",Fermat(multiply(835335,2,39014)-1, k),"\nExecution Time for 835335 * 2^39014 - 1 :",(time.time()-start)/60,"minutes")
start = time.time()
print("Status for Fermat primality for 835335 * 2^39014 + 1 :",Fermat(multiply(835335,2,39014)+1, k),"\nExecution Time for 835335 * 2^39014)+ 1 :",(time.time()-start)/60,"minutes")
