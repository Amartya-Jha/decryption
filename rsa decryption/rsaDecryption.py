import rsa

def load_private_key(private_key_location):
    private_key = None
    with open(private_key_location, "rb") as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read(), format = 'PEM')

        return private_key

def rsa_decrypt(encrypted_data,private_key):
    decrypted = rsa.decrypt(encrypted_data,private_key).decode('utf-8')

    return decrypted

def run():
    private_key_location = input("Enter privtae key location: ")
    private_key = load_private_key((private_key_location))
    encrypted_file_location = input("Enter encrypted text location: ")
    with open(encrypted_file_location, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = rsa_decrypt(encrypted_data, private_key)

        print("Decrypted text is: ", decrypted_data)

run()

