import re

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.criteria = {
            'length': (8, "Password should be at least 8 characters long."),
            'uppercase': (r'[A-Z]', "Password should contain at least one uppercase letter."),
            'lowercase': (r'[a-z]', "Password should contain at least one lowercase letter."),
            'digits': (r'[0-9]', "Password should contain at least one digit."),
            'special': (r'[!@#$%^&*(),.?":{}|<>]', "Password should contain at least one special character.")
        }
        self.score = 0
        self.analysis = []

    def evaluate(self):
        if len(self.password) >= self.criteria['length'][0]:
            self.score += 1
        else:
            self.analysis.append(self.criteria['length'][1])

        for key, (pattern, message) in self.criteria.items():
            if key == 'length':
                continue
            if re.search(pattern, self.password):
                self.score += 1
            else:
                self.analysis.append(message)
        
        return self.score

    def analyze(self):
        self.evaluate()
        strength_levels = {
            5: "Very Strong",
            4: "Strong",
            3: "Moderate",
            2: "Weak",
            1: "Very Weak",
            0: "Very Weak"
        }
        print(f"Password Strength: {strength_levels[self.score]}")
        if self.analysis:
            print("Weaknesses:")
            for issue in self.analysis:
                print(f"- {issue}")
        else:
            print("Your password is strong.")

    def recommend(self):
        recommendations = [
            "Use at least 12 characters, ideally more.",
            "Include a mix of uppercase and lowercase letters.",
            "Include numbers and special characters.",
            "Avoid using easily guessable information such as names or birthdates.",
            "Use a passphrase or a series of random words for better security.",
            "Consider using a password manager to generate and store complex passwords."
        ]
        print("\nRecommendations for a stronger password:")
        for recommendation in recommendations:
            print(f"- {recommendation}")

if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    analyzer = PasswordAnalyzer(password)
    analyzer.analyze()
    analyzer.recommend()
