"""Implementing the power(x, n) function in O(log n) time complexity, basically faster than 
repeated multiplication"""

def power(x, n):
    if (n == 0 ): return 1
    temp = power(x, int(n / 2))

    if(n % 2 == 0):
        return temp * temp
    else:
        if(n > 0): return x * temp * temp
        else: return (temp * temp) / x
        
#driver code
x, n = 2, 10
print(power(x, n))