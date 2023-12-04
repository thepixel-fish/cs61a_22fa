class link():
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is link.empty or isinstance(rest, link)
        self.first = first
        self.rest = rest


def range_link(start, end):
    if start >= end:
        return link.empty
    else:
        return link(start, link(start + 1, end))

def map_link(fn, s):
    if s.rest is link.empty:
        return link(fn(s.first))
    else:
        return link(fn(s.first), map_link(s.rest))

def filter_link(fn, s):
    if s is link.empty:
        return link.empty
    filtered_link = filter_link(s.rest)
    if fn(s.first):
        return link(s.first, filtered_link)
    else:
        return filtered_link
    
def add_link(s, v):
    """
    >>> s = link(2, link(3, link(5)))
    >>> add_link(s, 1)
    link(1, link(2, link(3, link(5))))
    """
    assert s is not link.empty
    if s.first > v:
        s.first, s.rest = v, link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = link(v)
    elif s.first < v:
        add_link(s.rest, v)
    return s