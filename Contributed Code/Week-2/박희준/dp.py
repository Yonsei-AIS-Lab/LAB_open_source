def length_of_lis(nums):
    if not nums:
        return 0
    
    cnt = 0 # nums의 길이를 저장하기 위한 변수
    
    for i in nums: # nums의 원소 개수만큼 iterate하며 
        cnt += 1 # 1 증가
    
    return cnt

# Example usage:
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
