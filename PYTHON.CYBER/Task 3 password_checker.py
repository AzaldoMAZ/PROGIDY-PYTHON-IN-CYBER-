import re
import string
from getpass import getpass

class PasswordChecker:
    def __init__(self):
        self.common_passwords = [
            "password", "123456", "password123", "admin", "qwerty",
            "letmein", "welcome", "monkey", "1234567890", "abc123",
            "password1", "123456789", "welcome123", "admin123",
            "root", "toor", "pass", "test", "guest", "user"
        ]
        
    def check_length(self, password):
        """Check password length and return score and feedback"""
        length = len(password)
        if length < 6:
            return 0, "Too short (minimum 6 characters)"
        elif length < 8:
            return 1, "Short (recommend 8+ characters)"
        elif length < 12:
            return 2, "Good length"
        else:
            return 3, "Excellent length"
    
    def check_uppercase(self, password):
        """Check for uppercase letters"""
        if re.search(r'[A-Z]', password):
            count = len(re.findall(r'[A-Z]', password))
            return 1, f"Contains {count} uppercase letter(s) ✓"
        return 0, "Missing uppercase letters"
    
    def check_lowercase(self, password):
        """Check for lowercase letters"""
        if re.search(r'[a-z]', password):
            count = len(re.findall(r'[a-z]', password))
            return 1, f"Contains {count} lowercase letter(s) ✓"
        return 0, "Missing lowercase letters"
    
    def check_numbers(self, password):
        """Check for numbers"""
        if re.search(r'[0-9]', password):
            count = len(re.findall(r'[0-9]', password))
            return 1, f"Contains {count} number(s) ✓"
        return 0, "Missing numbers"
    
    def check_special_chars(self, password):
        """Check for special characters"""
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        special_in_password = [char for char in password if char in special_chars]
        if special_in_password:
            return 1, f"Contains {len(special_in_password)} special character(s): {''.join(set(special_in_password))} ✓"
        return 0, "Missing special characters (!@#$%^&* etc.)"
    
    def check_common_patterns(self, password):
        """Check for common weak patterns"""
        issues = []
        score_penalty = 0
        
        # Check for common passwords
        if password.lower() in [pwd.lower() for pwd in self.common_passwords]:
            issues.append("Uses a common password")
            score_penalty += 2
        
        # Check for sequential characters
        if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
            issues.append("Contains sequential numbers")
            score_penalty += 1
        
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
            issues.append("Contains sequential letters")
            score_penalty += 1
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            issues.append("Contains repeated characters (3+ in a row)")
            score_penalty += 1
        
        # Check for keyboard patterns
        keyboard_patterns = ['qwerty', 'asdf', 'zxcv', '1234', 'qwer', 'asdfg']
        for pattern in keyboard_patterns:
            if pattern in password.lower():
                issues.append(f"Contains keyboard pattern: {pattern}")
                score_penalty += 1
        
        return score_penalty, issues
    
    def check_character_variety(self, password):
        """Check for character variety and complexity"""
        char_types = 0
        feedback = []
        
        if re.search(r'[a-z]', password):
            char_types += 1
        if re.search(r'[A-Z]', password):
            char_types += 1
        if re.search(r'[0-9]', password):
            char_types += 1
        if re.search(r'[^a-zA-Z0-9]', password):
            char_types += 1
        
        if char_types == 4:
            return 2, "Excellent character variety (all 4 types) ✓"
        elif char_types == 3:
            return 1, "Good character variety (3 types)"
        elif char_types == 2:
            return 0, "Limited character variety (only 2 types)"
        else:
            return -1, "Very limited character variety (only 1 type)"
    
    def calculate_entropy(self, password):
        """Calculate password entropy (bits of randomness)"""
        char_space = 0
        
        if re.search(r'[a-z]', password):
            char_space += 26
        if re.search(r'[A-Z]', password):
            char_space += 26
        if re.search(r'[0-9]', password):
            char_space += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            char_space += 32  # Approximate special characters
        
        if char_space == 0:
            return 0, "Cannot calculate entropy"
        
        import math
        entropy = len(password) * math.log2(char_space)
        
        if entropy < 30:
            return 0, f"Very low entropy ({entropy:.1f} bits) - easily crackable"
        elif entropy < 50:
            return 1, f"Low entropy ({entropy:.1f} bits) - weak against attacks"
        elif entropy < 70:
            return 2, f"Moderate entropy ({entropy:.1f} bits) - reasonable security"
        else:
            return 3, f"High entropy ({entropy:.1f} bits) - strong security ✓"
    
    def assess_password(self, password):
        """Comprehensive password assessment"""
        if not password:
            return {
                'score': 0,
                'strength': 'Invalid',
                'feedback': ['Password cannot be empty']
            }
        
        total_score = 0
        feedback = []
        
        # Length check
        length_score, length_feedback = self.check_length(password)
        total_score += length_score
        feedback.append(f"Length: {length_feedback}")
        
        # Character type checks
        upper_score, upper_feedback = self.check_uppercase(password)
        total_score += upper_score
        feedback.append(f"Uppercase: {upper_feedback}")
        
        lower_score, lower_feedback = self.check_lowercase(password)
        total_score += lower_score
        feedback.append(f"Lowercase: {lower_feedback}")
        
        number_score, number_feedback = self.check_numbers(password)
        total_score += number_score
        feedback.append(f"Numbers: {number_feedback}")
        
        special_score, special_feedback = self.check_special_chars(password)
        total_score += special_score
        feedback.append(f"Special chars: {special_feedback}")
        
        # Character variety
        variety_score, variety_feedback = self.check_character_variety(password)
        total_score += variety_score
        feedback.append(f"Variety: {variety_feedback}")
        
        # Entropy calculation
        entropy_score, entropy_feedback = self.calculate_entropy(password)
        total_score += entropy_score
        feedback.append(f"Entropy: {entropy_feedback}")
        
        # Pattern checks (penalties)
        pattern_penalty, pattern_issues = self.check_common_patterns(password)
        total_score -= pattern_penalty
        
        if pattern_issues:
            feedback.append("⚠️  Security Issues:")
            for issue in pattern_issues:
                feedback.append(f"  - {issue}")
        
        # Determine strength level
        if total_score <= 2:
            strength = "Very Weak"
            color = "🔴"
        elif total_score <= 4:
            strength = "Weak"
            color = "🟠"
        elif total_score <= 6:
            strength = "Fair"
            color = "🟡"
        elif total_score <= 8:
            strength = "Good"
            color = "🔵"
        else:
            strength = "Strong"
            color = "🟢"
        
        return {
            'score': total_score,
            'max_score': 10,
            'strength': strength,
            'color': color,
            'feedback': feedback
        }
    
    def generate_password_suggestions(self):
        """Generate example strong passwords"""
        suggestions = [
            "Tr0ub4dor&3",  # XKCD style but modified
            "MyD0g@L0vesW4lks!",
            "C0ff33&C0de2024",
            "Blu3Sky$Sunshine",
            "R0ck&R0ll4Ever!",
        ]
        return suggestions

