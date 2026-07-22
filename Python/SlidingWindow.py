'''
You are given an array of integers nums, and there is a sliding window
of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position, 
return the max value present inside that sliding window.
Constraint: You must solve it in O(n) time complexity.
Example: Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3 
Output: [3, 3, 5, 5, 6, 7]
'''


def max_sliding_window(nums, k):
    from collections import deque

    if not nums or k <= 0:
        return []

    result = []
    window = deque()

    for i in range(len(nums)):
        if window and window[0] < i - k + 1:
            window.popleft()

        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result

print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]