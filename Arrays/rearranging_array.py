# ===================================================================
# Separate Positive and Negative Numbers
# ===================================================================

# Approaches:
# 1. Using Separate Positive and Negative Lists
# 2. Using Auxiliary Array


# ===================================================================
# 1. Using Separate Positive and Negative Lists
# ===================================================================

nums = [3 ,-6, 8, 2, -9, -4, 5, 1]
n = len(nums)

pos_nums = []
neg_nums = []

for num in nums:
    if num >= 0:
        pos_nums.append(num)
    else:
        neg_nums.append(num)

n1 = len(pos_nums)
n2 = len(neg_nums)

for i in range(n1):
    nums[i] = pos_nums[i]

for j in range(n2):
    nums[n1 + j] = neg_nums[j]
print(f"Separated List: {nums}")

# Example:
# Input:  [3, -6, 8, 2, -9, -4, 5, 1]
# Output: [3, 8, 2, 5, 1, -6, -9, -4]

# Time Complexity:
# Best:     O(N)
# Average:  O(N)
# Worst:    O(N)

# Space Complexity:
# O(N)

print()



# ===================================================================
# 2. Using Auxiliary Array
# ===================================================================

nums = [3 ,-6, 8, 2, -9, -4, 5, 1]
n = len(nums)

result = [0] * n

i = 0
j = n - 1
k = 0

while k < n:

    if nums[k] >= 0:
        result[i] = nums[k]
        i += 1

    else:
        result[j] = nums[k]
        j -= 1

    k += 1

print(f"Separated List: {result}")

# Note:
# This approach does not preserve the relative order
# of negative numbers.

# Example:
# Input:  [3, -6, 8, 2, -9, -4, 5, 1]
# Output: [3, 8, 2, 5, 1, -4, -9, -6]

# Time Complexity:
# Best:     O(N)
# Average:  O(N)
# Worst:    O(N)

# Space Complexity:
# O(N)