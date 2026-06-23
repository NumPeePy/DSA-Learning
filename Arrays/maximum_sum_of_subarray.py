# ==================================================== 
# Maximum Sum of Sub-Array:
# ====================================================

nums = [-2, 4, 6, -12, 8, 10, -4, 22, 1, -16]
n = len(nums)

slice_len  = 4

max_sum = float("-inf")

for i in range((n + 1) - slice_len):

    current_sum = 0
    j = slice_len
    
    while j > 0:
        current_sum += nums[i + (slice_len - j)]
        j -= 1
    
    if current_sum > max_sum:
        max_sum = current_sum

print(f"The maximum sum of subarray is: {max_sum}")

# Time Complexity:
# Best:     O(N x k)
# Average:  O(N x k)
# Worst:    O(N x k)

# Space Complexity:
# O(1)