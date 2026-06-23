# ============================================================
# Max Consecutive Ones
# ============================================================

# Approach:
# 1. index Traversal
# 2. Direct Iteration

# Example:
# Input: [1, 1, 0, 1, 1, 1]
# Output: 3

# ===========================================================
# Index Traversal
# ===========================================================

nums = [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0]
n = len(nums)

count_one = 0
max_count = 0

for i in range(n):

    if nums[i] == 1:
        count_one += 1
    
        if count_one > max_count:
            max_count = count_one

    else:
        count_one = 0

print(f"Maximum consecutive 1s: {max_count}")
      
# Time Complexity:
# Best:     O(N)
# Average:  O(N)
# Worst:    O(N)

# Space Complexity:
# O(1)

print()



# ==============================================================
# 2. Direct Iteration
# ==============================================================

nums = [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0]

count = 0
max_count = 0

for num in nums:

    if num == 1:
        count += 1
        max_count = max(max_count, count)

    else:
        count = 0

print(f"Maximum consecutive 1s: {max_count}")

# Time Complexity:
# Best:     O(N)
# Average:  O(N)
# Worst:    O(N)

# Space Complexity:
# O(1)