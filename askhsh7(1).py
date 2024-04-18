def rc4(key, plaintext):
    S = list(range(256))
    j = 0
    out = []

    #κανει το Key scheduling 
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        temp = S[j]
        S[j] = S[i]
        S[i] = temp

    # Κανει το stream generation
    i = 0 
    j = 0
    for byte in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        temp = S[j]
        S[j] = S[i]
        S[i] = temp
        out.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(out)


key = b'HOUSE' #τα κάνει binary strings to b
plaintext = b'MISTAKESAREASSERIOUSASTHERESULTSTHEYCAUSE'
encrypted = rc4(key, plaintext).hex()
print("Encrypted message : ",encrypted)  
decrypted = rc4(key, bytes.fromhex(encrypted))
print("Decrypted Message :",decrypted.decode('utf-8'))  