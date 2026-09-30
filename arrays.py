def reverse_array(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

def is_palindrome(num):
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    reversed_num = 0
    original = num
    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10
    return original == reversed_num

def two_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    
    print(len(arr))
    
    arr.append(60)
    print(arr)
    
    arr.remove(30)
    print(arr)
    
    target_search = 40
    if target_search in arr:
        print(arr.index(target_search))
    else:
        print(-1)
        
    for element in arr:
        print(element, end=" ")
    print()
    
    sample_to_reverse = [1, 2, 3, 4, 5]
    print(reverse_array(sample_to_reverse))
    
    print(is_palindrome(121))
    print(is_palindrome(123))
    
    nums_list = [2, 7, 11, 15]
    target_sum = 9
    print(two_sum(nums_list, target_sum))