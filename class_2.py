#create a tour class
class Tour:
    # Constructor with initialization of tour instance with its attributes
    def __init__(self,tourID,date,guide,max_capacity,current_capacity,duration):
        #attributes
        self._tourID=tourID
        self._date=date
        self._guide=guide
        self._max_capacity=max_capacity
        self._current_capacity=current_capacity
        self._duration=duration

    #Getters and setters for the tour class
    def get_tourID (self):
        return self._tourID

    def set_tourID (self,tourID ):
        self._tourID=tourID

    def get_date(self):
        return self._date

    def set_date (self,date):
        self._date=date

    def get_guide (self):
        return self._guide

    def set_guide (self,guide ):
        self._guide=guide

    def get_max_capacity(self):
        return self._max_capacity

    def set_max_capacity (self,max_capacity ):
        self._max_capacity=max_capacity


    def get_current_capacity(self):
        return self._current_capacity

    def set_current_capacity (self,current_capacity ):
        self._current_capacity=current_capacity


    def get_duration(self):
        return self._duration

    def set_duration (self,duration ):
        self._duration=duration
