from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad,pad
from Crypto.Random import get_random_bytes

def encrypt_file(ifp,ofp,key,iv):
    cipher = AES.new(key,AES.MODE_CBC,iv)
    with open(ifp,"rb") as file:
            
        data   = file.read()

    #first pad then encrypt
    padded_data = pad(data,AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    with open(ofp,"wb") as file:
        file.write(iv)
        file.write(encrypted_data)
def decrypt_file(ifp,ofp,key,iv):
    with open(ifp,"rb") as file:
        iv = file.read(16)
        data=file.read()
    cipher = AES.new(key,AES.MODE_CBC,iv)
    #first decrypt then unpad
    decrypted_padded_data = cipher.decrypt(data)
    decrypted_data = unpad(decrypted_padded_data,AES.block_size)
    with open(ofp,"wb") as file:
        file.write(decrypted_data)

key = get_random_bytes(16)
iv = get_random_bytes(16)
encrypt_file("input.txt","encrypted.bin",key,iv)
print("File encrypted and saved ")
decrypt_file("encrypted.bin","dec.txt",key,iv)
print("file decrypted and saved")

