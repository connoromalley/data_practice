# this file is just working along with ch8

# mixing positional and arbitrary arguments

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'pepperoni')
