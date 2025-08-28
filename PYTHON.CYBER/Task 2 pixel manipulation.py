from PIL import Image # type: ignore
import numpy as np # type: ignore
import os

def encrypt_image(image_path, key, output_path=None):
    """
    Encrypt an image by applying XOR operation with a key to each pixel
    """
    try:
        # Open the image
        img = Image.open(image_path)
        img_array = np.array(img)
        
        # Apply XOR encryption to each pixel
        encrypted_array = img_array ^ key
        
        # Create encrypted image
        encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
        
        # Generate output path if not provided
        if output_path is None:
            base_name = os.path.splitext(image_path)[0]
            output_path = f"{base_name}_encrypted.png"
        
        # Save encrypted image
        encrypted_img.save(output_path)
        print(f"Image encrypted successfully! Saved as: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error encrypting image: {str(e)}")
        return None

def decrypt_image(encrypted_image_path, key, output_path=None):
    """
    Decrypt an image by applying XOR operation with the same key
    (XOR is symmetric, so decryption uses the same operation)
    """
    try:
        # Open the encrypted image
        img = Image.open(encrypted_image_path)
        img_array = np.array(img)
        
        # Apply XOR decryption (same as encryption for XOR)
        decrypted_array = img_array ^ key
        
        # Create decrypted image
        decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
        
        # Generate output path if not provided
        if output_path is None:
            base_name = os.path.splitext(encrypted_image_path)[0]
            output_path = f"{base_name}_decrypted.png"
        
        # Save decrypted image
        decrypted_img.save(output_path)
        print(f"Image decrypted successfully! Saved as: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error decrypting image: {str(e)}")
        return None

def swap_pixels(image_path, output_path=None):
    """
    Encrypt image by swapping pixel positions based on a pattern
    """
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        
        # Get image dimensions
        height, width = img_array.shape[:2]
        
        # Create a copy for manipulation
        swapped_array = img_array.copy()
        
        # Simple swap pattern: swap pixels in pairs
        for i in range(0, height, 2):
            for j in range(0, width, 2):
                if i + 1 < height and j + 1 < width:
                    # Swap adjacent pixels
                    swapped_array[i, j], swapped_array[i+1, j+1] = \
                        swapped_array[i+1, j+1].copy(), swapped_array[i, j].copy()
        
        # Create swapped image
        swapped_img = Image.fromarray(swapped_array.astype('uint8'))
        
        # Generate output path if not provided
        if output_path is None:
            base_name = os.path.splitext(image_path)[0]
            output_path = f"{base_name}_swapped.png"
        
        swapped_img.save(output_path)
        print(f"Pixel swapping completed! Saved as: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error swapping pixels: {str(e)}")
        return None

def unswap_pixels(swapped_image_path, output_path=None):
    """
    Decrypt image by reversing the pixel swap operation
    """
    # Since swapping is symmetric, we can use the same function
    return swap_pixels(swapped_image_path, output_path)

def mathematical_encryption(image_path, operation, value, output_path=None):
    """
    Apply mathematical operations to encrypt image
    Operations: 'add', 'subtract', 'multiply', 'divide'
    """
    try:
        img = Image.open(image_path)
        img_array = np.array(img, dtype=np.float64)
        
        if operation.lower() == 'add':
            result_array = (img_array + value) % 256
        elif operation.lower() == 'subtract':
            result_array = (img_array - value) % 256
        elif operation.lower() == 'multiply':
            result_array = (img_array * value) % 256
        elif operation.lower() == 'divide' and value != 0:
            result_array = (img_array / value) % 256
        else:
            print("Invalid operation or division by zero!")
            return None
        
        # Ensure values are within valid range
        result_array = np.clip(result_array, 0, 255)
        
        # Create result image
        result_img = Image.fromarray(result_array.astype('uint8'))
        
        # Generate output path if not provided
        if output_path is None:
            base_name = os.path.splitext(image_path)[0]
            output_path = f"{base_name}_math_{operation}.png"
        
        result_img.save(output_path)
        print(f"Mathematical operation '{operation}' applied! Saved as: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error applying mathematical operation: {str(e)}")
        return None

def get_valid_key():
    """Get a valid encryption key from user"""
    while True:
        try:
            key = int(input("Enter encryption key (1-255): "))
            if 1 <= key <= 255:
                return key
            else:
                print("Key must be between 1 and 255.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_file_path():
    """Get a valid file path from user"""
    while True:
        file_path = input("Enter image file path: ").strip().strip('"\'')
        if os.path.exists(file_path):
            try:
                # Try to open the image to verify it's valid
                Image.open(file_path)
                return file_path
            except Exception:
                print("Invalid image file. Please try again.")
        else:
            print("File not found. Please check the path and try again.")

def main():
    """Main program interface"""
    print("=" * 60)
    print("           IMAGE ENCRYPTION TOOL")
    print("         Pixel Manipulation Methods")
    print("=" * 60)
    
    while True:
        print("\nChoose an encryption method:")
        print("1. XOR Encryption/Decryption")
        print("2. Pixel Swapping")
        print("3. Mathematical Operations")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\n--- XOR ENCRYPTION/DECRYPTION ---")
            print("1. Encrypt image")
            print("2. Decrypt image")
            sub_choice = input("Choose option (1-2): ").strip()
            
            if sub_choice == '1':
                image_path = get_valid_file_path()
                key = get_valid_key()
                encrypt_image(image_path, key)
            elif sub_choice == '2':
                image_path = get_valid_file_path()
                key = get_valid_key()
                decrypt_image(image_path, key)
            else:
                print("Invalid choice.")
                
        elif choice == '2':
            print("\n--- PIXEL SWAPPING ---")
            print("1. Apply pixel swapping")
            print("2. Reverse pixel swapping")
            sub_choice = input("Choose option (1-2): ").strip()
            
            if sub_choice == '1':
                image_path = get_valid_file_path()
                swap_pixels(image_path)
            elif sub_choice == '2':
                image_path = get_valid_file_path()
                unswap_pixels(image_path)
            else:
                print("Invalid choice.")
                
        elif choice == '3':
            print("\n--- MATHEMATICAL OPERATIONS ---")
            image_path = get_valid_file_path()
            print("Available operations: add, subtract, multiply, divide")
            operation = input("Enter operation: ").strip()
            
            try:
                value = float(input("Enter value: "))
                mathematical_encryption(image_path, operation, value)
            except ValueError:
                print("Invalid value entered.")
                
        elif choice == '4':
            print("\nThank you for using the Image Encryption Tool!")
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()