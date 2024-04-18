
def XOR(str1, str2):
    result = []
    for i in range(max(len(str1), len(str2))):
        xored_value = ord(str1[i%len(str1)]) ^ ord(str2[i%len(str2)])
        result.append(hex(xored_value)[2:])
    return ''.join(result)

def ShiftLeft(st, a):
    return st[a:] + st[:a]

def decipher(c):
    return XOR(XOR(XOR(XOR(c, ShiftLeft(c, 2)), ShiftLeft(c, -2)), ShiftLeft(c, -4)), ShiftLeft(c, -12))
    
def cipher(m):
    return XOR(XOR(m, ShiftLeft(m, 6)), ShiftLeft(m, 10))


m = '0111001010101011'
c = '0111010110111101'
print(cipher(m))
print(decipher(c))




