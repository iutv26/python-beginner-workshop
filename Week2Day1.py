#Simple Calculator using functions
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
print("Addition: ", add(a, b))
print("Subtraction: ", subtract(a, b))
print("Multiplication: ", multiply(a, b))
print("Division: ", divide(a, b))
print("\n")

#Grade classification using functions
def grade_classification(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score < 0 or score > 100:
        return "Invalid score"
    else:
        return "F"
score = float(input("Enter the score: "))
print("Grade: ", grade_classification(score))
 