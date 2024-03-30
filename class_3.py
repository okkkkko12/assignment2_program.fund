#create a class for the artwork
class Artwork:
    # Constructor with initialization of artwork instance with its attributes
    def __init__(self,title,artist,date,historical_significance,exhibition_location):
        #attributes
        self._title=title
        self._artist=artist
        self._date=date
        self._historical_significance=historical_significance
        self._exhibition_location=exhibition_location

    #Getters and setters for the artwork class

    def get_title(self):
        return self._title

    def set_title(self,title):
        self._title=title

    def get_artist(self):
        return self._artist

    def set_artist(self,artist):
        self._artist=artist

    def get_date(self):
        return self._date

    def set_date(self,date):
        self._date=date


    def get_historical_significance(self):
        return self._historical_significance

    def set_historical_significance(self,historical_significance):
        self._historical_significance=historical_significance


    def get_exhibition_location(self):
        return self._exhibition_location

    def set_exhibition_location(self,exhibition_location):
        self._exhibition_location=exhibition_location
