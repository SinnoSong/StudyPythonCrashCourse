def make_sandwich(*toppings):
    msg = "toppings:"
    for topping in toppings:
        msg += topping+", "
    return msg


print(make_sandwich("test", "test2"))
