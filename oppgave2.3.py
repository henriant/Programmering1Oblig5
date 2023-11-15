from datetime import date

def get_car_age(car):
    car_year = car['year']
    current_date = date.today()
    current_year = current_date.year
    car_age = current_year - car_year
    return car_age

