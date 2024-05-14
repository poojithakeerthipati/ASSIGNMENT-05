# Task-1
# def ticket_booking(availableTicket, noOfBookingTicket):
#     if availableTicket >= noOfBookingTicket:
#         return f"{noOfBookingTicket} Tickets are available"
#     else:
#         return f"Sorry, Tickets are not Available"

# availableTicket = int(input("Enter the no of tickets available: "))
# noOfBookingTicket = int(input("Enter the no of Tickets you want to book: "))
# print(ticket_booking(availableTicket, noOfBookingTicket))

# task-2
# def ticket_booking_cost(availableTicket, noOfBookingTicket):
#     base_ticket_price = 100
#     if availableTicket >= noOfBookingTicket:
#         print(
#             """Tickets are available , please Select The required ticket from the following
#                 1.Silver
#                 2.Gold
#                 3.Diamond
#                 """
#         )
#         ticket = int(input("Select the ticket type: "))
#         if ticket == 1:
#             total_cost_of_tickets = noOfBookingTicket * base_ticket_price
#             return f"Total Cost of tickets is {total_cost_of_tickets} "
#         elif ticket == 2:
#             base_ticket_price += 20
#             total_cost_of_tickets = noOfBookingTicket * base_ticket_price
#             return f"Total Cost of tickets is {total_cost_of_tickets} "
#         elif ticket == 3:
#             base_ticket_price += 50
#             total_cost_of_tickets = noOfBookingTicket * base_ticket_price
#             return f"Total Cost of tickets is {total_cost_of_tickets} "
#         else:
#             return f"Sorry , Select the appropriate ticket type"
#     else:
#         return f"Sorry, Tickets are not Available"


# availableTicket = int(input("Enter the no of tickets available: "))
# noOfBookingTicket = int(input("Enter the no of Tickets you want to book: "))
# print(ticket_booking_cost(availableTicket, noOfBookingTicket))


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
