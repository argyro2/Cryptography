import signal
import math
import random
import time

def TimeoutHandler(signum, frame):
    raise TimeoutError("Function timed out")

def Lehman(n):
    for k in range(1,math.floor(math.pow(n, 1/3))):
        for a in range(math.ceil(math.sqrt(abs(4 * k * n))), math.floor(math.sqrt(abs(4 * k * n)) + (n ** (1 / 6) / (4 * math.sqrt(k))))):
            b = math.sqrt(abs(a ** 2 - 4 * k * n))
            if isinstance(b, int):
                return math.gcd(a - b, n)
    return 0

def GenerateRandomOdd():
    num = random.getrandbits(99)
    num |= 1 << 99
    num |= 1
    return num



timeout_seconds = 10


success_count = 0
total_count = 0
start = time.time()
print(GenerateRandomOdd())
'''
for i in range(1000):
    
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    # Cancel the timeout signal if the function completes within the time limit
    try:
        result = Lehman(int(GenerateRandomOdd))
        signal.alarm(0)
    except TimeoutError:
        pass


success_percentage = (success_count / 1000) * 100

print("Successful runs:", success_count)
print("Total runs:", total_count)
print("Success percentage:", success_percentage)
print("Execution Time:",(time.time()-start)/60,"minutes")
'''
