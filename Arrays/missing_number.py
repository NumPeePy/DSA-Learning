# ==============================================================
# Missing Numbers
# ==============================================================

# Approaches:
# 1. Brute Force (Linear Search)
# 2. Hashing
# 3. Sum Traversal
# 4. Mathematical Formula (Optimal) 

# Example:
# Input: [1, 9, 3, 0, 7, 8, 5, 2, 6]
# Output: 4



# ==============================================================
# 1. Brute Force (Linear Search)
# ==============================================================

nums = [1, 9, 3, 0, 7, 8, 5, 2, 6]
n = len(nums)

for i in range(n + 1):
    if i not in nums:
        print(f"Missing number is: {i}")
        break

# Time Complexity:
# Best:     O(N)
# Average:  O(N²)
# Worst:    O(N²)

# Space Complexity:
# O(1)

print()



# ==============================================================
# 2. Hashing Approach
# ==============================================================

nums = [1, 9, 3, 0, 7, 8, 5, 2, 6]
n = len(nums)

freq = {}

for i in range(n + 1):
    freq[i] = 0

for num in nums:
    freq[num] = 1

for k, v in freq.items():
    if v == 0:
        print(f"Missing number is: {k}")
        break

# Time Complexity:
# Best:     O(N)
# Average:  O(N)
# Worst:    O(N)

# Space Complexity:
# O(N)

print()



# ==============================================================
# 3. Sum Traversal
# ==============================================================

nums = [1, 9, 3, 0, 7, 8, 5, 2, 6]
n = len(nums)

actual_sum = 0
expected_sum = 0

for num in nums:
    actual_sum += num

for i in range(n + 1):
    expected_sum += i

print(f"Missing number is: {expected_sum - actual_sum}") 

# Time Complexity:
# Best:     O(N)
# Average:  O(N)
# Worst:    O(N)

# Space Complexity:
# O(1)

print()



# ==============================================================
# 4. Mathematical Formula (Optimal)
# ==============================================================

nums = [1, 9, 3, 0, 7, 8, 5, 2, 6]
n = len(nums)

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

print(f"Missing number is: {expected_sum - actual_sum}")

# Time Complexity:
# Best:     O(N)
# Average:  O(N)
# Worst:    O(N)

# Space Complexity:
# O(1)