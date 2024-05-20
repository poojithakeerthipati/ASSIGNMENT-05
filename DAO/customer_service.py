from tabulate import tabulate
from abc import ABC, abstractmethod
from Util.DBConn import DBConnection


class ICustomerSerice(ABC):
    @abstractmethod
    def display_customer_details(self):
        pass


class CustomerService(DBConnection, ICustomerSerice):
    def display_customer_details(self):
        try:
            self.cursor.execute("SELECT * FROM Customer")
            customer_data = [list(row) for row in self.cursor.fetchall()]
            headers = ["Customer_name", "email", "phone_number"]
            if customer_data:
                print(tabulate(customer_data, headers=headers, tablefmt="grid"))
            else:
                pass  # raise exception
        except Exception as e:
            print("OOPS Error Happened: ", e)
