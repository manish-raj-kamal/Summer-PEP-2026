'''
Given an array of integers heights representing the histogram's bar height where 
the width of each bar is 1, find the area of the largest rectangle in the histogram.
Example:cInput: heights = [2, 1, 5, 6, 2, 3]
Output: 10 (The largest rectangle is formed by bars 5 and 6 with a shared height of 5 and width of 2).
'''

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Append a zero height to flush out remaining bars in the stack

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # Output: 10