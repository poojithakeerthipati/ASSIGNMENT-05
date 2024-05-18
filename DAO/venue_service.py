from Entity import Venue
from abc import ABC, abstractmethod
from Util.DBConn import DBConnection
from tabulate import tabulate


class IVenueService(ABC):
    @abstractmethod
    def display_venue_details(self):
        pass


class VenueService(DBConnection, ABC):
    def display_venue_details(self):
        try:
            self.cursor.execute("SELECT * FROM Venue")
            venue_data = [list(row) for row in self.cursor.fetchall()]
            headers = ["Venue_id", "Venue_name", "Address"]
            if venue_data:
                print(tabulate(venue_data, headers=headers, tablefmt="grid"))
            else:
                pass  # raise exception
        except Exception as e:
            print("OOPS Error Happened: ", e)
