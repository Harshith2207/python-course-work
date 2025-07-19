print("< * Welcome To Bus Reservation System * > \n")

Available_Buses = {
    'Morning Star': {'Route': 'Hyderabad to Eluru', 'Cost': 700, 'Seats Available': 5},
    'SVKDT': {'Route': 'Eluru to Vizag', 'Cost': 600, 'Seats Available': 6},
    'Abhi bus': {'Route': 'Vizag to Vijayanagaram', 'Cost': 200, 'Seats Available': 21},
    'Zing bus (Return)': {'Route': 'Vizianagaram to Hyderabad', 'Cost': 'Free Return', 'Seats Available': 13},
    'Zing bus': {'Route': 'Hyderabad to Vizianagram', 'Cost': 1250, 'Seats Available': 25}
}
bus_list = list(Available_Buses.items())
print("Available Buses: \n")
for i, (bus_name, details) in enumerate(bus_list):
    print(f"{i + 1}. {bus_name} ({details['Route']}) - ₹{details['Cost']} - Seats: {details['Seats Available']}")
choice = int(input("\n Enter the number of the buses you want to book: ")) - 1
if 0 <= choice < len(bus_list):
    selected_bus, details = bus_list[choice]
    print(f"\n You have selected: {selected_bus}")
    print("Route:", details['Route'])
    print("Cost:", details['Cost'])
    print("Seats Available:", details['Seats Available'])
else:
    print("Invalid selection...")
