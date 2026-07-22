'''
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
Example:Input: nums = [1,1,1,2,2,3], k = 2  Output: [1, 2]
'''

from collections import Counter

def top_k_frequent(nums, k):
	freq = Counter(nums)
	return [num for num, _ in freq.most_common(k)]


if __name__ == "__main__":
	nums = [1, 1, 1, 2, 2, 3]
	k = 2
	print(top_k_frequent(nums, k))

