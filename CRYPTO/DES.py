from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad,pad
from Crypto.Random import get_random_bytes

def encrypt_file(ifp,ofp,key,iv):
    cipher = DES.new(key,DES.MODE_CBC,iv)
    with open(ifp,"rb") as file:
            
        data   = file.read()

    #first pad then encrypt
    padded_data = pad(data,DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    with open(ofp,"wb") as file:
        file.write(iv)
        file.write(encrypted_data)
def decrypt_file(ifp,ofp,key,iv):
    with open(ifp,"rb") as file:
        iv = file.read(8)
        data=file.read()
    cipher = DES.new(key,DES.MODE_CBC,iv)
    #first decrypt then unpad
    decrypted_padded_data = cipher.decrypt(data)
    decrypted_data = unpad(decrypted_padded_data,DES.block_size)
    with open(ofp,"wb") as file:
        file.write(decrypted_data)

key = get_random_bytes(8)
iv = get_random_bytes(8)
encrypt_file("input.txt","encrypted2.bin",key,iv)
print("File encrypted and saved ")
decrypt_file("encrypted2.bin","de2c.txt",key,iv)
print("file decrypted and saved")
