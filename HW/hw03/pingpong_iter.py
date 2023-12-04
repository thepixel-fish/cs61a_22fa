def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    """
    def switch(flag):
        if flag == 1:
            return lambda n: n + 1
        else:
            return lambda n: n - 1
    meet = lambda : i % 8 == 0 or num_eights(i) != 0
    
    turn = switch(1)
    i, flag = 1, 0
    pong = 0
    while i <= n:
        pong = turn(pong)
        if meet():
            turn = switch(flag)
            flag = 1 - flag
        i = i + 1
    return pong

def num_eights(pos):
    if pos == 0:
        return 0
    elif pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    else:
        return 0 + num_eights(pos // 10)