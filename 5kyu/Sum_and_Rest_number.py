# Question: https://www.codewars.com/kata/5603a9585480c94bd5000073/python
# Name: Sum and Rest the Number with its Reversed and See What Happens
# Level: 5kyu

# Description:
'''The number 45 is the first integer in having this interesting property: the sum of the number with its reversed is divisible by the difference between them(absolute Value).

45 + 54 = 99 
abs(45 - 54) = 9
99 is divisible by 9.
The first terms of this special sequence are :

n        a(n)
1        45
2        54
3        495
4        594
Make the function sum_dif_rev()(sumDivRef in JavaScript and CoffeeScript), that receives n, the ordinal number of the term and may give us, the value of the term of the sequence.

sum_dif_rev(n) -----> a(n)
Let's see some cases:

sum_dif_rev(1) -----> 45
sum_dif_rev(3) -----> 495
"Important: Do not include numbers which, when reversed, have a leading zero, e.g.: 1890 reversed is 0981, so 1890 should not be included."
Your code will be tested up to the first 65 terms, so you should think to optimize it as much as you can.'''

def isNumber(x):
    sum = x + int(str(x)[::-1])
    diff = abs(x - int(str(x)[::-1]))
    if diff == 0:
        return False
    if sum % diff == 0:
        return True
    return False

ans = []
for i in range(45, 10**6):
    if str(i)[-1] == '0':
        continue
    if isNumber(i):
        ans.append(i)

def sum_dif_rev(n):
    #your code here
    return ans[n-1] # n-th term of the sequence
  

# Sample Tests:
'''test.describe("Example Tests")
test.assert_equals(sum_dif_rev(1), 45)
test.assert_equals(sum_dif_rev(3), 495)
test.assert_equals(sum_dif_rev(4), 594)'''
