from tabulate import tabulate


# Task-1
def ticket_booking(availableTicket, noOfBookingTicket):
    if availableTicket >= noOfBookingTicket:
        return f"{noOfBookingTicket} Tickets are available"
    else:
        return f"Sorry, Tickets are not Available"


availableTicket = int(input("Enter the no of tickets available: "))
noOfBookingTicket = int(input("Enter the no of Tickets you want to book: "))
print(ticket_booking(availableTicket, noOfBookingTicket))


# task-2
def ticket_booking_cost(availableTicket, noOfBookingTicket):
    base_ticket_price = 100
    if availableTicket >= noOfBookingTicket:
        print(
            """Tickets are available , please Select The required ticket from the following
                1.Silver
                2.Gold
                3.Diamond
                """
        )
        ticket = int(input("Select the ticket type: "))
        if ticket == 1:
            total_cost_of_tickets = noOfBookingTicket * base_ticket_price
            return f"Total Cost of tickets is {total_cost_of_tickets} "
        elif ticket == 2:
            base_ticket_price += 20
            total_cost_of_tickets = noOfBookingTicket * base_ticket_price
            return f"Total Cost of tickets is {total_cost_of_tickets} "
        elif ticket == 3:
            base_ticket_price += 50
            total_cost_of_tickets = noOfBookingTicket * base_ticket_price
            return f"Total Cost of tickets is {total_cost_of_tickets} "
        else:
            return f"Sorry , Select the appropriate ticket type"
    else:
        return f"Sorry, Tickets are not Available"


availableTicket = int(input("Enter the no of tickets available: "))
noOfBookingTicket = int(input("Enter the no of Tickets you want to book: "))
print(ticket_booking_cost(availableTicket, noOfBookingTicket))


# TAsk-3
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


# Task-4
class Event:
    def calculate_total_revenue(self):
        try:
            self.cursor.execute(
                "SELECT Event_Id,Total_seats,available_seats,ticket_price FROM Event"
            )
            event_data = [list(row) for row in self.cursor.fetchall()]
            revenue_data = []
            if event_data:
                for row in event_data:
                    event_id, total_seats, available_seats, ticket_price = row
                    total_revenue = (total_seats - available_seats) * ticket_price
                    revenue_data.append((event_id, total_revenue))
                headers = [event_id, revenue_data]
                print("Total revenue generated from the tickets is:")
                print(tabulate(revenue_data, headers=headers, tablefmt="grid"))
            else:
                pass  # raise error
        except Exception as e:
            print("OOPS Error Happened: ", e)

    def getBookedNoOfTickets(self):
        self.cursor.execute("SELECT EVENT_ID,TOTAL_SEATS,AVAILABLE_SEATS FROM Event")
        event_data = [list(row) for row in self.cursor.fetchall()]
        booked_data = []
        for row in event_data:
            event_id, total_seats, available_seats = row
            booked_tickets = total_seats - available_seats
            booked_data.append((event_id, booked_tickets))
        headers = [event_id, booked_data]
        print(tabulate(booked_data, headers=headers, tablefmt="grid"))

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully for {self.event_name}")
        else:
            print("Sorry, Seats are unavailable")

    def cancel_booking(self, num_tickets):
        if num_tickets <= (self.total_seats - self.available_seats):
            self.available_seats += num_tickets
            print(f"{num_tickets} tickets cancelled successfully for {self.event_name}")

        else:
            print("Invalid no of seats to cancel")

    def display_event_details(self, Event):
        try:
            self.cursor.execute("SELECT * FROM EVENT")
            event_data = [list(row) for row in self.cursor.fetchall()]
            headers = [
                "event_id",
                "Event_name",
                "event_date",
                "Event_time",
                "venue_id",
                "total_seats",
                "available_seats",
                "ticket_price",
                "event_type",
            ]
            if event_data:
                print(tabulate(event_data, headers=headers, tablefmt="grid"))
            else:
                pass
                # raise Error
        except Exception as e:
            print("OOPS Error Happened: ", e)