def display_results(result):
    """Display password assessment results"""
    print("\n" + "="*60)
    print("           PASSWORD STRENGTH ASSESSMENT")
    print("="*60)
    
    print(f"\nOverall Strength: {result['color']} {result['strength'].upper()}")
    print(f"Score: {result['score']}/{result['max_score']}")
    
    # Create visual strength bar
    bar_length = 20
    filled_length = int(bar_length * result['score'] / result['max_score'])
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    print(f"Strength: [{bar}] {result['score']}/{result['max_score']}")
    
    print(f"\nDetailed Analysis:")
    print("-" * 40)
    for item in result['feedback']:
        print(f"  {item}")
    
    # Recommendations
    print(f"\n💡 Recommendations:")
    if result['score'] < 6:
        print("  - Increase password length (12+ characters recommended)")
        print("  - Include uppercase and lowercase letters")
        print("  - Add numbers and special characters")
        print("  - Avoid common words and patterns")
        print("  - Consider using a passphrase with substitutions")
    elif result['score'] < 8:
        print("  - Consider adding more character variety")
        print("  - Increase length for better security")
        print("  - Avoid predictable patterns")
    else:
        print("  - Excellent password! Keep using strong passwords like this.")
        print("  - Remember to use unique passwords for each account")
        print("  - Consider using a password manager")

def main():
    """Main program interface"""
    checker = PasswordChecker()
    
    print("="*60)
    print("           PASSWORD COMPLEXITY CHECKER")
    print("         Security Assessment Tool")
    print("="*60)
    print("\nThis tool helps you assess password strength and security.")
    print("Your password will not be stored or transmitted anywhere.")
    
    while True:
        print(f"\nOptions:")
        print("1. Check password strength")
        print("2. View password guidelines")
        print("3. See example strong passwords")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\n--- PASSWORD STRENGTH CHECK ---")
            print("Enter your password (input will be hidden for security):")
            
            # Use getpass for secure password input
            password = getpass("Password: ")
            
            # Assess the password
            result = checker.assess_password(password)
            
            # Display results
            display_results(result)
            
        elif choice == '2':
            print("\n--- PASSWORD SECURITY GUIDELINES ---")
            print("="*50)
            print("✅ DO:")
            print("  • Use at least 12 characters")
            print("  • Include uppercase letters (A-Z)")
            print("  • Include lowercase letters (a-z)")
            print("  • Include numbers (0-9)")
            print("  • Include special characters (!@#$%^&*)")
            print("  • Use unique passwords for each account")
            print("  • Consider passphrases with substitutions")
            print("  • Use a password manager")
            print("\n❌ DON'T:")
            print("  • Use personal information (names, birthdays)")
            print("  • Use common words or phrases")
            print("  • Use sequential characters (123, abc)")
            print("  • Use repeated characters (aaa, 111)")
            print("  • Use keyboard patterns (qwerty, asdf)")
            print("  • Reuse passwords across accounts")
            
        elif choice == '3':
            print("\n--- EXAMPLE STRONG PASSWORDS ---")
            print("="*45)
            suggestions = checker.generate_password_suggestions()
            print("Here are some examples of strong passwords:")
            print("(Don't use these exact ones - create your own!)")
            print()
            for i, suggestion in enumerate(suggestions, 1):
                result = checker.assess_password(suggestion)
                print(f"{i}. {suggestion}")
                print(f"   Strength: {result['color']} {result['strength']} (Score: {result['score']}/{result['max_score']})")
                print()
            
            print("💡 Tips for creating your own:")
            print("  • Start with a memorable phrase")
            print("  • Substitute letters with numbers/symbols")
            print("  • Add random characters at the end")
            print("  • Make it personal but not obvious")
            
        elif choice == '4':
            print("\nThank you for using the Password Complexity Checker!")
            print("Stay secure online! 🔒")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()