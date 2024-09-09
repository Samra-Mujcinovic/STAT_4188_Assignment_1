cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

encrypted_file = open("encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write code below


# Create the reverse cipher
reverse_cipher = {v: k for k, v in cipher.items()}

# Function to decrypt the message
def decrypt_message(encrypted_message, reverse_cipher):
    decrypted_message = ""
    for char in encrypted_message:
        if char in reverse_cipher:
            decrypted_message += reverse_cipher[char]
        else:
            decrypted_message += char  # Leave any characters that are not in the cipher unchanged
    return decrypted_message

# Open the encrypted file and read the message
with open("encrypted_message_one.txt", 'r') as encrypted_file:
    encrypted_message = encrypted_file.read()

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, reverse_cipher)

# Print the decrypted message
print(decrypted_message)



