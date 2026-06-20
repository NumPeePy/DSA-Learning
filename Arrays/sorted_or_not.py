# ============================================================
# Sorted OR Not?
# ============================================================

nums = [1, 1, 4, 5, 6, 8, 9]
n = len(nums)

check = True

for i in range(n - 1):
    if nums[i] > nums[i + 1]:
        check = False
        break

print("Sorted") if check else print("Unsorted")

# Time Complexity: 
# Best:     O(1)
# Average:  O(n)
# Worst:    O(n)

# Space Complexity:
# O(1)

print()