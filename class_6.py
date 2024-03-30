class Ticket:
    # Constructor with initialization of ticket instance with its attributes
    def __init__(self,ticket_id,ticket_type,exhibition,visitor,purchase_date):
        #attributes
        self._ticket_id=ticket_id
        self._ticket_type=ticket_type
        self._exhibition=exhibition
        self._visitor=visitor
        self._purchase_date=purchase_date

    #Getters and setters

    def get_ticket_id(self):
        return self._ticket_id

    def set_ticket_id(self,ticket_id):
        self._ticket_id=ticket_id


    def get_ticket_type(self):
        return self._ticket_type

    def set_ticket_type(self,ticket_type):
        self._ticket_type= ticket_type


    def get_exhibition(self):
        return self._exhibition

    def set_exhibition(self,exhibition):
        self._exhibition= exhibition


    def get_visitor(self):
        return self._visitor

    def set_visitor(self,visitor):
        self._visitor=visitor


    def get_purchase_date(self):
        return self._purchase_date

    def set_purchase_date(self,purchase_date):
        self._purchase_date= purchase_date
