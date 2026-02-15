

# Two Sum Problem

def two_sum(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print((i, j), end=" ")
    return None

nums = [2, 7, 11, 15, 3, 4, 1, 5]   
target = 6
result = two_sum(nums, target)
