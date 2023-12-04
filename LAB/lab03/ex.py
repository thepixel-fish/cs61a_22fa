
def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    high_num = 0
    final = 0
    while k >= 0:
        tempn, i = n, 0
        while tempn > 0:
            if high_num < tempn % 10:
                high_num = tempn % 10
                pos = i
            tempn, i = tempn // 10, i + 1
        high_num = 0
        n ,reminder = n // 10 ** pos, n % 10 ** pos
        while n % 10 > n // 10 % 10 and n // 10 > 0:
            n //= 10
        final, n = n % 10, n // 10
        n = n + reminder
        k = k - 1
    return final