# Dictionary med varer
all_wares = {
"amd_processor": {
"name": "AMD Ryzen 9 5900X Processor",
"price": 5590.0,
"number_in_stock": 50,
"ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
"description": "All the cores and threads you'll need!",
},
"playstation_5": {
"name": "PlayStation 5",
"price": 5999.0,
"number_in_stock": 0,
"ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
"description": "Next generation console, never in stock!",
},
"hdmi_cable": {
"name": "Belkin Ultra High Speed HDMI Cable - 2m",
"price": 349.0,
"number_in_stock": 3,
"ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
"description": "A high speed overprices HDMI cable!",
}
}



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