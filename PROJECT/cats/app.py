from flask import Flask
app = Flask(__name__)

#错误代码
def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.
    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """

    """ use in;;相同部分1修改, 修改>2的时候再处理之前的1"""
    print("DEBUG:", not start or not goal)
    if limit < 0:
        return 0
    if not start and not goal:  # Fill in the condition
        # BEGIN
        return 0
        # END
    elif not start or not goal:  # Feel free to remove or add additional cases
        # BEGIN
        return (abs(len(start) - len(goal)))
        # END)
    elif start[0] == goal[0]:
        return limit - minimum_mewtations(start[1:], goal[1:], limit) - 1
    else:
        add = lambda s, i, c: s[:i] + c + s[i:len(s)]   # Fill in these lines
        remove = lambda s, i: s[:i] + s[i + 1:len(s)]
        substitute = lambda s, i, c: s[:i] + c + s[i + 1:len(s)]
        # BEGIN
        if not start[1:] or not goal[1:]:
            return minimum_mewtations(start[1:], goal[1:], limit)
        elif start[0] == goal[1]:
            start = add(start, 0, goal[0])
            print("DEBUG:","SUB", start[0], start)
            return limit - minimum_mewtations(start[1:], goal[1:], limit - 1)
        elif start[1] == goal[0]:
            start = remove(start, 0)
            print("DEBUG:","RM", start[0], start)
            return limit - minimum_mewtations(start[1:], goal[1:], limit - 1)
        else:
            start = substitute(start, 0, goal[0])
            print("DEBUG:","SUB", start[0], start)
            return limit - minimum_mewtations(start[1:], goal[1:], limit - 1)