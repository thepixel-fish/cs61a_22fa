def dictionary():
    dict = []
    def getitem(key):
        match = [i for i in dict if key == i[0]]
        if len(match) == 1:
            key, value = match[0]
        return value
    def setitem(key, value):
        nonlocal dict
        non_match = [i for i in dict if key != i[0]]
        dict = non_match + [[key, value]]
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch

def account(init_balance):
    """initial a bank account."""
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if dispatch['balance'] < amount:
            return 'Insufficient funds.'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit': deposit, 'withdraw': withdraw, 
                'balance': init_balance}
    return dispatch

def deposit(account, amount):
    return account['deposit'](amount)
def withdraw(account, amount):
    return account['withdraw'](amount)
def check_account(account):
    return account['balance']