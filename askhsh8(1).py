from collections import Counter

def maxCount(lst):
    count = Counter(lst)
    return max(count.values())

def XOR(str1, str2):
    result = []
    for i in range(max(len(str1), len(str2))):
        xored_value = ord(str1[i % len(str1)]) ^ ord(str2[i % len(str2)])
        result.append(hex(xored_value)[2:])
    return ''.join(result)

def s(m, sbox):
    row = int(m[0] + m[-1], 2)
    col = int(m[1:-1], 2)
    return sbox[row][col]

def DifferentialUniformity(sbox, n, diff=0):
    for x in range(1, n):
        y = []
        for z in range(n):
            y.append(XOR(s(XOR("{0:06b}".format(z), "{0:06b}".format(x)), sbox), s("{0:06b}".format(z), sbox)))
        max_y_count = maxCount(y)
        if max_y_count > diff:
            diff = max_y_count
    return diff



sbox = [["0000","0010","0011","0111","1001","1100","1111","0111","0110","1111","1111","0001","0111","0011","0001","0000"],
        ["0001","0101","0110","1101","0100","0001","0101","1011","0111","1000","0111","0001","0001","0011","0010","1101"],
        ["0101","0011","0101","1100","1011","0001","0001","0101","1101","0000","1111","0111","0010","0010","1101","0000"],
        ["0011","1100","0011","1011","0010","0010","0010","0100","0110","0101","0101","0000","0100","0011","0001","0000"]]

input("Differential Uniformity: " + str(DifferentialUniformity(sbox, 64)))
