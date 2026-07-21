# Factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
        
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 30]
target = 12
result = binary_search(data, target, 0, len(data) - 1)