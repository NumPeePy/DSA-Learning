# =============================================================
# Rotate an Array k time
# =============================================================

# Problem:
# Rotate the elements of an array by k positions.

# Example:
# Input : nums = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 2
# Right Rotation Output: [8, 9, 1, 2, 3, 4, 5, 6, 7]
# Left Rotation Output : [3, 4, 5, 6, 7, 8, 9, 1, 2]

# =================================
# Right Orientation
# =================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(nums) - 1
k = 2
while k > 0:
    for i in range(n):
        nums[i], nums[n] = nums[n], nums[i]
    k -= 1
print(nums)

# Time Complexity:
# Best:     O(n x k)
# Average:  O(n x k)
# Worst:    O(n x k)

# Space Complexity:
# O(1)

print()


# ==================================
# Left Orientation
# ==================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(nums) - 1
k = 2
while k > 0:
    for i in range(n, -1, -1):
        nums[i], nums[n] = nums[n], nums[i]
    k -= 1
print(nums)

# Time Complexity:
# Best:     O(n x k)
# Average:  O(n x k)
# Worst:    O(n x k)

# Space Complexity:
# O(1)