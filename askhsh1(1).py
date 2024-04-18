
def LetterToNumber(c):
    if ord(c) < 962:
        return ord(c) - 944
    return ord(c) - 945


def NumberToLetter(n):
    if n < 18:
        return chr(int(n) + 944)
    return chr(int(n) + 945)


def f(x):
    return x**5 + 3*x**3 + 7*x**2 + 3*x**4 + 5*x + 4


def FindM(c, x0):
    m = [(LetterToNumber(char) - f(x0)) % 24 + 1 for char in c]
    return [NumberToLetter(num) for num in m]


def BruteForce(c):
    for i in range(24):
        m = [(LetterToNumber(char) + i) % 24 + 1 for char in c]
        PrintString([NumberToLetter(num) for num in m])


def PrintString(list):
    print("".join(list))

x0 = (-3 - 5**(1/2))/2
PrintString(FindM('οκηθμφδζθγοθχυκχσφθμφμχγ', x0))
