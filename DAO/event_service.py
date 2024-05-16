class EventService:
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
