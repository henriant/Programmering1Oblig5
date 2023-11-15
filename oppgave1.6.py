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

shopping_cart = {}

def calculate_shopping_cart_price(shopping_cart, all_wares, tax = 0.25):
    calculate_tax = all_wares['price'] * tax
    total_price = all_wares['price'] + calculate_tax
    shopping_cart['{ware}'] = all_wares['name']
    shopping_cart['{price}'] = total_price
    print(f"{shopping_cart}")

calculate_shopping_cart_price(shopping_cart, all_wares['amd_processor'])
