# Question: https://www.codewars.com/kata/5511b2f550906349a70004e1/python
# Name: Last digit of a large number
# Level: 5kyu

# Solution:
rules = {
    0: [0,0,0,0],   
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6], 
    5: [5,5,5,5], 
    6: [6,6,6,6], 
    7: [7,9,3,1], 
    8: [8,4,2,6], 
    9: [9,1,9,1],
}

def last_digit(n1, n2):
    ruler = rules[int(str(n1)[-1])]
    if n2 == 0:
        return 1
    else:
        return ruler[(n2 % 4) - 1]
 
# Examples:
'''
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
'''
