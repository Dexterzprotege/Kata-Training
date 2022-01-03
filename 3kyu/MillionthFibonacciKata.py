# Question: https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python

# Description:
'''In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.

HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n) if you already know fib(n + 1) and fib(n + 2)? Use this to reason what value fib has to have for negative values.

HINT II: See https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4 '''

# Solution:
import numpy as np

def fib(n):
    matrix = np.matrix([[1, 1], [1, 0]], dtype=object) ** abs(n)
    if n%2 == 0 and n < 0:
        return -matrix[0,1]
    return matrix[0, 1]
  
# Sample Tests
test.assert_equals(fib(0),0)
test.assert_equals(fib(1),1)
test.assert_equals(fib(2),1)
test.assert_equals(fib(3),2)
test.assert_equals(fib(4),3)
test.assert_equals(fib(5),5)
test.assert_equals(fib(1000),43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)
