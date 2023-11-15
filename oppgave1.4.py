from modul import all_wares



def is_number_of_ware_in_stock(ware, number_of_ware):
    correct_number = False
    actual_amount_in_stock = ware['number_in_stock']
    if actual_amount_in_stock == number_of_ware:
        correct_number = True
    else:
        correct_number = False
    if correct_number == True:
        print("Correct amount in stock.")
    elif correct_number == False:
        print("Incorrect amound in stock.")


is_number_of_ware_in_stock(all_wares['amd_processor'], 50)