class Venue:
    def display_venue_details(self):
        try:
            self.cursor.execute("SELECT * FROM Venue")
            venue_data = [list(row) for row in self.cursor.fetchall()]
            headers = ["Venue_id", "Venue_name", "Address"]
            if venue_data:
                print(tabulate(venue_data, headers=headers, tablefmt="grid"))
            else:
                pass  # raise exception
        except Exception as e:
            print("OOPS Error Happened: ", e)


class Customer:
    def display_customer_details(self):
        try:
            self.cursor.execute("SELECT * FROM Customer")
            customer_data = [list(row) for row in self.cursor.fetchall()]
            headers = ["Customer_name", "email", "phone_number"]
            if customer_data:
                print(tabulate(customer_data, headers=headers, tablefmt="grid"))
            else:
                pass  # raise exception
        except Exception as e:
            print("OOPS Error Happened: ", e)


class Booking:
    def calculate_booking_cost(self, num_tickets):
        total_cost = num_tickets * self.ticket_price
        return total_cost

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            return f"{num_tickets} tickets booked successfully for {self.event_name}"
        return f"Sorry , tickets are unavailable"

    def cancel_booking(self, num_tickets):
        if (self.total_seats - self.available_seats) >= num_tickets:
            self.available_seats += num_tickets
            return f"{num_tickets} tickets cancelled successfully for {self.event_name}"
        return f"Sorry, Invalid no of tickets"

    def get_available_no_of_tickets(self):
        return f"the tickets available are {self.available_seats}"

    def get_event_details(self):
        try:
            self.cursor.execute("SELECT * FROM Booking")
            booking_data = [list(row) for row in self.cursor.fetchall()]
            headers = [
                "booking_id",
                "customer_id",
                "event_id",
                "num_of_tickets",
                "total_cost",
                "booking_date",
            ]
            if booking_data:
                print(tabulate(booking_data, headers=headers, tablefmt="grid"))
            else:
                pass  # raise exception
        except Exception as e:
            print("OOPS Error Happened: ", e)


class Movie(Event):
    def display_event_details(self):
        print(f"Event: {self.event_name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Genre: {self.genre}")
        print(f"Actor: {self.actor_name}")
        print(f"Actress: {self.actress_name}")

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for {self.event_name}.")
        else:
            print("Sorry, the event is sold out.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")


class Concert(Event):
    def __init__(
        self,
        event_name,
        date,
        time,
        total_seats,
        ticket_price,
        event_type,
        venue_name,
        artist,
        concert_type,
    ):
        super().__init__(
            event_name, date, time, total_seats, ticket_price, event_type, venue_name
        )
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        print(f"Event: {self.event_name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Artist: {self.artist}")
        print(f"Concert Type: {self.concert_type}")

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for {self.event_name}.")
        else:
            print("Sorry, the event is sold out.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")


class Sport(Event):
    def __init__(
        self,
        event_name,
        date,
        time,
        total_seats,
        ticket_price,
        event_type,
        venue_name,
        sport_name,
        teams_name,
    ):
        super().__init__(
            event_name, date, time, total_seats, ticket_price, event_type, venue_name
        )
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        print(f"Event: {self.event_name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Sport: {self.sport_name}")
        print(f"Teams: {self.teams_name}")

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for {self.event_name}.")
        else:
            print("Sorry, the event is sold out.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")


class BookingSystem:
    def __init__(self):
        self.events = []

    def create_event(
        self,
        event_name,
        event_date,
        event_time,
        total_seats,
        ticket_price,
        event_type,
        venue_name,
    ):
        event = None
        if event_type.lower() == "movie":
            event = Movie(
                event_name,
                event_date,
                event_time,
                venue_name,
                total_seats,
                ticket_price,
                event_type,
            )
        elif event_type.lower() == "concert":
            event = Concert(
                event_name,
                event_date,
                event_time,
                venue_name,
                total_seats,
                ticket_price,
                event_type,
            )
        elif event_type.lower() == "sport":
            event = Sport(
                event_name,
                event_date,
                event_time,
                venue_name,
                total_seats,
                ticket_price,
                event_type,
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
