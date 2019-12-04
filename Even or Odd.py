import tensorflow as tf
def even_or_odd(number):
    if (number % 2 == 1):
        print('odd')
        return 'odd'
    else: 
        print('even')
        return 'even'

even_or_odd(-1)

# # other
# def even_or_odd(number):
#   return 'Odd' if number % 2 else 'Even'