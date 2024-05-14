# Control structure
## Task 1: Conditional Statements
- In a BookingSystem, you have been given the task is to create a program to book tickets. if available
- tickets more than noOfTicket to book then display the remaining tickets or ticket unavailable:
### Tasks:
1. Write a program that takes the availableTicket and noOfBookingTicket as input.
2. Use conditional statements (if-else) to determine if the ticket is available or not.
3. Display an appropriate message based on ticket availability.

```python   
def ticket_booking(availableTicket, noOfBookingTicket):
    if availableTicket >= noOfBookingTicket:
        return f"{noOfBookingTicket} Tickets are available"
    else:
        return f"Sorry, Tickets are not Available"


availableTicket = int(input("Enter the no of tickets available: "))
noOfBookingTicket = int(input("Enter the no of Tickets you want to book: "))
print(ticket_booking(availableTicket, noOfBookingTicket))

```

## Task 2: Nested Conditional Statements
- Create a program that simulates a Ticket booking and calculating cost of tickets. - Display tickets options such as "Silver", "Gold", "Dimond". Based on ticket category fix the base ticket price and get the user input for ticket type and no of tickets need and calculate the total cost of tickets booked.

```python
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
```


## Task 3: Looping
- From the above task book the tickets for repeatedly until user type "Exit"

```python
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
```

## Task 4: Class & Object
### Create a Following classes with the following attributes and methods:
1. Event Class:
- • Attributes:
- event_name,
- event_date DATE,
- event_time TIME,
- venue_name,
- total_seats,
- available_seats,
- ticket_price DECIMAL,
- event_type ENUM('Movie', 'Sports', 'Concert')
2. Methods and Constuctors:
- Implement default constructors and overload the constructor with Customer
attributes, generate getter and setter, (print all information of attribute) methods for the attributes.
- calculate_total_revenue(): Calculate and return the total revenue based on the
number of tickets sold.
- getBookedNoOfTickets(): return the total booked tickets
- book_tickets(num_tickets): Book a specified number of tickets for an event. Initially
available seats are equal to the total seats when tickets are booked available seats
number should be reduced.
- cancel_booking(num_tickets): Cancel the booking and update the available seats.
o display_event_details(): Display event details, including event name, date time seat availability

```python
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

Salaar.display_event_details()
Salaar.book_tickets(10)
print(Salaar.getBookedNoOfTickets())
print(Salaar.calculate_total_revenue())
Salaar.cancel_booking(5)
Salaar.display_event_details()

```

2. Venue Class
- • Attributes:
- venue_name,
- address
- Methods and Constuctors:
- display_venue_details(): Display venue details.
- Implement default constructors and overload the constructor with Customer attributes, generate getter and setter methods.

```python
class Venue:
    def __init__(self, venue_name, address):
        self.venue_name = venue_name
        self.address = address

    def display_venue_details(self):
        print(f"Name of the Venue: {self.venue_name}")
        print(f"Venue address : {self.address}")


venue1 = Venue("Multiplex Mayajaal", "Chennai,Tamilnadu")
venue1.display_venue_details()
```

3. Customer Class
- • Attributes:
- customer_name,
- email,
- phone_number,
- • Methods and Constuctors:
- Implement default constructors and overload the constructor with Customer attributes, generate getter and setter methods.
- display_customer_details(): Display customer details.

```python
class Customer:
    def __init__(self, customer_name, email, phone_number):
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def display_customer_details(self):
        print(f"Name of the Customer : {self.customer_name}")
        print(f"Customer email : {self.email}")
        print(f"phone number: {self.phone_number}")


James = Customer("James", "James@gmail.com", 7458764567)
James.display_customer_details()
```

4. Booking Class to represent the Tiket booking system. Perform the following operation in main method. Note:- Use Event class object for the following operation.
- • Methods and Constuctors:
- calculate_booking_cost(num_tickets): Calculate and set the total cost of the
booking.
- book_tickets(num_tickets): Book a specified number of tickets for an event.
- cancel_booking(num_tickets): Cancel the booking and update the available seats.
- getAvailableNoOfTickets(): return the total available tickets
- getEventDetails(): return event details from the event class

```python
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
print(Salaar1.book_tickets(5))
print(Salaar1.calculate_booking_cost(5))
print(Salaar1.cancel_booking(4))
print(Salaar1.getAvaialableNoOfTickets())
Salaar1.getEventDetails()
```

## Task 5: Inheritance and polymorphism
1. Inheritance
- • Create a subclass Movie that inherits from Event. Add the following attributes and methods:
- Attributes:
- 1. genre: Genre of the movie (e.g., Action, Comedy, Horror).
- 2. ActorName
- 3. ActresName
- Methods:
1. Implement default constructors and overload the constructor with Customer
attributes, generate getter and setter methods.
2. display_event_details(): Display movie details, including genre.

```python
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


```


- Create another subclass Concert that inherits from Event. Add the following attributes and
methods:
- o Attributes:
1. artist: Name of the performing artist or band.
2. type: (Theatrical, Classical, Rock, Recital)
- Methods:
1. Implement default constructors and overload the constructor with Customer
attributes, generate getter and setter methods.
2. display_concert_details(): Display concert details, including the artist.

```python

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


```
- Create another subclass Sports that inherits from Event. Add the following attributes and
methods:
- o Attributes:

1. sportName: Name of the game.
2. teamsName: (India vs Pakistan)
- o Methods:
1. Implement default constructors and overload the constructor with Customer
attributes, generate getter and setter methods.
2. display_sport_details(): Display concert details, including the artist.

```python
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
```