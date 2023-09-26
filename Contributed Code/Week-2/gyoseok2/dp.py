def length_of_lis(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(1, i): # 코드 일관성 통일 및 계산 횟수 감소
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage:
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
