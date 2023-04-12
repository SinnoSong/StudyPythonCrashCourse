def make_car(vendor,model,**map):
    map['vendor'] = vendor
    map['model'] = model
    return map

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)