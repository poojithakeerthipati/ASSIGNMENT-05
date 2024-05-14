from enum import Enum
from datetime import datetime


class Event_type(Enum):
    Movie = 1
    Sports = 2
    Concert = 3


class Event:
    def __init__(
        self,
        event_name,
        event_date,
        event_time,
        venue_name,
        total_seats,
        available_seats,
        ticket_price,
        event_type,
    ):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def calculate_total_revenue(self):
        print("Total revenue generated from the tickets is: ")
        return (self.total_seats - self.available_seats) * self.ticket_price

    def getBookedNoOfTickets(self):
        print("Total tickets booked are: ")
        return self.total_seats - self.available_seats

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

    def display_event_details(self):
        print(f"Event name is: {self.event_name}")
        print("Event date is : ", self.event_date.strftime("%d-%m-%Y"))
        print("Event_time is : ", self.event_time.strftime("%H:%M"))
        print(f"Venue_name is : {self.venue_name}")
        print(f"Total seats are : {self.total_seats}")
        print(f"Available seats are : {self.available_seats}")
        print(f"price of the ticket is : {self.ticket_price}")
        print(f"Type of the event : {self.event_type} ")


class Venue:
    def __init__(self, venue_name, address):
        self.venue_name = venue_name
        self.address = address

    def display_venue_details(self):
        print(f"Name of the Venue: {self.venue_name}")
        print(f"Venue address : {self.address}")


class Customer:
    def __init__(self, customer_name, email, phone_number):
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def display_customer_details(self):
        print(f"Name of the Customer : {self.customer_name}")
        print(f"Customer email : {self.email}")
        print(f"phone number: {self.phone_number}")


class Booking:
    def __init__(
        self,
        event_name,
        event_date,
        event_time,
        venue_name,
        total_seats,
        available_seats,
        ticket_price,
        event_type,
    ):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

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

    def getAvaialableNoOfTickets(self):
        return f"the tickets available are {self.available_seats}"

    def getEventDetails(self):
        print(f"Event name is: {self.event_name}")
        print("Event date is : ", self.event_date.strftime("%d-%m-%Y"))
        print("Event_time is : ", self.event_time.strftime("%H:%M"))
        print(f"Venue_name is : {self.venue_name}")
        print(f"Total seats are : {self.total_seats}")
        print(f"Available seats are : {self.available_seats}")
        print(f"price of the ticket is : {self.ticket_price}")
        print(f"Type of the event : {self.event_type} ")


class Movie(Event):
    def __init__(
        self,
        event_name,
        event_date,
        event_time,
        venue_name,
        total_seats,
        available_seats,
        ticket_price,
        event_type,
        genre,
        actor_name,
        actress_name,
    ):
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name
        super().__init__(
            event_name,
            event_date,
            event_time,
            venue_name,
            total_seats,
            available_seats,
            ticket_price,
            event_type,
        )

    def display_movie_details(self):
        print(f"genre of the movie : {self.genre}")
        print(f"Movie actor: {self.actor_name}")
        print(f"Movie actress : {self.actress_name}")
        return super().display_event_details()


class Concert(Event):
    def __init__(
        self,
        event_name,
        event_date,
        event_time,
        venue_name,
        total_seats,
        available_seats,
        ticket_price,
        event_type,
        artist,
        type,
    ):
        self.artist = artist
        self.type = type
        super().__init__(
            event_name,
            event_date,
            event_time,
            venue_name,
            total_seats,
            available_seats,
            ticket_price,
            event_type,
        )

    def display_concert_details(self):
        print(f"Name of the artist: {self.artist}")
        print(f"Concert type: {self.type}")
        return super().display_event_details()


class Sports(Event):
    def __init__(
        self,
        event_name,
        event_date,
        event_time,
        venue_name,
        total_seats,
        available_seats,
        ticket_price,
        event_type,
        sports_name,
        teams_name,
    ):
        self.sport_name = sports_name
        self.teams_name = teams_name
        super().__init__(
            event_name,
            event_date,
            event_time,
            venue_name,
            total_seats,
            available_seats,
            ticket_price,
            event_type,
        )

    def display_sport_details(self):
        print(f"Name of the sport: {self.sport_name}")
        print(f"Name of the team : {self.teams_name}")
        return super().display_event_details()


if __name__ == "__main__":
    total_seats = 200
    available_seats = total_seats
    ticket_price = 300
    Salaar = Event(
        "Salaar",
        datetime(2023, 5, 5),
        datetime.strptime("18:00", "%H:%M"),
        "Cineplex",
        total_seats,
        available_seats,
        ticket_price,
        Event_type.Movie,
    )
    Salaar1 = Booking(
        "Salaar",
        datetime(2023, 5, 5),
        datetime.strptime("18:00", "%H:%M"),
        "Cineplex",
        total_seats,
        available_seats,
        ticket_price,
        Event_type.Movie,
    )
    Salaar.display_event_details()
    Salaar.book_tickets(10)
    print(Salaar.getBookedNoOfTickets())
    print(Salaar.calculate_total_revenue())
    Salaar.cancel_booking(5)
    Salaar.display_event_details()
    venue1 = Venue("Multiplex Mayajaal", "Chennai,Tamilnadu")
    venue1.display_venue_details()
    James = Customer("James", "James@gmail.com", 7458764567)
    James.display_customer_details()
    print(Salaar1.book_tickets(5))
    print(Salaar1.calculate_booking_cost(5))
    print(Salaar1.cancel_booking(4))
    print(Salaar1.getAvaialableNoOfTickets())
    Salaar1.getEventDetails()
    prabhas = Movie(
        "Salaar",
        datetime(2023, 5, 5),
        datetime.strptime("18:00", "%H:%M"),
        "Cineplex",
        total_seats,
        available_seats,
        ticket_price,
        Event_type.Movie,
        "Action",
        "Prabhas",
        "Shrithi Hassan",
    )
    print(prabhas.display_movie_details())

    TaylorSwift = Concert(
        "The Eras Tour",
        datetime(2024, 6, 13),
        datetime.strptime("14:00", "%H:%M"),
        "SoFi Stadium",
        total_seats,
        available_seats,
        ticket_price,
        Event_type.Concert,
        "TaylorSwift",
        "Rock",
    )
    print(TaylorSwift.display_concert_details())

    Cricket = Sports(
        "T20",
        datetime(2023, 6, 9),
        datetime.strptime("20:00", "%H:%M"),
        "Eisenhower park",
        total_seats,
        available_seats,
        ticket_price,
        Event_type.Sports,
        "Cricket",
        "IND Vs PAK",
    )

    print(Cricket.display_sport_details())
