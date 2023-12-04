def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    '''通过辅助函数实现俩个序列间的交流,s不动,mult做中间量。
    来计算几个跳动后得到的值，再取最大值
    '''
    def count(mult, index):
        if index + 2 > len(s):
            return mult
        else:
            mult = [mult[0] * s[i] for i in range(index + 2, len(s))]
            return [count(mult, index + 2) for each in mult]
    if s == []:
        return 1
    else:
        return max(count(s, 0) + count(s, 1))

def ans_max_product(s):
    if s == []:
        return 1
    else:
        return max(ans_max_product(s[1:]), s[0] * ans_max_product(s[2:]))
    
"""At each step, we choose if we want to include the current number in our product or not:
1. If we include the current number, we cannot use the adjacent number.
2. If we don't use the current number, we try the adjacent number 
        (and obviously ignore the current number).
The recursive calls represent these two alternate realities. 
Finally, we pick the one that gives us the largest product.
"""