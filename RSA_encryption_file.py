from random import *
from time import *
import math

# Modular arithmetic methods

def random_prime():
    p = randint(1, 10000)
    q = randint(1, 1000)
    while math.gcd(p, q) != 1:
        p = randint(1, 10000)
        q = randint(1, 10000)
    return p, q

def exponential_cipher():
    a, b = random_prime()
    n = a * b  # encryption module
    phi = (a - 1) * (b - 1)
    e = randint(1, phi - 1)
    while math.gcd(e, phi) != 1:
        e = randint(1, phi)
    return e, phi, n

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, b):
    x, y, z = extended_euclidean(a, b)
    return y

# private and public key generation
def generation_key():
    global e, phi, n, d
    e, phi, n = exponential_cipher()

    d = modular_inverse(e, phi)
    if d < 0:
        del (e, phi, n, d)
        generation_key()
    else:
        print("Public key :", (e, n))
        print("Private key :", (d, n))
    return e, d, n



print("\n")
print ("---------------------------------------------------------------------------------\n")
print ("----------------------------  [ Python 3.9 ]  -----------------------------------\n")
print ("------------  RSA Asymmetric Cryptosystem Encryption & Decryption  --------------\n")
print ("------------------------------   E.Erwann    ------------------------------------\n")
print ("---------------------------------------------------------------------------------\n")
print ("\n")

sleep(1)
print ("---------------------------------------------------------------------------------\n")
channel = "abcdefghijklmnopqrstuvwxyzABDCEFGHIJKLMNOPQRSTUVWXYZ0123456789!?.,: "
print("Generating key...")
sleep(2)
(e, d, n) = generation_key()

#encryption process

plaintext = input("Type plaintext to encrypt: ")
ciphertext = ""
for k in plaintext:
    m = 0
    for l in channel:
        if k == l:
            if m < 10:
                m = m + 00
            ciphertext = ciphertext + (str(pow(m, e, n))) + " "
            break
        m += 1
print("Encrypted text : ",ciphertext)

#decryption process

print("\n")
encrypted_text = input("Type ciphertext to decrypt: ")
plain_text = ""
for s in encrypted_text.split(" "):
    for k in channel:
        m = 0
        for l in channel:
            if k == l:
                if s == (str(pow(m, e, n))):
                    plain_text = plain_text + l
                break
            m += 1
print("Decrypted message : ", plain_text)
print("\n")

#encrypting .txt file

path = input("Specify full file path to encrypt :")
file = open(path)
cipherfile = file.read()
encrypted_file = open("encrypted_file.txt", "w")
ciphertext = ""
for k in cipherfile:
    m = 0
    for l in channel:
        if k == l:
            if m < 10:
                m = m + 00
            ciphertext = ciphertext + (str(pow(m, e, n))) + " "
            break
        m += 1
encrypted_file.write(str(ciphertext))
encrypted_file.close()
encrypted_file = open("encrypted_file.txt", "r")
print("Encrypted file : \n")
print(encrypted_file.read())
file.close()
print("\n")

#decrypting file

Verification = input("Input private key to decrypt : ")
while Verification != str(d):
    print("Wrong private key...\n")
    Verification = input("Input private key to decrypt : ")
decrypted_file = open("decrypted_file.txt", "w")
plain_text = ""
for s in encrypted_file.read():
    for k in channel:
        m = 0
        for l in channel:
            if k == l:
                if s == (str(pow(m, e, n))):
                    plain_text = plain_text + l
                break
            m += 1
decrypted_file.write(str(plain_text))
decrypted_file.close()
decrypted_file = open("decrypted_file.txt", "r")
print("Decrypted file : \n")
print(decrypted_file.read())
encrypted_file.close()
decrypted_file.close()
