from modul import all_wares

# Funksjon for å printe ut informasjon om en vare
def print_ware_information(ware):
    print(f"""
Name: {ware['name']}
Price: {ware['price']},-
Number in stock: {ware['number_in_stock']}
Description: {ware['description']}""")
    
# Funksjonen brukes
print_ware_information(all_wares['hdmi_cable'])