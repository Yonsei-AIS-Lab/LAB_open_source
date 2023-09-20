def length_of_lis(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j], dp[i] + 1)
    
    return max(dp)

# Example usage:
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
