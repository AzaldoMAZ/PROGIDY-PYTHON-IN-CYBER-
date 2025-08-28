# Cybersecurity Educational Tasks

This repository contains three educational cybersecurity projects designed to help understand fundamental concepts in encryption, password security, and image processing. These tasks are intended for learning purposes and should be used responsibly with proper authorization.

## 📋 Overview

| Task | Name | Description | Difficulty |
|------|------|-------------|------------|
| Task-01 | Caesar Cipher | Text encryption/decryption using classical cipher | Beginner |
| Task-02 | Image Encryption | Pixel manipulation for image security | Intermediate |
| Task-03 | Password Checker | Password strength assessment tool | Beginner |

---

## 🔐 Task-01: Caesar Cipher Implementation

### Description
Create a Python program that implements the Caesar Cipher algorithm for encrypting and decrypting text messages. This classical substitution cipher shifts each letter by a fixed number of positions in the alphabet.

### Features
- Encrypt text messages using user-defined shift values
- Decrypt encrypted messages
- Handle both uppercase and lowercase letters
- Preserve non-alphabetic characters (spaces, punctuation)
- Interactive user interface for message input and shift value selection

### Learning Objectives
- Understanding basic cryptographic concepts
- Algorithm implementation in Python
- String manipulation and character encoding
- User input validation and error handling

### Usage Example
```
Enter message: Hello World
Enter shift value: 3
Encrypted: Khoor Zruog
```

### Implementation Notes
- Use modular arithmetic for alphabet wrapping
- Consider edge cases (negative shifts, non-alphabetic characters)
- Implement both encryption and decryption functions
- Add input validation for shift values

---

## 🖼️ Task-02: Pixel Manipulation for Image Encryption

### Description
Develop a simple image encryption tool using pixel manipulation techniques. This project involves applying mathematical operations to pixel values to encrypt and decrypt images.

### Features
- Load and process image files (PNG, JPEG)
- Apply pixel value transformations for encryption
- Implement corresponding decryption operations
- Support for various image formats
- Visual comparison of original and encrypted images

### Possible Techniques
- **Pixel Swapping**: Rearrange pixels based on a pattern
- **Mathematical Operations**: Apply arithmetic operations to RGB values
- **XOR Operations**: Use XOR with a key for reversible encryption
- **Bit Manipulation**: Modify specific bits in pixel data

### Learning Objectives
- Image processing fundamentals
- Pixel data manipulation
- File I/O operations with images
- Understanding of color spaces (RGB)
- Reversible transformation concepts

### Implementation Notes
- Use libraries like PIL (Pillow) or OpenCV for image handling
- Ensure encryption operations are reversible
- Consider memory efficiency for large images
- Implement proper error handling for file operations

---

## 🔒 Task-03: Password Complexity Checker

### Description
Build a comprehensive password strength assessment tool that evaluates passwords based on multiple security criteria and provides actionable feedback to users.

### Assessment Criteria
- **Length**: Minimum character requirements
- **Character Diversity**: 
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- **Pattern Detection**: Identify common weak patterns
- **Dictionary Attacks**: Check against common passwords

### Features
- Real-time password strength indicator
- Detailed feedback on security weaknesses
- Scoring system (Weak/Moderate/Strong/Very Strong)
- Suggestions for password improvement
- Optional password generation with custom criteria

### Strength Levels
| Level | Requirements | Score |
|-------|-------------|-------|
| Weak | < 8 chars, missing character types | 0-25 |
| Moderate | 8+ chars, 2-3 character types | 26-50 |
| Strong | 10+ chars, all character types | 51-75 |
| Very Strong | 12+ chars, all types + no patterns | 76-100 |

### Learning Objectives
- Security best practices understanding
- Regular expressions for pattern matching
- Algorithm design for scoring systems
- User experience in security applications

### Implementation Notes
- Use regex for pattern detection
- Implement entropy calculation for randomness
- Consider using zxcvbn-style algorithms
- Provide constructive feedback, not just scores

---

## 🚀 Getting Started

### Prerequisites
```bash
# Required Python packages
pip install pillow  # For image processing (Task-02)
pip install regex   # For advanced pattern matching (Task-03)
```

### Project Structure
```
cybersecurity-tasks/
├── task01_caesar_cipher/
│   ├── caesar_cipher.py
│   ├── tests.py
│   └── README.md
├── task02_image_encryption/
│   ├── image_encrypt.py
│   ├── sample_images/
│   ├── tests.py
│   └── README.md
├── task03_password_checker/
│   ├── password_checker.py
│   ├── common_passwords.txt
│   ├── tests.py
│   └── README.md
└── README.md
```

## ⚠️ Important Ethical Considerations

### Educational Use Only
These projects are designed for educational purposes to understand cybersecurity concepts. Users must:

- Only use these tools on their own systems and data
- Obtain proper authorization before testing on any network or system
- Respect privacy and legal boundaries
- Not use these tools for malicious purposes

### Security Disclaimers
- The encryption methods implemented are for learning purposes only
- Do not use these implementations for protecting sensitive data in production
- Real-world security requires professional-grade, tested cryptographic libraries
- Always follow responsible disclosure practices

### Legal Compliance
- Ensure compliance with local laws and regulations
- Respect intellectual property rights
- Follow institutional policies for cybersecurity education
- Report any security vulnerabilities responsibly

## 📚 Additional Resources

### Further Learning
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Introduction to Cryptography - Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography)
- [Python Cryptography Documentation](https://cryptography.io/)

### Related Concepts
- Symmetric vs Asymmetric encryption
- Hash functions and digital signatures
- Modern encryption standards (AES, RSA)
- Security through obscurity vs proper cryptography

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes with proper documentation
4. Add tests for new functionality
5. Submit a pull request with detailed description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Acknowledgments

- Educational institutions promoting cybersecurity awareness
- Open-source cryptography communities
- Security researchers advancing the field

---

**Remember**: With great power comes great responsibility. Use these tools ethically and legally!
