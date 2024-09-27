Bike Rental Shop
This is a Python-based Bike Rental Shop program built using object-oriented programming. It allows customers to rent bikes on an hourly, daily, or weekly basis and calculates the rental cost accordingly. It also handles customer management, billing, and bike inventory tracking.

Features
Bike Inventory: Displays the number of available bikes in the shop.
Rental Options: Rent bikes on an hourly, daily, or weekly basis.
Hourly Rate: $5 per hour
Daily Rate: $20 per day
Weekly Rate: $60 per week
Customer Management: Tracks bike rentals for individual customers, including rental time and type.
Billing: Automatically calculates the total bill based on the rental duration.
Inventory Management: Tracks bike stock after rentals and returns.
Input Validation: Ensures that the user inputs valid choices and quantities.
Return Options: Customers can return bikes and view their rental bill.
How to Run the Program
Install Python: Ensure that Python is installed on your system. You can download it from python.org.

Download the Code: Clone or download the code from this repository to your local machine.

Run the Code: Open a terminal or command prompt, navigate to the folder where the code is saved, and run the program:

bash
python bike_rental.py
Use the Menu: Once the program starts, you will be presented with a menu:

markdown
===== Bike Rental Shop =====
1. Display available bikes
2. Rent a bike
3. Return a bike
4. Exit
Select option 1 to display the number of available bikes in the shop.
Select option 2 to rent a bike. You will be asked to choose how many bikes and for how long (hourly, daily, or weekly).
Select option 3 to return the rented bikes and view the bill.
Select option 4 to exit the program.
Code Overview
1. BikeShop Class:
Manages the bike inventory, rental process, and billing.
Rental options include hourly, daily, and weekly.
Tracks available stock and updates it as customers rent or return bikes.
2. Customer Class:
Manages the customer's rental details (quantity of bikes, rental time, and rental basis).
Stores the time at which the bikes were rented for accurate billing.
3. Main Program:
Presents a user-friendly menu for interacting with the bike rental shop.
Provides options for viewing available stock, renting bikes, and returning bikes.
Example Usage
Display Available Bikes:

The system displays the total number of bikes available for rent in the shop.
Renting a Bike:

A customer can choose to rent bikes on an hourly, daily, or weekly basis by entering their preferred option.
The system validates the quantity and ensures the customer does not rent more bikes than available.
Returning a Bike:

When returning a bike, the system calculates the bill based on the time spent renting and the rental basis (hourly, daily, or weekly).
The bill is displayed, and the bike inventory is updated accordingly.
Pricing
Hourly Rental: $5 per hour.
Daily Rental: $20 per day.
Weekly Rental: $60 per week.
Requirements
Python 3.x
License
This project is open-source and free to use for personal or educational purposes.
