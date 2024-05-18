from datetime import datetime


def ticket_booking_cost(availableTicket):
    total_cost_of_tickets = 0
    while True:
        noOfBookingTicket = int(input("Enter the no of Tickets you want to book: "))
        ticket = int(
            input(
                """Tickets are available , please Select The required ticket from the following
                    1.Silver
                    2.Gold
                    3.Diamond
                    4.EXIT
                    """
            )
        )
        if availableTicket >= noOfBookingTicket:
            if ticket == 1:
                base_ticket_price = 100
            elif ticket == 2:
                base_ticket_price = 120
            elif ticket == 3:
                base_ticket_price = 150
            elif ticket == 4:
                print(f"Thank you for visiting our ticket booking system")
                break
            else:
                print(f"Sorry , Select the appropriate ticket type")
                continue
            cost_of_tickets = noOfBookingTicket * base_ticket_price
            total_cost_of_tickets += noOfBookingTicket * base_ticket_price
            print(f"Total cost of tickets is {cost_of_tickets}")
            availableTicket -= noOfBookingTicket
        else:
            print(f"Sorry, Tickets are not Available")
            break
    return f"total cost of tickets is {total_cost_of_tickets}"


availableTicket = 20
print(ticket_booking_cost(availableTicket))

from datetime import datetime


class TicketBookingSystem:
    def __init__(self):
        self.events = []

    def create_event(
        self, event_name, date, time, total_seats, ticket_price, event_type, venue_name
    ):
        event = Event(
            event_name, date, time, total_seats, ticket_price, event_type, venue_name
        )
        self.events.append(event)
        return event

    def display_event_details(self, event):
        event.display_event_details()

    def book_tickets(self, event, num_tickets):
        if event.available_seats >= num_tickets:
            event.book_tickets(num_tickets)
            return event.ticket_price * num_tickets
        else:
            print("Sorry, the event is sold out.")
            return 0

    def cancel_tickets(self, event, num_tickets):
        event.cancel_booking(num_tickets)

    def main(self):
        while True:
            print("\n1. View Events")
            print("2. Book Tickets")
            print("3. Cancel Tickets")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_events()
            elif choice == "2":
                self.book_ticket_menu()
            elif choice == "3":
                self.cancel_ticket_menu()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_events(self):
        for event in self.events:
            self.display_event_details(event)

    def book_ticket_menu(self):
        event_name = input("Enter event name: ")
        num_tickets = int(input("Enter number of tickets to book: "))

        event = self.find_event_by_name(event_name)
        if event:
            cost = self.book_tickets(event, num_tickets)
            if cost > 0:
                print(
                    f"Successfully booked {num_tickets} tickets for {event_name}. Total cost: {cost}"
                )
        else:
            print("Event not found.")

    def cancel_ticket_menu(self):
        event_name = input("Enter event name: ")
        num_tickets = int(input("Enter number of tickets to cancel: "))

        event = self.find_event_by_name(event_name)
        if event:
            self.cancel_tickets(event, num_tickets)
            print(f"Successfully canceled {num_tickets} tickets for {event_name}.")
        else:
            print("Event not found.")

    def find_event_by_name(self, event_name):
        for event in self.events:
            if event.event_name.lower() == event_name.lower():
                return event
        return None


class Event:
    def __init__(
        self, event_name, date, time, total_seats, ticket_price, event_type, venue_name
    ):
        self.event_name = event_name
        self.date = date
        self.time = time
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
        self.venue_name = venue_name

    def display_event_details(self):
        print(f"Event: {self.event_name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")


ticket_booking_system = TicketBookingSystem()
ticket_booking_system.main()


