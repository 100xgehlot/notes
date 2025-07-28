# Aim: Program to demonstrate  cryptoanalysis of affine cipher

def decrypt():
    cl = "nktauv"
    #find modular inverse of a
    ainv = 0
    for a in [2,3,5,7,9,11,13,15,17,19,23]:
        for i in range(26):
            if ((a*i)%26)==1:
                ainv = i
        for b in range(26):
            pt = ""
            for i in range(len(cl)):
                if cl[i] == " ":
                    pt+=" "
                if cl[i].isupper():
                    ci = ord(cl[i])-65
                    pi = (ainv*(ci-b))%26
                    pt += chr(pi+65)
                else:
                    ci = ord(cl[i])-97
                    pi = (ainv*(ci-b))%26
                    pt += chr(pi+97)
            print(f"For KEY-A: {a} and KEY-B: {b} is : {pt}")
    
    


decrypt()


