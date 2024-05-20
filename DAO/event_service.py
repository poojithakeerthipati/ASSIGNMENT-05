from abc import ABC, abstractmethod
from Util.DBConn import DBConnection
from Entity import Event
from tabulate import tabulate
from MyExceptions.exception import EventNotFoundException


class IEvent(ABC):
    @abstractmethod
    def calculate_total_revenue(self):
        pass

    @abstractmethod
    def get_booked_no_of_tickets(self):
        pass

    # @abstractmethod
    # def book_tickets(self, num_tickets):
    #     pass

    # @abstractmethod
    # def cancel_booking(self, num_tickets):
    #     pass

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
                raise EventNotFoundException
        except Exception as e:
            print("OOPS Error Happened: ", e)

    def get_booked_no_of_tickets(self):
        self.cursor.execute("SELECT EVENT_ID,TOTAL_SEATS,AVAILABLE_SEATS FROM Event")
        event_data = [list(row) for row in self.cursor.fetchall()]
        booked_data = []
        for row in event_data:
            event_id, total_seats, available_seats = row
            booked_tickets = total_seats - available_seats
            booked_data.append((event_id, booked_tickets))
        headers = [event_id, booked_data]
        print(tabulate(booked_data, headers=headers, tablefmt="grid"))

    # def book_tickets(self, num_tickets):
    #     if self.available_seats >= num_tickets:
    #         self.available_seats -= num_tickets
    #         print(f"{num_tickets} tickets booked successfully for {self.event_name}")
    #     else:
    #         print("Sorry, Seats are unavailable")

    # def cancel_booking(self, num_tickets):
    #     if num_tickets <= (self.total_seats - self.available_seats):
    #         self.available_seats += num_tickets
    #         print(f"{num_tickets} tickets cancelled successfully for {self.event_name}")

    #     else:
    #         print("Invalid no of seats to cancel")

    def display_event_details(self):
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
                raise EventNotFoundException
        except Exception as e:
            print("OOPS Error Happened: ", e)
