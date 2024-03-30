#create a class for the exhibition
class Exhibition:
    # Constructor with initialization of exhibition instance with its attributes
    def __init__(self,title,location,duration,description):
        #attributes
        self._title=title
        self._location=location
        self._duration=duration
        self._description=description

    #Getters and setters

    def get_title(self):
        return self._title

    def set_title(self,title):
        self._title=title


    def get_location(self):
        return self._location

    def set_location(self,location):
        self._location=location


    def get_duration(self):
        return self._duration

    def set_duration(self,duration):
        self._duration=duration


    def get_description(self):
        return self._description

    def set_description(self,description):
        self._description=description
