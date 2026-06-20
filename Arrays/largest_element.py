## ============================================================
# 1. Largest Element in an Array
# ============================================================

nums = [5, 10, 20, 5, 50, 45, 90, 15]

n = len(nums)
largest = float("-inf")

for i in range(n):           
    if largest < nums[i]:
        largest = nums[i]
        
print(f"Largest element is: {largest}")

# Time Complexity:
# Best:     O(n)
# Average:  O(n)
# Worst:    O(n)

# Space Complexity:
# O(1)

print()



# ============================================================
# 2. Second largest element
# ============================================================

nums = [5, 10, 20, 5, 50, 45, 90, 15]
n = len(nums)

largest = float("-inf")
s_largest = float("-inf")

for i in range(n):
    if largest < nums[i]:
        largest = nums[i]

for j in range(n):
    if s_largest < nums[j] < largest:
        s_largest = nums[j]

print(f"The largest element is: {largest}")

if s_largest == float("-inf"):
    print("There is no second largest element")
else:
    print(f"The second largest element is: {s_largest}")

# Time Complexity: 
# Best:     O(n)
# Average:  O(n)
# Worst:    O(n)

# Space Complexity:
# O(1)