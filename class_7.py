#create a prices class
class Prices:
    #  Constructor with initialization of the prices class with default values for base price, VAT rate, and discount rate
    def __init__(self, base_price=63.0, vat_rate=0.05, discount_rate=0.5):
        self._base_price = base_price  # The base price which is the ticket price without taxes
        self._vat_rate = vat_rate  # Value-Added Tax rate applied to the ticket price
        self._discount_rate = discount_rate  # Discount rate for group tickets

    def calc_ticket_price(self, age, visitor_type, is_group):
        # Calculates the final ticket price based on age, visitor type, and group status
        ticket_price = self._base_price  # Initialize ticket price to base price

        # Check for free admission for certain categories and age groups
        if visitor_type == 'Adult' and 18 <= age <= 60:
            pass  # Adult pays base price
        elif visitor_type in ['Child', 'Teacher', 'Student', 'Senior'] and (age < 18 or age > 60):
            ticket_price = 0  # 'Child', 'Teacher', 'Student', 'Senior' categories gets in free

        # Apply group discount if the visitor is part of a group and the ticket price is not already 0
        if is_group and ticket_price > 0:
            ticket_price *= (1 - self._discount_rate)  # Discount is subtracted from 1 to get the reduced price factor

        # Apply VAT to the ticket price unless it's 0 (free admission)
        if ticket_price > 0:
            ticket_price *= (1 + self._vat_rate)  # VAT is added to the price

        return ticket_price  # Return the final calculated ticket price


