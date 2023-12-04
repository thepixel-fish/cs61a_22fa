def make_instance(clss):
    """make a class instance"""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = clss['get'](name)
            return bind_method(instance, value)
    def set_value(name, value):
        attributes[name] = value
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance

def bind_method(instance, value):
    """binding function to instance as method"""
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value

def init_instance(clss, *args):
    """Return a instance with cls __init__ effacted."""
    instance = make_instance(clss)
    init = clss['get']('__init__')
    if init:
        init(instance, *args)
    return instance

def make_class(attributes, base_class=None):
    """Just a class make function to make a class with some attributes.
        Not __init__, not particular method in it.
    """
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
    def new(*args):
        return init_instance(clss, *args)
    clss = {'get': get_value, 'set': set_value, 'new': new}
    return clss

    ##########################
    ## make a bank instance ##
    ##########################

# Account class
def make_account_class():
    """Return a Account class"""
    interest = 0.02
    def __init__(selff, holder, balance=0):
        selff['set']('holder', holder)
        selff['set']('balance', balance)
    def deposit(selff, amount):
        new_balance = selff['get']('balance') + amount
        selff['set']('balance', new_balance)
        return selff['get']('balance')
    def withdraw(selff, amount):
        balance = selff['get']('balance')
        if amount > balance:
            print('Insufficient fund!')
        else:
            selff['set']('balance', balance - amount)
            return selff['get']('balance')
    return make_class(locals())
Account = make_account_class()

kirk_account = Account['new']('krik')

def make_smartaccount_class():
    deposit_fee = 1
    withdraw_fee = 2
    interest = 0.01
    def __init__(selff, holder, balance=0):#对象也需要上传至祖类中，才可以使用祖类的方法
        return Account['get']('__init__')(selff, holder, balance + 1)
    def deposit(selff, amount): #参数传入数量不对应 DEBUG：1
        fee = selff['get']('deposit_fee')
        return Account['get']('deposit')(selff, amount - fee)
    def withdraw(selff, amount):
        fee = selff['get']('withdraw_fee')
        return Account['get']('withdraw')(selff, amount + fee)
    return make_class(locals(), Account)
SmartAccount = make_smartaccount_class()