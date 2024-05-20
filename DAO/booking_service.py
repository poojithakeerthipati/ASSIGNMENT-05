from abc import ABC, abstractmethod
from tabulate import tabulate
from Util.DBConn import DBConnection
from MyExceptions.exception import EventNotFoundException


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

    def calculate_booking_cost(self, event_id, num_tickets):
        total_cost_of_tickets = 0
        self.cursor.execute(
            "SELECT AVAILABLE_SEATS FROM EVENT WHERE Event_id=?", (event_id)
        )
        booking_data = self.cursor.fetchall()
        available_seats = booking_data[0][0]
        while True:
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
            if available_seats >= num_tickets:
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
                cost_of_tickets = num_tickets * base_ticket_price
                total_cost_of_tickets += num_tickets * base_ticket_price
                print(f"Total cost of tickets is {cost_of_tickets}")
                available_seats -= num_tickets
            else:
                print(f"Sorry, Tickets are not Available")
                break
        return f"total cost of tickets is {total_cost_of_tickets}"

    def book_tickets(self, event_id, num_tickets):
        self.cursor.execute(
            "SELECT available_seats from event where event_id=?", (event_id)
        )
        available_seats = self.cursor.fetchone()[0]
        try:
            if available_seats >= num_tickets:
                self.cursor.execute(
                    "UPDATE Event SET available_seats = available_seats - ? WHERE event_id = ?",
                    (num_tickets, event_id),
                )
                # self.conn.commit()
                return f"{num_tickets} tickets booked successfully"
            else:
                return "Sorry, tickets are unavailable"
        except Exception as e:
            print("OOPS Error Happened: ", e)

    def cancel_booking(self, event_id, num_tickets):
        self.cursor.execute(
            "SELECT total_seats,available_seats from event where event_id=?", (event_id)
        )
        data = self.cursor.fetchone()
        total_seats, available_seats = data
        try:
            if (total_seats - available_seats) >= num_tickets:
                self.cursor.execute(
                    "UPDATE Event SET available_seats = available_seats +? WHERE event_id = ?",
                    (num_tickets, event_id),
                )
                self.conn.commit()
                return f"{num_tickets} tickets cancelled successfully"
            else:
                return "Sorry, Invalid number of tickets"
        except Exception as e:
            print("OOPS Error Happened: ", e)

    def get_available_no_of_tickets(self, event_id):
        try:
            self.cursor.execute(
                "SELECT available_seats FROM Event WHERE event_id = ?",
                (event_id,),
            )
            available_seats = self.cursor.fetchone()[0]
            return f"The tickets available are {available_seats}"
        except Exception as e:
            print("OOPS Error Happened: ", e)

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
                raise EventNotFoundException
        except Exception as e:
            print("OOPS Error Happened: ", e)
