#from fileinput import filename
import sys
from Crypto.Cipher import AES
from Crypto import Random
from os import urandom
import hashlib



def banner():
    print("""
    

    ╔═╗╔═╗╔═╗  ═╗ ╦╔═╗╦═╗  ╔═╗┌┐┌┌─┐┬─┐┬ ┬┌─┐┌┬┐┌─┐┬─┐
    ╠═╣║╣ ╚═╗  ╔╩╦╝║ ║╠╦╝  ║╣ ││││  ├┬┘└┬┘├─┘ │ │ │├┬┘
    ╩ ╩╚═╝╚═╝  ╩ ╚═╚═╝╩╚═  ╚═╝┘└┘└─┘┴└─ ┴ ┴   ┴ └─┘┴└─
           AES/XOR encrypt files and strings
                    
           inspired by Sektor7's MDE course
           --------------------------------
                   
    """)




# string padding
def pad(s):

    return s.ljust(len(s) + AES.block_size - (len(s) % AES.block_size), '0')

""""
# Pad files
def padFile(s):

    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
"""
    

# XOR string encryption
def xorString(data, key):

    key = str(key)
    #l = len(key)
    output_str = ""

    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        output_str += chr(ord(current) ^ ord(current_key))

    return output_str


# XOR file encryption
def xorFile(data, key):

    key = str(key)
    #l = len(key)
    output_str = ""

    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        temp = (current) ^ ord(current_key)
        output_str += chr(temp)

    return output_str



# AES string encryption
def aesencString(plaintext, key):

    k = hashlib.sha256(key).digest()
    #initV = 16 * b'\x00'
    initV = Random.new().read(AES.block_size)
    
    #string padding
    plaintext = pad(plaintext)
    cipher = AES.new(k, AES.MODE_CBC, initV)
    
    return cipher.encrypt(bytes(plaintext,'utf-8'))



# AES file encryption
def aesencFile(plaintext, key):
    
    k = hashlib.sha256(key).digest()
    #initV = 16 * b'\x00'
    initV = Random.new().read(AES.block_size)

    # file padding
    length = 16 - (len(plaintext) % 16)
    plaintext += bytes([length])*length
    
    cipher = AES.new(k, AES.MODE_CBC, initV)
    
    # plaintext must be multiple of 16
    return cipher.encrypt(plaintext)



# file AES/XOR encription
def chooseForFile(plaintext):
    
    print("\n[i] You can choose between XOR and AES encryption!")
    print("\n[i] Press CTRL+C anytime to exit!\n")
    choice = input("\nPress 1 for XOR and 2 for AES: ")

    if choice == '1':
        XORkey = input("\n[*] Provide the string you want to use as XOR key: ")
        ciphertext = xorFile(plaintext, XORkey)
        ciphertext_bytes = str.encode(ciphertext)
        
        print("\n")
        print("-" * 120)
        print("[+] File to XOR encrypt: %s" %sys.argv[1])
        print("[+] Selected XOR key: %s" %XORkey)
        print(("\nXORkey[] = { 0x" + ", 0x".join(hex(ord(x))[2:] for x in XORkey) + " };"))
        #print("Payload[] = { 0x" + ", 0x".join(hex(ord(x))[2:] for x in ciphertext) + " };")
        print("-" * 120)
        
        open("testing.ico", "wb").write(ciphertext_bytes)
        print("\n[+] Encrypted file saved successfully!\n")


    elif choice == '2':
        print("\n[+] The AES key is randomly generated and it will refresh after every session!")
        AESkey = urandom(16)
        
        ciphertext = aesencFile(plaintext, AESkey)
        
        print("\n")
        print("-" * 120)
        print("[+] File to AES encrypt: %s" %sys.argv[1]) 
        print(("\nAESkey[] = { 0x" + ", 0x".join(hex(x)[2:] for x in AESkey) + " };"))
        #print("Payload[] = { 0x" + ", 0x".join(hex(x)[2:] for x in ciphertext) + " };")
        print("-" * 120)

        open("testing.ico", "wb").write(ciphertext)
        print("\n[+] Encrypted file saved successfully!\n")


    else:
        print("[-] Wrong input!")



# string AES/XOR encription
def choose():
    print("\n[i] You can choose between XOR and AES encryption!")
    print("\n[i] Press CTRL+C anytime or insert quit to exit!\n")
    choice = input("\nPress 1 for XOR and 2 for AES: ")
        
    if choice == '1':
        XORkey = input("\n[*] Provide the string you want to use as XOR key: ") 

        condition = True

        while condition:
            string = input("\n[*] What string do you want to XOR-encrypt? ")
    
            if string == "quit":
                break

            else:
                print("\n")
                print("-" * 120)                
                print("[+] String to XOR-encrypt: %s" %string)
                print("[+] Selected XOR key: %s" %XORkey)
                print("\n")

                ciphertext = xorString(string, XORkey)

                print(("XORkey[] = { 0x" + ", 0x".join(hex(ord(x))[2:] for x in XORkey) + " };"))
                print("Payload[] = { 0x" + ", 0x".join(hex(ord(x))[2:] for x in ciphertext) + " };")
                print("-" * 120)
                print("\n")


    elif choice == '2':
        print("\n[*] The AES key is randomly generated and it will refresh after every session!")
        AESkey = urandom(16)
        
        condition = True
        
        while condition:

            plaintext = input("\n[*] What string do you want to AES-encrypt? ")

            if plaintext == "quit":
                break

            elif plaintext != "quit":
                print("\n")
                print("-" * 120)
                print("[+] String to AES-encrypt: %s" %plaintext)
                print("\n")
                
                ciphertext = aesencString(plaintext, AESkey)
                
                print(("AESkey[] = { 0x" + ", 0x".join(hex(x)[2:] for x in AESkey) + " };"))
                print("Payload[] = { 0x" + ", 0x".join(hex(x)[2:] for x in ciphertext) + " };")
                print("-" * 120)
                print("\n")

    else:
        print("[-] Wrong input!")



try:
    if len(sys.argv) == 1:
        banner()
        choose()

    else:
        plaintext = open(sys.argv[1], "rb").read()
        banner()
        chooseForFile(plaintext)
        	
except:
    print("Something went wrong :( \n")
    sys.exit()