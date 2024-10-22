import random 
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters 
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")
# print(chars)

#decrypt
plain_text = input("Enter a message to decrypt :")
cipher_text = ""

for letter in cipher_text:
    index = chars.index(letter)
    plain_text += key[index]

print(f"original message :{cipher_text}")
print(f"encrypted message :{plain_text}")