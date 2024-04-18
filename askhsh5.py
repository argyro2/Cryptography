import random
 
my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R' , 'S', 'T', 'U' , 'V', 'W', 'X', 'Y', 'Z', '.', '!', '?', '(', ')', '-']
def decimalToBinary(n: int) -> str:
    
    return bin(n)[2:].zfill(5)

def binaryToDecimal(binary: str) -> int:
    
    return int(binary, 2)


def CreateKey(length: int) -> str:
   
    return ''.join(str(random.randint(0, 1)) for _ in range(length))


def messageToBinary(msg):
    result = ""
    for char in msg:
        result += decimalToBinary(my_list.index(char))
    return result

#(source : https://stackoverflow.com/questions/36242887/how-to-xor-two-strings-in-python)   k
def XOR(str1, str2):
    result = []
    for i in range(max(len(str1), len(str2))):
        xored_value = ord(str1[i%len(str1)]) ^ ord(str2[i%len(str2)])
        result.append(hex(xored_value)[2:])
    return ''.join(result)

def binaryToMessage(xor):
    result = ""
    temp = ""
    for char in xor:
        temp+=char
        if len(temp) == 5:
            result += my_list[int(binaryToDecimal(temp))]
            temp = ""
    return result


def encrypt(msg, key) :
    
    binary = messageToBinary(msg)
    xor = XOR(binary, key)
    return binaryToMessage(xor)

def decrypt(msg,key):
  binary = messageToBinary(msg)
  msg = XOR(binary, key)
  return binaryToMessage(msg)
msg = input("Give message : ")
binary = messageToBinary(msg)
key = CreateKey(len(msg)*5)
#print("binary = ", binary)
#print("key = ", key)
print("Encrypted message =", encrypt(msg,key))
encrypted_msg=encrypt(msg,key)
print("Original message = ", decrypt(encrypted_msg,key))
