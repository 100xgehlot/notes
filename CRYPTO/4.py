# Aim: Program to demonstrate implementation of affine cipher
def encrypt(pl,a,b):
    ct = ""
    for i in range(len(pl)):
        if pl[i] == " ":
            ct+=" "
        if pl[i].isupper():
            pi = ord(pl[i])-65
            ci = (a*pi+b)%26
            ct +=chr(ci+65)
        else:
            pi = ord(pl[i])-97
            ci = (a*pi+b)%26
            ct+= chr(ci+97)
        print(ct)
    return ct
def decrypt(cl,a,b):
    pt = ""
    #find modular inverse of a
    ainv = 0
    for i in range(26):
        if ((a*i)%26)==1:
            ainv = i
    for i in range(len(cl)):
        if cl[i] == " ":
            pl+=" "
        if cl[i].isupper():
            ci = ord(cl[i])-65
            pi = (ainv*(ci-b))%26
            pt += chr(pi+65)
        else:
            ci = ord(cl[i])-97
            pi = (ainv*(ci-b))%26
            pt += chr(pi+97)
    return pt
    

pl = input("Enter a plain text: ")
a = int(input("Enter a KEY A: "))
b = int(input("Enter a KEY B: "))
enc = encrypt(pl,a,b)
print(pl+" encrypted form is: "+enc)
dec = decrypt(enc,a,b)
print(enc+" decrypted form is: "+dec)


