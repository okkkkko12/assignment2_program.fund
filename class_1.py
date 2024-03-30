#crate a class for the museum
class Museum:
    # Constructor with initialization of museum instance with its attributes and lists for artworks, exhibitions, and tickets
    def __init__(self,name,location,established_date,opening_time,closing_time_weekdays,closing_time_weekends):
        self._name=name
        self._location=location
        self._established_date=established_date
        self._opening_time=opening_time
        self._closing_time_weekdays=closing_time_weekdays
        self._closing_time_weekends=closing_time_weekends
        self.artworks = []  # List to manage artworks
        self.exhibitions = []  # List to manage exhibitions
        self.tickets = []  # List to manage tickets

    # Getters and setters for museum class

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name=name

    def get_location (self):
        return self._location

    def set_location(self,location):
        self._location=location

    def get_established_date (self):
        return self._established_date

    def set_established_date(self,established_date):
        self._established_date=established_date

    def get_opening_time (self):
        return self._opening_time

    def set_opening_time(self,opening_time):
        self._opening_time=opening_time

    def get_closing_time_weekdays (self):
        return self._closing_time_weekdays

    def set_closing_time_weekdays(self,closing_time_weekdays):
        self._closing_time_weekdays=closing_time_weekdays

    def get_closing_time_weekends (self):
        return self._closing_time_weekends

    def set_closing_time_weekends(self,closing_time_weekends):
        self._closing_time_weekends=closing_time_weekends

    # Methods to interact with artworks
    def add_artwork(self, artwork):
        # Adds an artwork to the museum's collection
        self.artworks.append(artwork)

    # Methods to interact with exhibitions
    def open_exhibition(self, exhibition):
        # Adds an exhibition to the museum's schedule
        self.exhibitions.append(exhibition)

    # Methods to manage ticket purchases
    def purchase_ticket(self, ticket):
        # Records a ticket purchase
        self.tickets.append(ticket)

    def display_payment_receipt(self, ticket, dob):
        #formatte the payment receipt for a ticket purchase to a string
        formatted_purchase_date = ticket.get_purchase_date().strftime('%Y-%m-%d')
        formatted_purchase_time = ticket.get_purchase_date().strftime('%H:%M:%S')
        formatted_price = "{:.2f}".format(ticket.get_visitor().get_ticket_price())  # This line formats the price

        visitor = ticket.get_visitor()
        # Format the date of birth to a string
        formatted_dob = dob.strftime('%Y-%m-%d')
        # Returns a formatted receipt string
        return (f"Receipt\n"
                f"Name: {visitor.get_name()}\n"
                f"Date of Purchase: {formatted_purchase_date}\n"
                f"Time of Purchase: {formatted_purchase_time}\n"
                f"Ticket Type: {ticket.get_ticket_type()}\n"
                f"Price: {visitor.get_ticket_price()}\n")
