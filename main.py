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
