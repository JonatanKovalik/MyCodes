# Define the alphabet - each letter appears twice to allow shifting with both positive and negative keys.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Request a message from the user and convert it to uppercase letters.
message = input("Enter clear message: ").upper()

# Request an encryption key, allowing for negative numbers (for decrypting a message).
key = int(input("Please enter a key (number from -25 to 25): "))

# An empty variable to store the encrypted message.
encrypted = ""

# Loop through each letter in the original message.
for letter in message:
    # Find the position of the current letter in the alphabet.
    position = alphabet.find(letter)
    
    # If the letter is in the alphabet, calculate the new position.
    if letter in alphabet:
        newPosition = position + key  # Shift the letter according to the key.
        encrypted += alphabet[newPosition]  # Append the encrypted letter to the encrypted message.
    else:
        # If the character is not a letter (e.g., a space), add it as-is.
        encrypted += letter

# Print the encrypted message.
print("Encrypted message:", encrypted)
