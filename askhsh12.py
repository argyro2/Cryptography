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

def phi(p, q):
    return (p - 1) * (q - 1)

N = 11413
e = 19


factors = TrialDivision(N)
p = factors[0]
q = factors[1]


phi = phi(p, q)

print("p:", p)
print("q:", q)
print("φ(N):", phi)
def inverse(a, m):
    g, x, y = ExtendedGCD(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m

def ExtendedGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ExtendedGCD(b, a % b)
    return g, y, x - (a // b) * y

def decipher(ciphertext, d, N):
    plaintext = ""
    for c in ciphertext:
        m = pow(c, d, N)
        plaintext += chr(m)
    return plaintext

N = 11413
e = 19
ciphertext = [3203, 909, 3143, 5255, 5343, 3203, 909, 9958, 5278, 5343, 9958, 5278, 4674, 909, 9958, 792, 909, 4132,3143, 9958, 3203, 5343, 792, 3143, 4443]


d = inverse(e,phi)

plaintext = decipher(ciphertext, d, N)

print("Private key (d):", d)
print("Decrypted message:", plaintext)
