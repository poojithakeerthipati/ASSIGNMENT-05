import pyodbc
from tabulate import tabulate
from DAO import VenueService, CustomerService, EventService, BookingService


class MainMenu:
    venue_service = VenueService()
    customer_service = CustomerService()
    event_service = EventService()
    booking_service = BookingService()

    def booking_menu(self):
        while True:
            print(
                """
                  1.Calculate Booking Cost
                  2.Book the tickets
                  3.Cancel Booking
                  4.Get available Tickets
                  5.Display Event Details
                  6.Exit"""
            )
            choice = int(input("Please choose from above options:"))
            if choice == 1:
                event_id = input(
                    "Enter the event id which you want to book your tickets:"
                )
                num_tickets = int(input("Enter no of tickets to book :"))
                self.booking_service.calculate_booking_cost(event_id, num_tickets)
            elif choice == 2:
                event_id = input(
                    "Enter the event id which you want to book your tickets:"
                )
                num_tickets = int(input("Enter no of tickets to book :"))
                print(self.booking_service.book_tickets(event_id, num_tickets))
            elif choice == 3:
                event_id = input(
                    "Enter the event id which you want to book your tickets:"
                )
                num_tickets = int(input("Enter no of tickets to book :"))
                print(self.booking_service.cancel_booking(event_id, num_tickets))
            elif choice == 4:
                event_id = input(
                    "Enter the event id which you want to book your tickets:"
                )
                print(self.booking_service.get_available_no_of_tickets(event_id))
            elif choice == 5:
                self.booking_service.get_event_details()
            elif choice == 6:
                break
            else:
                print("Sorry Please Enter a valid option")

    def venue_menu(self):
        while True:
            print(
                """
                  1. Get Venue Details
                  2.EXIT"""
            )
            choice = int(input("Please choose from above options:"))
            if choice == 1:
                self.venue_service.display_venue_details()
            elif choice == 2:
                break
            else:
                print("Sorry Please Enter a valid option")

    def customer_menu(self):
        while True:
            print(
                """
                  1. Get Customer Details
                  2.EXIT"""
            )
            choice = int(input("Please choose from above options:"))
            if choice == 1:
                self.customer_service.display_customer_details()
            elif choice == 2:
                break
            else:
                print("Sorry Please Enter a valid option")

    def event_menu(self):
        while True:
            print(
                """
                  1.calculate total revenue
                  2.Get Booked Tickets
                  3.Display event Details
                  4.EXIT
                
            """
            )
            choice = int(input("Please choose from above options:"))
            if choice == 1:
                self.event_service.calculate_total_revenue()
            elif choice == 2:
                self.event_service.get_booked_no_of_tickets()
            elif choice == 3:
                self.event_service.display_event_details()
            elif choice == 4:
                break
            else:
                print("Sorry Please Enter a valid option")


def main():
    main_menu = MainMenu()

    while True:
        print(
            """
              1.Booking Management
              2.Event Management
              3.Venue Management
              4.Customer Management
              5.EXIT"""
        )
        choice = int(input("Please choose from above options:"))
        if choice == 1:
            main_menu.booking_menu()
        elif choice == 2:
            main_menu.event_menu()
        elif choice == 3:
            main_menu.venue_menu()
        elif choice == 4:
            main_menu.customer_menu()
        elif choice == 5:
            main_menu.booking_service.close()
            main_menu.event_service.close()
            main_menu.customer_service.close()
            main_menu.venue_service.close()
            break


if __name__ == "__main__":
    print("Welcome to the ticket booking app")
    main()
