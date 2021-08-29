"""
import fibo
fibo.fib(1000)
fibsi=fibo.fib
fibsi(500)
"""

"""
from fibo import fib, fib2
fib(500)
"""

"""
from fibo import *
fib(500)
"""

#  In most cases Python programmers do not use this facility
# since it introduces an unknown set of names into the interpreter,
# possibly hiding some things you have already defined.

# Note that in general the practice of importing * from a
# module or package is frowned upon, since it often causes
# poorly readable code.

"""
import fibo as fib
fib.fib(500)
import fibo as fibona
fibona.fib(500)
# fibo.fib(500) # This will not work as the name fibo is undefined
"""

"""
from fibo import fib as fibonacci
fibonacci(500)
from fibo import fib2 as fiboreturns
print(fiboreturns(1000))
"""

# Each module is imported only once per interpreter session
# To test modules interactively, use importlib.reload()
