"""
Get a dollar amount and an integer from the user. 
Sort the dollar amount into [integer] number of piles, and if there is a remainder, include it.
So if dollar = 25 and int = 2, the output will be: 12, 12, 1. 
"""

def get_dollar():
    dollar_input = input("Please enter a dollar amount: ").strip()
    if "$" in dollar_input:
        dollar_input = dollar_input.replace("$", '')
    try:
        # Normally, it's a Very Bad Idea to use floats for currency in Python, but
        # for the purposes of this exercise, it should be fine.
        dollar_float = float(dollar_input)
        return dollar_float
    except:
        print(f"{dollar_input} is not a valid dollar amount.")
        dollar_float = get_dollar()
        return dollar_float

def get_int():
    integer_input = input("Please enter a whole number, without decimals: ").strip()
    if not integer_input.isnumeric() or integer_input == '0':
        print(f"{integer_input} is not a valid integer.")
        integer_value = get_int()
        return integer_value
    else: 
        integer_value = int(integer_input)
        return integer_value
            
def create_array():
    d = get_dollar()
    i = get_int()
    div = int(d // i)
    mod = int(d % i)
    div_list = []
    count = 0
    while count < i: 
        div_list.append(div)
        count += 1
    if mod != 0:
        div_list.append(mod)
    for item in div_list:
        print(item, sep='\n')

create_array()