# Program to demonstrate cryptanalysis of shift cipher

import math 
# cipertext =  Pievrmrk Gvctxskvtle
def cryptoanalysis():
    ct=input("enter a ciper text for cryptoanalysis: ")
  
    for k in range(26):
        pt = " " 
        for i in range(len(ct)):
            if ct[i] == " ":
                pt+=" "
            elif ct[i].isupper():
                ci = ord(ct[i])-65
                ei = (ci-k)%26
                pt += chr(ei+65) 
            else:
                ci = ord(ct[i])-97
                ei = (ci-k)%26
                pt += chr(ei+97)  
        print(f" For key = {k}, plain text = {pt}")

cryptoanalysis()