# Define a dictionary to map month numbers to season names
season_dict = {
    1: "Winter", 2: "Winter", 3: "Spring",
    4: "Spring", 5: "Spring", 6: "Summer",
    7: "Summer", 8: "Summer", 9: "Autumn",
    10: "Autumn", 11: "Autumn", 12: "Winter"
}
month_number = int(input("Enter the month number (1-12): "))
print("Season:", season_dict.get(month_number, "Invalid month number"))
