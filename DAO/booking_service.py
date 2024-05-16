class BookingService:

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
