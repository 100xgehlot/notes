# Program to demonstrate cryptanalysis of shift cipher

import math 
def encrypt_words(pt,key):
    ct=  ""
    n = len(pt)
    val = math.ceil(n/len(key))
    key  = key*val
    for i in range(n):
        if pt[i] == " ":
            ct+=" "
        elif pt[i].isupper():
            pi = ord(pt[i])-65
            ki = ord(key[i])-65
            ei = (pi+ki)%26
            ct += chr(ei+65)    
        else:
            pi = ord(pt[i])-97
            ki = ord(key[i])-97
            ei = (pi+ki)%26
            ct += chr(ei+97)  
    return ct


def decrypt_words(ct,key):
    pt=  ""
    n = len(ct)
    val = math.ceil(n/len(key))
    key  = key*val
    for i in range(n):
        if ct[i] == " ":
            pt+=" "
        elif ct[i].isupper():
            ci = ord(ct[i])-65
            ki = ord(key[i])-65
            ei = (ci-ki)%26
            pt += chr(ei+65) 
        else:
            ci = ord(ct[i])-97
            ki = ord(key[i])-97
            ei = (ci-ki)%26
            pt += chr(ei+97)  

    return pt

plain_text = input("Enter a text: ")
key  = input("Enter a key: ")
enc = encrypt_words(plain_text,key)
print(enc)
print(decrypt_words(enc,key))