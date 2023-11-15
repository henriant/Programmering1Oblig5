from modul import all_wares

# Selve funksjonen
def calculate_average_ware_rating(ware):
    ratings = ware['ratings']
    amount_of_ratings = len(ware['ratings'])
    sum_ratings = sum(ratings)
    try:
        average_rating = float(sum_ratings / amount_of_ratings)
        print(f"The average rating for {ware['name']} is {round(average_rating, 1)}.")
    except ZeroDivisionError:
        print("The list seems to be empty!")

# Funksjonen brukes
calculate_average_ware_rating(all_wares['amd_processor'])
