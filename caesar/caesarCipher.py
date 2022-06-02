import string

def decrypt_text(ciphertext,key):
    decrypt_plaintext = ''

    for c in ciphertext:
        if c.isupper():
            alphabet = string.ascii_uppercase
        elif c.islower():
            alphabet = string.ascii_lowercase
        else:
            decrypt_plaintext += c
            continue

        position = alphabet.find(c)
        shifted_position = (position - int(key)) % 26
        plaintext_letter = alphabet[shifted_position]
        decrypt_plaintext += plaintext_letter

    return decrypt_plaintext

def run():
    ciphertext = input("Enter the encrypted text: ")
    key = input("Enter the key: ")
    plaintext = decrypt_text(ciphertext,key)
    print("The decrypted message is: ", plaintext)


run()