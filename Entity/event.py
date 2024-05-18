from enum import Enum


class Event_type(Enum):
    Movie = 1
    Sports = 2
    Concert = 3


class Event:
    def __init__(
        self,
        event_id,
        event_name,
        event_date,
        event_time,
        venue_name,
        total_seats,
        available_seats,
        ticket_price,
        event_type,
    ):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type


class Movie(Event):
    def __init__(
        self,
        event_id,
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
            event_id,
            event_name,
            event_date,
            event_time,
            venue_name,
            total_seats,
            available_seats,
            ticket_price,
            event_type,
        )

    # def display_movie_details(self):
    #     print(f"genre of the movie : {self.genre}")
    #     print(f"Movie actor: {self.actor_name}")
    #     print(f"Movie actress : {self.actress_name}")
    #     return super().display_event_details()


class Concert(Event):
    def __init__(
        self,
        event_id,
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
            event_id,
            event_name,
            event_date,
            event_time,
            venue_name,
            total_seats,
            available_seats,
            ticket_price,
            event_type,
        )

    # def display_concert_details(self):
    #     print(f"Name of the artist: {self.artist}")
    #     print(f"Concert type: {self.type}")
    #     return super().display_event_details()


class Sports(Event):
    def __init__(
        self,
        event_id,
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
            event_id,
            event_name,
            event_date,
            event_time,
            venue_name,
            total_seats,
            available_seats,
            ticket_price,
            event_type,
        )

    # def display_sport_details(self):
    #     print(f"Name of the sport: {self.sport_name}")
    #     print(f"Name of the team : {self.teams_name}")
    #     return super().display_event_details()
