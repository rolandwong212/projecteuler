# XOR decryption
# Problem 59
# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange). For
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# 
# A modern encryption method is to take a text file, convert the bytes to
# ASCII, then XOR each byte with a given value, taken from a secret key. The
# advantage with the XOR function is that using the same encryption key on the
# cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
# 
# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without
# both "halves", it is impossible to decrypt the message.
# 
# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password
# key for security, but short enough to be memorable.
# 
# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
# a file containing the encrypted ASCII codes, and the knowledge that the plain
# text must contain common English words, decrypt the message and find the sum
# of the ASCII values in the original text.


import itertools # needed for permutations and cycle methods
import string
import sys

# list comprehension of three char permutations of lowercase
enc_key_space = [x for x in itertools.permutations(string.ascii_lowercase,3)]

filename = input('enter source file: ')

with open(filename) as source:
    ciphertext = source.read()

# for i in range(len(enc_key_space)):
# for n chars in ciphertext, XOR cyclicly with enc_key_space[i]

def decrypt(k,c):
    """Returns a list.

    Assumes k is a three lowercase character string, and c is the ciphertext.
    the function will XOR each successive character from k with each character
    from c, then cycle k."""
    zipped = list(zip(itertools.cycle(k),c))
    return [((ord(zipped[i][0])) ^ int(zipped[i][1])) for i in range(len(zipped))]

#cleartext = [(decrypt(enc_key_space[i],ciphertext.split(','))) for i in range(len(enc_key_space))]




# for i in range(len(cleartext)):
#     sys.stdout.write(chr(cleartext[i]))
# 
# sys.stdout.flush
# 



# for i in range(len(enc_key_space)):
#     print()
#     print(enc_key_space[i])
#     for j in range(len(cleartext[i])):
#         sys.stdout.write(chr(cleartext[i][j]))
#     sys.stdout.flush


def main(*args):
    """calls other functions"""
    for i in range(len(enc_key_space)):
        testkey = [ enc_key_space[i][j] for j in range(len(enc_key_space[i])) ]
        print()
        print(testkey)
        cleartext = decrypt(testkey,ciphertext.split(','))
        for k in range(len(cleartext)):
            sys.stdout.write(chr(cleartext[k]))
        sys.stdout.flush
    return


#main()

cleartext = decrypt(["g","o","d"],ciphertext.split(','))

print(sum(cleartext))
