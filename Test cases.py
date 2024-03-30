from class_1 import Museum
from class_3 import Artwork
from class_4 import Exhibition
from class_5 import Visitor
from class_6 import Ticket
from class_7 import Prices
import unittest
from datetime import datetime

# Define a test class that inherits from unittest.TestCase
class TestFunctionality(unittest.TestCase):
    def setUp(self):
        # Setup method to initialize common test objects used in multiple test methods
        self.museum = Museum('Louvre Museum Abu Dhabi', 'Saadiyat Island,Abu Dhabi, UAE', '2017-11-08', '10:00','20:00', '22:00')
        self.exhibition = Exhibition('Cartier, Islamic Inspiration and Modern Design', 'Louvre Abu Dhabi','16 November 2023 - 24 March 2024',"Discover the influence of Islamic art on Cartier’s designs and creations at Louvre Abu Dhabi's exhibition.")
        self.artwork = Artwork('The Bezique Game', 'Gustave Caillebotte', '1880','Showcasing leisure among friends, influenced by photography and new perspectives in painting.','Louvre Abu Dhabi')
        self.prices = Prices()

    def test_add_artwork(self):
        # Test case for adding an artwork to the museum's collection
        self.museum.add_artwork(self.artwork)  # Add the artwork to the museum's collection
        added_artwork = self.museum.artworks[-1]  # Retrieve the last added artwork
        # Print details of the added artwork for verification
        print(f"\nAdded Artwork: {added_artwork.get_title()} by {added_artwork.get_artist()}, Date: {added_artwork.get_date()}, Historical Significance: {added_artwork.get_historical_significance()}, Location: {added_artwork.get_exhibition_location()}.")

    def test_new_exhibition(self):
        # Test case for adding a new exhibition to the museum
        self.museum.open_exhibition(self.exhibition)  # Add the exhibition to the museum
        added_exhibition = self.museum.exhibitions[-1]  # Retrieve the last added exhibition
        # Print details of the added exhibition for verification
        print(f"\nOpened Exhibition: {added_exhibition.get_title()}, Location: {added_exhibition.get_location()}, Duration: {added_exhibition.get_duration()}, Description: {added_exhibition.get_description()}.")

    def test_ticket_adult(self):
        # Test case for an adult visitor purchasing a ticket
        visitor = Visitor('Mariam', 30, '784199312345678', 'mariam@gmail.com', '0501234567', 'Adult', 0)  # Create an adult visitor
        ticket_price = self.prices.calc_ticket_price(visitor.get_age(), visitor.get_ticket_type(), is_group=False)  # Calculate ticket price
        visitor.set_ticket_price(ticket_price)  # Set the calculated ticket price for the visitor
        ticket = Ticket('123', visitor.get_ticket_type(), self.exhibition, visitor, datetime.now())  # Create a ticket for the visitor
        self.museum.purchase_ticket(ticket)  # Add the ticket to the museum's ticket collection
        # Print ticket purchase details for the visitor
        print(f"\nTicket Purchased for Visitor: Name: {visitor.get_name()}, Age: {visitor.get_age()}, Ticket Type: {visitor.get_ticket_type()}, Price: AED {visitor.get_ticket_price()}. Exhibition: {ticket.get_exhibition().get_title()}.")

    def test_ticket_child(self):
        # Test case for purchasing a ticket for a child
        visitor = Visitor('noor', 10, '784201211145678', 'ahmed@gmail.com', '0501275367', 'Child', 0)  # Create a child visitor
        ticket_price = self.prices.calc_ticket_price(visitor.get_age(), visitor.get_ticket_type(), is_group=False)  # Calculate ticket price for the child
        visitor.set_ticket_price(ticket_price)  # Set the calculated ticket price for the visitor
        initial_ticket_count = len(self.museum.tickets)  # Get the initial number of tickets
        ticket = Ticket('124', visitor.get_ticket_type(), self.exhibition, visitor, datetime.now())  # Create a ticket for the child visitor
        self.museum.purchase_ticket(ticket)  # Add the ticket to the museum's ticket collection
        # Assert that the number of tickets has increased by 1
        self.assertEqual(len(self.museum.tickets), initial_ticket_count + 1, "Failed to purchase child ticket")
        # Print success message indicating the test passed and show total tickets
        print(f'Test ticket child: PASSED, total tickets: {len(self.museum.tickets)}')

    def test_ticket_senior(self):
        # Test case for a senior purchasing a ticket
        visitor = Visitor('Amal', 64, '784196012274678', 'amal@gmail.com', '0501234777', 'Senior', 0)  # Create a senior visitor
        ticket_price = self.prices.calc_ticket_price(visitor.get_age(), visitor.get_ticket_type(), is_group=False)  # Calculate ticket price for the senior
        visitor.set_ticket_price(ticket_price)  # Set the calculated ticket price for the visitor
        ticket = Ticket('125', visitor.get_ticket_type(), self.exhibition, visitor, datetime.now())  # Create a ticket for the senior visitor
        self.museum.purchase_ticket(ticket)  # Add the ticket to the museum's ticket collection
        # Print ticket purchase details for the senior visitor
        print(f"\nTicket Purchased for Visitor: Name: {visitor.get_name()}, Age: {visitor.get_age()}, Ticket Type: {visitor.get_ticket_type()}, Price: AED {visitor.get_ticket_price()}. Exhibition: {ticket.get_exhibition().get_title()}.")


    def test_display_payment_receipt1(self):
        # Test case for displaying a payment receipt for an adult visitor
        visitor = Visitor('Meera', 30, '784198488466254', 'meera@example.com', '0557455836', 'Adult', 0)  # Create an adult visitor
        ticket_price = self.prices.calc_ticket_price(visitor.get_age(), visitor.get_ticket_type(), is_group=False)  # Calculate ticket price for the visitor
        visitor.set_ticket_price(ticket_price)  # Set the calculated ticket price for the visitor
        ticket = Ticket('001', visitor.get_ticket_type(), self.exhibition, visitor, datetime.now())  # Create a ticket for the visitor
        self.museum.purchase_ticket(ticket)  # Add the ticket to the museum's ticket collection
        dob = datetime(1990, 1, 1).date()  # Set date of birth for receipt details
        receipt = self.museum.display_payment_receipt(ticket, dob)  # Generate and display the payment receipt
        # Print the payment receipt details
        print(f"\nPayment Receipt:\n{receipt}")

    def test_display_payment_receipt2(self):
        # Test case for displaying a payment receipt for a child visitor
        visitor = Visitor('Ali', 10, '3353282484', 'ali@gmail.com', '55-1234', 'Child', 0)  # Create a child visitor
        ticket_price = self.prices.calc_ticket_price(visitor.get_age(), visitor.get_ticket_type(), is_group=False)  # Calculate ticket price for the child
        visitor.set_ticket_price(ticket_price)  # Set the calculated ticket price for the visitor
        ticket = Ticket('002', visitor.get_ticket_type(), self.exhibition, visitor, datetime.now())  # Create a ticket for the child visitor
        self.museum.purchase_ticket(ticket)  # Add the ticket to the museum's ticket collection
        dob = datetime(2008, 2, 4).date()  # Set date of birth for receipt details
        receipt = self.museum.display_payment_receipt(ticket, dob)  # Generate and display the payment receipt
        # Print the payment receipt details
        print(f"\nPayment Receipt:\n{receipt}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
