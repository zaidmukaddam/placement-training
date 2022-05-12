#lex_auth_012751870201536512237
#Start writing your code here

class Ticket:
    counter = 0

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = None
        self.__source = source
        self.__destination = destination

    def validate_source_destination(self):
        if self.__source.title() == "Delhi" and (
            self.__destination.title() == "Mumbai"
            or self.__destination.title() == "Pune"
            or self.__destination.title() == "Kolkata"
            or self.__destination.title() == "Chennai"
        ):
            return True
        else:
            return False

    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter += 1
            self.__ticket_id = (
                self.__source[0]
                + self.__destination[0]
                + "{:02d}".format(Ticket.counter)
            )
        else:
            return False

    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination


passenger = Ticket("Tushar", "Delhi", "Pune")
ticket = passenger.generate_ticket()
if ticket == False:
    print("Invalid Input")
else:
    print(
        passenger.get_passenger_name(),
        passenger.get_ticket_id(),
        passenger.get_source(),
        passenger.get_destination(),
    )
