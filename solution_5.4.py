""" 
    solution_5.4.py -- Decorator Function
    Author: Timothy McCarthy
    Revised Date: 07-01-2023
"""

import time

def logfunc(func):
    def wrapper(*args, **kwargs):
        
        arglist = [f"'{arg}'" for arg in args]                                            
        arglist += [f"{arg[0]}='{arg[1]}'" for arg in kwargs.items()]
        full_arg_str = ', '.join(arglist)

        print(f'{time.ctime()}'
              f' entering {func.__name__}({full_arg_str})')

        retval = func(*args, **kwargs)
        
        print(f'{time.ctime()} leaving {func.__name__}()')
        return retval
    
    return wrapper

@logfunc
def greet(greeting, place='world'):
    time.sleep(2)
    return f'{greeting}, {place}'

msg = greet('hello')            # prints:  Fri Jul 10 17:07:37 2020  entering greet(('hello',), {})
                                #          Fri Jul 10 17:09:37 2020  leaving greet()

print(msg)                      # hello, world!

msg2 = greet('goodbye', place='Mars')  # prints:  Fri Jul 10 17:07:37 2020  entering greet(('goodbye',),
                                       #                                    {'place': 'Mars'})
                                       #          Fri Jul 10 17:09:37 2020  leaving greet()

print(msg2) 
