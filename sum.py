"""This python scripts accepts two numbers from a user and prints the sum"""

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

def add(num1: int, num2: int) -> int:
    """sum function"""
    
    return num1 + num2

print(f"The sum is = {add(x, y)}")

#To run the code: python sum.py
