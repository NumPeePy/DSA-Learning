# ========================
# Palindrome
# ========================


"""
Q. What is a Palindrome?
Ans. Any number or charater sequence that reads the same forwards 
    and backwards is called a palindrome.

Examples:
NOON, NAMAN, NAYAN, 12321, 990099
"""

# Appraoch 1: Arithmetic (Digit manipulation)
 
num = 0
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10     
    reversed_num = reversed_num * 10 + digit
    num //= 10         

if reversed_num == original_num:
    print(f"{original_num} is a Palindrome.")
else:
    print(f"{original_num} is not a palindrome.")

#d = number of digits
# Time Complexity: O(d)
# Space Complexity: O(1)

print()


# Appraoch 2: String Transversal

num = 12521

if str(num) == str(num)[::-1]:
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is not a Palindrome.")

# Time Complexity: O(d)
# Space Complecity: O(d)