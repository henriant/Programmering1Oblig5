def create_car(car_register, brand, model, price, year, month, new, km):
    car_dictionary = {
        car_register: {
            "brand" : brand,
            "model" : model,
            "price" : price,
            "year" : year,
            "month" : month,
            "new" : new,
            "km" : km
        }
    }
    return car_dictionary

