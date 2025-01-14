def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    
    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.
    
    Returns:
    List[int]: Indices of the two numbers.
    """
    Example = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [Example[complement], i]
        Example[num] = i
    return []

# Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))  # Output: [0, 1]