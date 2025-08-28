def caesar_encrypt(text, shift):
    """
    Encrypt text using Caesar cipher with given shift value
    """
    result = ""
    shift = shift % 26
    
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """
    Decrypt text using Caesar cipher with given shift value
    """
    return caesar_encrypt(text, -shift)

def get_valid_shift():
    """
    Get a valid shift value from user input
    """
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 0 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 25.")

def main():
    """
    Main program loop with menu interface
    """
    print("=" * 50)
    print("        CAESAR CIPHER ENCRYPTION TOOL")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            print("\n--- ENCRYPTION ---")
            message = input("Enter message to encrypt: ")
            shift = get_valid_shift()
            encrypted = caesar_encrypt(message, shift)
            print(f"\nOriginal message: {message}")
            print(f"Shift value: {shift}")
            print(f"Encrypted message: {encrypted}")
            
        elif choice == '2':
            print("\n--- DECRYPTION ---")
            message = input("Enter message to decrypt: ")
            shift = get_valid_shift()
            decrypted = caesar_decrypt(message, shift)
            print(f"\nEncrypted message: {message}")
            print(f"Shift value: {shift}")
            print(f"Decrypted message: {decrypted}")
            
        elif choice == '3':
            print("\nThank you for using the Caesar Cipher tool!")
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()           