class TicketBookingSystem(BookingSystem):
    def __init__(self):
        self.events = []

    def create_event(
        self, event_name, date, time, total_seats, ticket_price, event_type, venue_name
    ):
        # Logic to create event of appropriate type based on event_type
        if event_type.lower() == "movie":
            event = Movie(
                event_name,
                date,
                time,
                total_seats,
                ticket_price,
                event_type,
                venue_name,
                "Action",
                "Actor",
                "Actress",
            )
        elif event_type.lower() == "concert":
            event = Concert(
                event_name,
                date,
                time,
                total_seats,
                ticket_price,
                event_type,
                venue_name,
                "Artist",
                "Rock",
            )
        elif event_type.lower() == "sport":
            event = Sport(
                event_name,
                date,
                time,
                total_seats,
                ticket_price,
                event_type,
                venue_name,
                "Football",
                "India vs Pakistan",
            )
        else:
            print("Invalid event type.")
            return None

        self.events.append(event)
        return event

    def display_event_details(self, event):
        event.display_event_details()

    def book_tickets(self, event, num_tickets):
        event.book_tickets(num_tickets)

    def cancel_tickets(self, event, num_tickets):
        event.cancel_booking(num_tickets)

    def main(self):
        while True:
            print("\n")


from datetime import datetime


class Venue:
    def __init__(self, venue_name, address):
        self.venue_name = venue_name
        self.address = address

    def display_venue_details(self):
        print(f"Venue Name: {self.venue_name}")
        print(f"Address: {self.address}")


class Event:
    def __init__(
        self,
        event_name,
        event_date,
        event_time,
        venue,
        total_seats,
        ticket_price,
        event_type,
    ):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
        self.bookings = []

    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Event Time: {self.event_time}")
        print(f"Venue: {self.venue.venue_name}")
        print(f"Available Seats: {self.available_seats}/{self.total_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type}")

    def calculate_total_revenue(self):
        return (self.total_seats - self.available_seats) * self.ticket_price

    def get_booked_no_of_tickets(self):
        return sum(booking["num_tickets"] for booking in self.bookings)

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            return True
        else:
            return False

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets

    def add_booking(self, customer, num_tickets):
        self.bookings.append({"customer": customer, "num_tickets": num_tickets})


class Movie(Event):
    pass


class Concert(Event):
    pass


class Sport(Event):
    pass


class Customer:
    def __init__(self, customer_name, email, phone_number):
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def display_customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")


class Booking:
    booking_id = 0

    def __init__(self, event, num_tickets, customer):
        Booking.booking_id += 1
        self.booking_id = Booking.booking_id
        self.event = event
        self.num_tickets = num_tickets
        self.customer = customer
        self.total_cost = event.ticket_price * num_tickets
        self.booking_date = datetime.now()

    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"Event: {self.event.event_name}")
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Total Cost: {self.total_cost}")
        print(f"Booking Date: {self.booking_date}")
        self.customer.display_customer_details()


