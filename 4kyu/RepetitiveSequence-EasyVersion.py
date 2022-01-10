# Question: https://www.codewars.com/kata/5f134651bc9687000f8022c4/train/python

# Solution:
def find(n):
    arr = [0, 1, 2, 2]
    if n <= 3:
        return arr[n]
    arr_sum = 5
    arr_len = 4
    for i in range(3, n+1):
        arr_sum += i * arr[i]
        if arr_sum >= n:
            x = (arr_sum - n) // i
            return arr_len + arr[i] - (x+1)
        arr_len += arr[i]
        if arr_len < 70_000:
            arr += [i] * arr[i]

# Sample Tests
'''@test.describe('Example Tests')
def example_tests():
    testing = [[0, 0], [1, 1], [2, 2], [3, 2], [4, 3], [5, 3], [6, 4], [7, 4], [8, 4], [9, 5], [10, 5], [11, 5], [12, 6], [13, 6], [14, 6], [15, 6], [16, 7], [17, 7], [18, 7], [19, 7]]
    
    for nth, expected in testing:
        test.assert_equals(find(nth), expected)'''
