from abc import ABC, abstractmethod
from Util.DBConn import DBConnection
from Entity import Event
from tabulate import tabulate


class IEvent(ABC):
    @abstractmethod
    def calculate_total_revenue(self):
        pass

    @abstractmethod
    def get_booked_no_of_tickets(self):
        pass

    @abstractmethod
    def book_tickets(self, num_tickets):
        pass

    @abstractmethod
    def cancel_booking(self, num_tickets):
        pass

    @abstractmethod
    def display_event_details(self):
        pass


class EventService(IEvent, DBConnection):
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


# class Movie(Event):
#     def display_event_details(self):
#         print(f"Event: {self.event_name}")
#         print(f"Date: {self.date}")
#         print(f"Time: {self.time}")
#         print(f"Venue: {self.venue_name}")
#         print(f"Available Seats: {self.available_seats}")
#         print(f"Ticket Price: {self.ticket_price}")
#         print(f"Genre: {self.genre}")
#         print(f"Actor: {self.actor_name}")
#         print(f"Actress: {self.actress_name}")

#     def book_tickets(self, num_tickets):
#         if self.available_seats >= num_tickets:
#             self.available_seats -= num_tickets
#             print(f"{num_tickets} tickets booked for {self.event_name}.")
#         else:
#             print("Sorry, the event is sold out.")

#     def cancel_booking(self, num_tickets):
#         self.available_seats += num_tickets
#         print(f"{num_tickets} tickets canceled for {self.event_name}.")


# class Concert(Event):
#     def __init__(
#         self,
#         event_name,
#         date,
#         time,
#         total_seats,
#         ticket_price,
#         event_type,
#         venue_name,
#         artist,
#         concert_type,
#     ):
#         super().__init__(
#             event_name, date, time, total_seats, ticket_price, event_type, venue_name
#         )
#         self.artist = artist
#         self.concert_type = concert_type

#     def display_event_details(self):
#         print(f"Event: {self.event_name}")
#         print(f"Date: {self.date}")
#         print(f"Time: {self.time}")
#         print(f"Venue: {self.venue_name}")
#         print(f"Available Seats: {self.available_seats}")
#         print(f"Ticket Price: {self.ticket_price}")
#         print(f"Artist: {self.artist}")
#         print(f"Concert Type: {self.concert_type}")

#     def book_tickets(self, num_tickets):
#         if self.available_seats >= num_tickets:
#             self.available_seats -= num_tickets
#             print(f"{num_tickets} tickets booked for {self.event_name}.")
#         else:
#             print("Sorry, the event is sold out.")

#     def cancel_booking(self, num_tickets):
#         self.available_seats += num_tickets
#         print(f"{num_tickets} tickets canceled for {self.event_name}.")


# class Sport(Event):
#     def __init__(
#         self,
#         event_name,
#         date,
#         time,
#         total_seats,
#         ticket_price,
#         event_type,
#         venue_name,
#         sport_name,
#         teams_name,
#     ):
#         super().__init__(
#             event_name, date, time, total_seats, ticket_price, event_type, venue_name
#         )
#         self.sport_name = sport_name
#         self.teams_name = teams_name

#     def display_event_details(self):
#         print(f"Event: {self.event_name}")
#         print(f"Date: {self.date}")
#         print(f"Time: {self.time}")
#         print(f"Venue: {self.venue_name}")
#         print(f"Available Seats: {self.available_seats}")
#         print(f"Ticket Price: {self.ticket_price}")
#         print(f"Sport: {self.sport_name}")
#         print(f"Teams: {self.teams_name}")

#     def book_tickets(self, num_tickets):
#         if self.available_seats >= num_tickets:
#             self.available_seats -= num_tickets
#             print(f"{num_tickets} tickets booked for {self.event_name}.")
#         else:
#             print("Sorry, the event is sold out.")

#     def cancel_booking(self, num_tickets):
#         self.available_seats += num_tickets
#         print(f"{num_tickets} tickets canceled for {self.event_name}.")
