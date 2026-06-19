# =============================================================
# Linear Search
# =============================================================

# Example:
# Input : nums = [1, 4, 7, 9, 87, 45, 21], target = 7
# Output: The given target is at 2 position.

nums = [1, 4, 7, 9, 87, 45, 21]
n = len(nums)

target = 7

for i in range(n):
    if nums[i] == target:
        print(f"The given target is at {i} position.")
        break
else:     
    print(f"Target not Found.")

# Time Complexity:
# Best:     O(1)
# Average:  O(n)
# Worst:    O(n)

# Space Complexity:
# O(1)