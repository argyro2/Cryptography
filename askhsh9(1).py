from Crypto.Cipher import AES
import os

def GeneratePairs(num_pairs):
    pairs = []
    for i in range(num_pairs):
        m1 = os.urandom(32)
        m2 = bytearray(m1)
        m2[0] ^= 1
        pairs.append((m1, m2))
    return pairs

def DiffBitsCount(b1, b2):
    diff = 0
    for i in range(len(b1)):
        diff += bin(b1[i] ^ b2[i]).count('1')
    return diff
  

def AvalancheTest(name, iv=None):
    cipher = AES.new(os.urandom(16), AES.MODE_CBC, iv)
    if iv is None:
      cipher = AES.new(os.urandom(16), AES.MODE_ECB)
    p = int(input("Enter number of message pairs : "))
    pairs = GeneratePairs(p)
  
    for m1, m2 in pairs:
        c1 = cipher.encrypt(m1)
        c2 = cipher.encrypt(m2)
        DiffBits = DiffBitsCount(c1, c2)
        percent_diff = (DiffBits / (len(m1) * 8)) * 100
        print(f"{name}: {DiffBits} bits differ for this pair of messages")
        
        print(f"{name}: {percent_diff:.2f}% of bits differ for this pair of messages")

AvalancheTest("AES-128 ECB")
AvalancheTest("AES-128 CBC", os.urandom(16))
