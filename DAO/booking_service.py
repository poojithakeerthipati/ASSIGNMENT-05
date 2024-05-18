from abc import ABC, abstractmethod
from tabulate import tabulate
from Util.DBConn import DBConnection


class IBookingSystem(ABC):
    @abstractmethod
    def calculate_booking_cost(self, num_tickets):
        pass

    @abstractmethod
    def book_tickets(self, event, num_tickets):
        pass

    @abstractmethod
    def cancel_booking(self, num_tickets):
        pass

    @abstractmethod
    def get_available_no_of_tickets(self):
        pass

    @abstractmethod
    def get_event_details(self, event):
        pass


class BookingService(DBConnection, IBookingSystem):

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
