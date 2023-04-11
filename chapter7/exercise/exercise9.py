sandwich_orders = ['pastrami', 'sandwich1',
                   'pastrami', 'pastrami', 'sandwich2']
print("pastrami has no one")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
