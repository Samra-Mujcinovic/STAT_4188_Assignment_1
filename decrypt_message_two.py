
encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

# Function to decrypt the transposition cipher
def decrypt_transposition_cipher(text):
    # Convert the text to a list to allow swapping characters
    text = list(text)

    # Set pointers: start from the second character from the beginning and end
    start = 1
    end = len(text) - 2

    # Swap characters as described
    while start < end:
        text[start], text[end] = text[end], text[start]
        start += 2
        end -= 2

    # Return the decrypted message as a string
    return ''.join(text)

# Open the encrypted file and read the message
with open('encrypted_message_two.txt', 'r') as encrypted_file:
    encrypted_message = encrypted_file.read()

# Decrypt the message
decrypted_message = decrypt_transposition_cipher(encrypted_message)

# Print the decrypted message
print(decrypted_message)
