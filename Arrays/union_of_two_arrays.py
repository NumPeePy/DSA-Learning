# =================================================================
# Union of Two Sorted Arrays
# =================================================================

# Approaches:
# 1. Two Pointers (Optimal)
# 2. Set (Brute Force)

# Example:
# nums_1 = [1, 1, 2, 3]
# nums_2 = [1, 2, 4]
# Output = [1, 2, 3, 4]



# =================================================================
# 1. Two Pointers (Optimal)
# =================================================================

nums_1 = [1, 1, 1, 2, 3, 4, 6, 7, 8, 8, 9]
nums_2 = [1, 2, 2, 5, 7, 7, 8]

n1 = len(nums_1)
n2 = len(nums_2)

union = []

i = j = 0

while i < n1 and j < n2:
    if nums_1[i] <= nums_2[j]:
        if len(union) == 0 or union[-1] != nums_1[i]:
            union.append(nums_1[i])
        i += 1
    else:
        if len(union) == 0 or union[-1] != nums_2[j]:
            union.append(nums_2[j])
        j += 1

while i < n1:
    if len(union) == 0 or union[-1] != nums_1[i]:
        union.append(nums_1[i])
    i += 1

while j < n2:
    if len(union) == 0 or union[-1] != nums_2[j]:
        union.append(nums_2[j])
    j += 1

print(f"Union: {union}")

# Time Complexity:
# Best:     O(n1 + n2)
# Average:  O(n1 + n2)
# Worst:    O(n1 + n2)

# Space Complexity:
# O(n1 + n2)

print()



# ====================================================================
# 2. Set (Brute Force)
# ====================================================================

nums_1 = [1, 1, 1, 2, 3, 4, 6, 7, 8, 8, 9]
nums_2 = [1, 2, 2, 5, 7, 7, 8]


union = sorted(set(nums_1 + nums_2))

print(f"Union: {union}")

# Time Complexity:
# Best:     O((n1 + n2) log(n1 + n2))
# Average:  O((n1 + n2) log(n1 + n2))
# Worst:    O((n1 + n2) log(n1 + n2))

# Space Complexity:
# O(n1 + n2)