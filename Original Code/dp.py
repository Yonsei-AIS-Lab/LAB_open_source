def length_of_lis(nums):
    if not nums:  # 배열이 비어있는 경우
        return 0

    dp = [1] * len(nums)  # dp배열 초기화

    for i in range(1, len(nums)):  # 배열의 두번째 요소부터 마지막까지 순회
        for j in range(i):  # 'i'위치보다 앞쪽에 있는 모든 위치 순회
            if nums[i] > nums[j]:  # 'i' 의 위치 값이 'j'의 위치 값보다 큰 경우
                dp[i] = max(dp[i], dp[j] + 1)  # i 와 j의 위치를 바꿔야 증가하는 수열의 길이를 구할 수 있음.

    return max(dp)


# Example usage:
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
