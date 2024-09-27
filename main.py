import datetime

class BikeShop:
    def __init__(self, stock):
        self.stock = stock
        self.hourly_rate = 5    # $5 per hour
        self.daily_rate = 20    # $20 per day
        self.weekly_rate = 60   # $60 per week

    def display_stock(self):
        """Display the total number of bikes available for rent."""
        print(f"Total available bikes: {self.stock}")

    def rent_bike(self, request, customer):
        """
        Rent a bike based on the customer's request.
        request: 1 for hourly, 2 for daily, 3 for weekly
        customer: the customer object that is renting the bike.
        """
        if request == 1:
            customer.rental_time = datetime.datetime.now()
            customer.rental_basis = 'hourly'
            print(f"You rented a bike on an hourly basis at {self.hourly_rate}/hour.")
        elif request == 2:
            customer.rental_time = datetime.datetime.now()
            customer.rental_basis = 'daily'
            print(f"You rented a bike on a daily basis at {self.daily_rate}/day.")
        elif request == 3:
            customer.rental_time = datetime.datetime.now()
            customer.rental_basis = 'weekly'
            print(f"You rented a bike on a weekly basis at {self.weekly_rate}/week.")
        else:
            print("Invalid rental option.")
            return

        if customer.quantity <= 0 or customer.quantity > self.stock:
            print("Invalid quantity. Please select a quantity between 1 and available stock.")
            return

        self.stock -= customer.quantity
        print(f"Rented {customer.quantity} bike(s). Remaining stock: {self.stock}")

    def return_bike(self, customer):
        """
        Return the bike and calculate the rental bill based on the time spent.
        customer: the customer object returning the bike.
        """
        if customer.rental_time is None:
            print("You did not rent a bike.")
            return

        now = datetime.datetime.now()
        rental_period = now - customer.rental_time

        # Calculate rental cost
        if customer.rental_basis == 'hourly':
            bill = round(rental_period.total_seconds() / 3600) * self.hourly_rate * customer.quantity
        elif customer.rental_basis == 'daily':
            bill = round(rental_period.total_seconds() / 86400) * self.daily_rate * customer.quantity
        elif customer.rental_basis == 'weekly':
            bill = round(rental_period.total_seconds() / 604800) * self.weekly_rate * customer.quantity
        else:
            print("Error in rental basis.")
            return

        self.stock += customer.quantity
        print(f"Total bill: ${bill}")
        print(f"Thank you for returning the bike(s). Updated stock: {self.stock}")

        # Reset customer details
        customer.reset_rental()

class Customer:
    def __init__(self):
        self.quantity = 0
        self.rental_basis = None
        self.rental_time = None

    def request_bike(self):
        """
        Ask the user how many bikes they would like to rent.
        """
        self.quantity = int(input("How many bikes would you like to rent? "))
        return self.quantity

    def reset_rental(self):
        """
        Reset the customer's rental details after returning a bike.
        """
        self.quantity = 0
        self.rental_basis = None
        self.rental_time = None

def main():
    shop = BikeShop(100)
    customer = Customer()

    while True:
        print('''
        ===== Bike Rental Shop =====
        1. Display available bikes
        2. Rent a bike
        3. Return a bike
        4. Exit
        ''')
        choice = int(input("Enter your choice: "))

        if choice == 1:
            shop.display_stock()
        
        elif choice == 2:
            customer.request_bike()
            rental_type = int(input("Rent bike on (1: Hourly, 2: Daily, 3: Weekly): "))
            shop.rent_bike(rental_type, customer)
        
        elif choice == 3:
            shop.return_bike(customer)
        
        elif choice == 4:
            print("Thank you for using the Bike Rental Shop!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
