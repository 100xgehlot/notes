from stegano import lsb

imgpath = input("Enter file name with extension: ")
msg = input("Enter a message to hide: ")

secret = lsb.hide(imgpath,msg)
secret.save("hiddenimg1.png")
print("image containing the hidden msg saved...")


clear_msg = lsb.reveal("hiddenimg1.png")
print("Verfiy hidden msg: "+clear_msg)