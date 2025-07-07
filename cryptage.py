from numpy import array

DN = str(input("date  "))

M = array([[None for _ in range(4)] for _ in range(4)])

def remplirM(M):
    for i in range(4):
        for j in range(4):
            val = str(input(" 0..9 / A..F "))
            while not ("0" <= val <= "9" or "A" <= val <= "F") or val in M:
                val = str(input(" 0..9 / A..F "))
            M[i][j] = val

def Decimal_hex(N):
    N = int(N)
    if N == 0:
        return "0"
    ch = ""
    while N > 0:
        r = N % 16
        if r <= 9:
            ch = str(r) + ch
        else:
            ch = chr(55 + r) + ch
        N = N // 16
    return ch

def DNHex(DN):
    res = ""
    DN = DN + "/"
    while "/" in DN:
        ch = DN[0: DN.find("/")]
        res = res + Decimal_hex(ch) + "/"
        DN = DN[DN.find("/") + 1:]
    return res[0: len(res)-1]

def Crypter(DN, M):
    DN = DNHex(DN)
    res = ""
    for i in range(len(DN)):
        if DN[i] != "/":
            res = res + str(Mat(DN[i], M))
        else:
            res = res + "/"
    return res

def Mat(c, M):
    for i in range(4):
        for j in range(4):
            if c == M[i][j]:
                if "A" <= c <= "F":
                    cod = (j + 87) - ord(c)
                else:
                    cod = (i + 87) - int(c)
                if "A" <= chr(cod) <= "Z":
                    return chr(cod)
                else:
                    return int(cod)

remplirM(M)
print(Crypter(DN, M))
