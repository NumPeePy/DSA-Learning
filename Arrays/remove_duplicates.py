# =============================================================
# Move Zeroes to the End of the List
# =============================================================

# Approaches:
# 1. Temporary List
# 2. Nested Loops + Break
# 3. Two Pointers (Optimal)

#Example:
# Input : [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
# Output: [1, 2, 4, 3, 3, 5, 1, 0, 0, 0]

# =============================================================
# 1. Temporary List
# =============================================================

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
temp = []

n1 = n2 = 0

for num in nums:
    if num != 0:
        temp.append(num)
        n1 += 1
    else: 
        n2 += 1

for i in range(n1):
    nums[i] = temp[i]
    
for j in range(n2):
    nums[n1] = 0
    n1 += 1
    
print(nums)

# Time Complexity:
# Best:     O(n)
# Average:  O(n)
# Worst:    O(n)

# Space Complexity:
# O(n)

print()


# =============================================================
# 2. Nested Loops + Break
# =============================================================

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
n = len(nums)

for i in range(n - 1):
    if nums[i] == 0:
        for j in range(i + 1, n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                break

print(nums)

# Time Complexity:
# Best:     O(n)
# Average:  O(n²)
# Worst:    O(n²)

# Space Complexity:
# O(1)

print()


# =============================================================
# 3. Two Pointers (Optimal)
# =============================================================

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
n = len(nums)

i = 0

for j in range(n):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1 

print(nums)

# Time Complexity:
# Best:     O(n)
# Average:  O(n)
# Worst:    O(n)

# Space Complexity:
# O(1)