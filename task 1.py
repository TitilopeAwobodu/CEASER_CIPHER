def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Example Usage
plain_text = "Cyber, world"
shift_value = 7
encrypted_text = caesar_encrypt(plain_text, shift_value)
decrypted_text = caesar_decrypt(encrypted_text, shift_value)

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

def main():
    print("Caesar Cipher Program")
    
    # Get user input for encryption or decryption
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    
    # Get the message from the user
    message = input("Enter your message: ")
    
    # Get the shift value from the user
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_message = caesar_cipher_encrypt(message, shift) # type: ignore
        print("Encrypted Message: " + encrypted_message)
    elif choice == 'D':
        decrypted_message = caesar_cipher_decrypt(message, shift) # type: ignore
        print(f"Decrypted Message: {decrypted_message}")
    else:print("Invalid choice. Please enter 'E' for encryption or 'D' for decryptiom.")