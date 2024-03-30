class Visitor:
    # Constructor with initialization of visitor instance with its attributes
    def __init__(self,name,age,national_id,email,phone_number,ticket_type,ticket_price):
        #attributes
        self._name=name
        self._age=age
        self._national_id=national_id
        self._email=email
        self._phone_number=phone_number
        self._ticket_type=ticket_type
        self._ticket_price=ticket_price

    #Getters and setters

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name=name

    def get_age(self):
        return self._age

    def set_age(self,age):
        self._age=age

    def get_national_id(self):
        return self._national_id

    def set_national_id(self,national_id):
        self._national_id=national_id

    def get_email(self):
        return self._email

    def set_email(self,email):
        self._email=email


    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self,phone_number):
        self._phone_number=phone_number


    def get_ticket_type(self):
        return self._ticket_type

    def set_ticket_type(self,ticket_type):
        self._ticket_type= ticket_type

    def get_ticket_price(self):
        return self._ticket_price

    def set_ticket_price(self, ticket_price):
        self._ticket_price = ticket_price
