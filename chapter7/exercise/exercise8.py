sandwich_orders = ['sandwich1', 'sandwich2']
finished_sandwiched = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your tuna {sandwich}")
    finished_sandwiched.append(sandwich)
print(finished_sandwiched)
