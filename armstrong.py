# ==============================
# Armstrong Number 
# ==============================

""" 
Q. What is an Armstrong Number?
Ans. An Armstrong number is a number that is equal to the sum of
    its digits raised to the power of the number of digits.

Example:
153 = 1³ + 5³ + 3³
    = 1 + 125 + 27
    = 153
"""

# Approach 1: Arithmetic (Digit Manipulation)
# Idea: Extract each digit using integer division and modulus.
num = 153
arm_sum = 0
digit_count = len(str(num))

for position in range(digit_count):
    current_digit = (num // (10 ** position)) % 10
    arm_sum += current_digit ** digit_count

if arm_sum == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")

# Time Complexity: O(d)
# Space Complexity: O(1)

print()


# Approach 2: String Traversal
# Idea: Convert each digit into string and process each digit as a character.

num = 153
digit_str = str(num)
digit_count = len(digit_str)
arm_sum = 0

for digit in digit_str:
    arm_sum += int(digit) ** digit_count

if arm_sum == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")

# d = number of digits
# Time Complexity: O(d)
# Space Complexity: O(d)