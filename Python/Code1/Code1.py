alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Enter clear message: ").upper()
key = int(input("Please enter a key (number from -25 to 25): "))
encrypted = ""
for letter in message:
    position = alphabet.find(letter)
    
    if letter in alphabet:
        newPosition = position + key  
        encrypted += alphabet[newPosition]   
    else:
        encrypted += letter

print("Encrypted message:", encrypted)
