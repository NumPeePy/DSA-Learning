# ============================================================
# Sorting Algorithm
# ============================================================
# Algorithms Covered:
# 1. Selection Sort
# 2. Bubble Sort
# 3. Insertion Sort
# 4. Merge Sort
# 5. Quick Sort
# ============================================================


# ============================================================
# 1. Selection sort
# ============================================================
# Idea:
# Find the minimum number from the unsorted part
# and place it at its correct position.

nums = [4, 3, 8, 7, 6, 9, 5, 1, 2]
n = len(nums)

for i in range(n - 1):
    min_index = i
    
    for j in range(i + 1, n):

        if nums[j] < nums[min_index]:  
            min_index = j

    nums[i], nums[min_index] = nums[min_index], nums[i]

print(f"Selection sort: {nums}")

# Time Complexity: 
# Best:     O(n²)
# Average:  O(n²)
# Worst:    O(n²)

# Space Complexity:
# O(1)

print()



# ============================================================
# 2. Bubble Sort
# ============================================================
# Idea:
# repeatedly swap adjacent elements if they are
# in the wrong order.

nums = [4, 3, 8, 7, 6, 9, 5, 1, 2]
n = len(nums)

for i in range(n - 1):
    for j in range(1, n - i):

        if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
print(f"Bubble Sort: {nums}")

# Time Complexity: 
# Best:     O(n²)
# Average:  O(n²)
# Worst:    O(n²)

# Space Complexity:
# O(1)

print()



# ============================================================
# 3. Insertion Sort
# ============================================================
# Idea:
# Insert each element into its correct position
# in the sorted part of the array.

nums = [4, 9, 3, 1, 8, 2, 6, 7, 5]
n = len(nums)

for i in range(1, n):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
       nums[j + 1] = nums[j]
       j -= 1

    nums[j + 1] = key

print(f"Insertion sort: {nums}")

# Time Complexity: 
# Best:     O(n)
# Average:  O(n²)
# Worst:    O(n²)

# Space Complexity:
# O(1)

print()



# ============================================================
# 4. Merge Sort
# ============================================================
# Idea:
# Divide the array into halves, sort them, and
# then merge the sorted halves.

def merge_nums(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(nums):

    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2

    left = merge_sort(nums[ :mid])
    right = merge_sort(nums[mid: ])
    
    return merge_nums(left, right)

nums = [4, 3, 8, 7, 6, 9, 5, 1, 2]
print(f"Merge Sort: {merge_sort(nums)}")

# Time Complexity:
# Best:     O(n log(n))
# Average:  O(n log(n))
# Worst:    O(n log(n))

# Space Complexity:
# O(n)

print()



# ============================================================
# 5. Quick Sort
# ============================================================
# Idea:
# Choose a pivot and partition the array so that
# smaller elements go left and larger elements go right.

nums = [4, 3, 8, 7, 6, 9, 5, 1, 2]

def partition(nums, low, high):

    pivot = nums[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and nums[i] <= pivot:
            i += 1

        while j >= low + 1 and nums[j] > pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]

    return j
    
def quick_sort(nums, low, high):

    if low < high:
        p_index = partition(nums, low, high)

        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)


nums = [4, 3, 8, 7, 6, 9, 5, 1, 2]

quick_sort(nums, 0, (len(nums) - 1))

print(f"Quick Sort: {nums}")

# Time Complexity:
# Best:     O(n log(n))
# Average:  O(n log(n))
# Worst:    O(n²)

# Space Complexity:
# Best:     O(log n)
# Average:  O(log n)
# Worst:    O(n)