import time
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

u = 2**62 - 1
v = 2**102 -1
start = time.time()
print("Prime Factors for",2**62 -1,": ",TrialDivision(u),"\nExecution Time for ",2**62 -1," : ",time.time()-start,"seconds")
print("Prime Factors for ",2**102 -1,":",TrialDivision(v),"\nExecution Time for ",2**102 -1," : ",time.time()-start,"seconds")