class BookingSystem:
    def __init__(self):
        self.events = []

    def create_event(
        self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name
    ):
        event = None
        if event_type.lower() == "movie":
            event = Movie(
                event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type
            )
        elif event_type.lower() == "concert":
            event = Concert(
                event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type
            )
        elif event_type.lower() == "sport":
            event = Sport(
                event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type
            )
        else:
            print("Invalid event type.")
        if event:
            self.events.append(event)
        return event

    def calculate_booking_cost(self, num_tickets, event):
        return num_tickets * event.ticket_price

    def book_tickets(self, event_name, num_tickets, customers):
        for event in self.events:
            if event.event_name == event_name:
                if event.book_tickets(num_tickets):
                    for customer in customers:
                        event.add_booking(customer, num_tickets)
                    print(f"{num_tickets} tickets booked for {event_name}.")
                else:
                    print("Sorry, not enough available seats.")
                return
        print("Event not found.")

    def cancel_booking(self, booking_id):
        for event in self.events:
            for booking in event.bookings:
                if booking["booking"].booking_id == booking_id:
                    event.cancel_booking(booking["num_tickets"])
                    event.bookings.remove(booking)
                    print(f"Booking {booking_id} canceled.")
                    return
        print("Booking not found.")

    def get_available_no_of_tickets(self):
        return sum(event.available_seats for event in self.events)

    def get_event_details(self):
        for event in self.events:
            event.display_event_details()

    def main(self):
        while True:
            print("\nWelcome to the Ticket Booking System")
            print("1. Create Event")
            print("2. Book Tickets")
            print("3. Cancel Booking")
            print("4. Get Available Seats")
            print("5. Get Event Details")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                event_name = input("Enter event name: ")
                date = input("Enter event date (YYYY-MM-DD): ")
                time = input("Enter event time (HH:MM): ")
                total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (Movie/Sport/Concert): ")
                venue_name = input("Enter venue name: ")
                address = input("Enter venue address: ")
                venue = Venue(venue_name, address)
                self.create_event(
                    event_name, date, time, total_seats, ticket_price, event_type, venue
                )
            elif choice == 2:
                event_name = input("Enter event name: ")
                num_tickets = int(input("Enter number of tickets: "))
                customer_name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                phone_number = input("Enter customer phone number: ")
                customer = Customer(customer_name, email, phone_number)
                self.book_tickets(event_name, num_tickets, [customer])
            elif choice == 3:
                booking_id = int(input("Enter booking ID: "))
                self.cancel_booking(booking_id)
            elif choice == 4:
                print("Available Seats:", self.get_available_no_of_tickets())
            elif choice == 5:
                self.get_event_details()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice.")


# if __name__ == "__main__":
#     total_seats = 200
#     available_seats = total_seats
#     ticket_price = 300
#     Salaar = Event(
#         "Salaar",
#         datetime(2023, 5, 5),
#         datetime.strptime("18:00", "%H:%M"),
#         "Cineplex",
#         total_seats,
#         available_seats,
#         ticket_price,
#         Event_type.Movie,
#     )
#     Salaar1 = Booking(
#         "Salaar",
#         datetime(2023, 5, 5),
#         datetime.strptime("18:00", "%H:%M"),
#         "Cineplex",
#         total_seats,
#         available_seats,
#         ticket_price,
#         Event_type.Movie,
#     )
#     Salaar.display_event_details()
#     Salaar.book_tickets(10)
#     print(Salaar.getBookedNoOfTickets())
#     print(Salaar.calculate_total_revenue())
#     Salaar.cancel_booking(5)
#     Salaar.display_event_details()
#     venue1 = Venue("Multiplex Mayajaal", "Chennai,Tamilnadu")
#     venue1.display_venue_details()
#     James = Customer("James", "James@gmail.com", 7458764567)
#     James.display_customer_details()
#     print(Salaar1.book_tickets(5))
#     print(Salaar1.calculate_booking_cost(5))
#     print(Salaar1.cancel_booking(4))
#     print(Salaar1.getAvaialableNoOfTickets())
#     Salaar1.getEventDetails()
#     prabhas = Movie(
#         "Salaar",
#         datetime(2023, 5, 5),
#         datetime.strptime("18:00", "%H:%M"),
#         "Cineplex",
#         total_seats,
#         available_seats,
#         ticket_price,
#         Event_type.Movie,
#         "Action",
#         "Prabhas",
#         "Shrithi Hassan",
#     )
#     print(prabhas.display_movie_details())

#     TaylorSwift = Concert(
#         "The Eras Tour",
#         datetime(2024, 6, 13),
#         datetime.strptime("14:00", "%H:%M"),
#         "SoFi Stadium",
#         total_seats,
#         available_seats,
#         ticket_price,
#         Event_type.Concert,
#         "TaylorSwift",
#         "Rock",
#     )
#     print(TaylorSwift.display_concert_details())

#     Cricket = Sports(
#         "T20",
#         datetime(2023, 6, 9),
#         datetime.strptime("20:00", "%H:%M"),
#         "Eisenhower park",
#         total_seats,
#         available_seats,
#         ticket_price,
#         Event_type.Sports,
#         "Cricket",
#         "IND Vs PAK",
#     )

#     print(Cricket.display_sport_details())
