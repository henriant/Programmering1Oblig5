def rent_car_monthly_price(car):
    car_price = car['price']
    yearly_rent_price = car['price'] * 0.4
    monthly_rent_price = yearly_rent_price / 12
    if car['new'] == True:
        monthly_rent_price = monthly_rent_price + 1000
    return car_price