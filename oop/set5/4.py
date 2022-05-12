from abc import ABCMeta, abstractmethod


class Customer(metaclass=ABCMeta):
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None
        self.bill_id = None

    @abstractmethod
    def calculate_bill_amount(self):
        pass

    def get_customer_name(self):
        return self.__customer_name


class OccasionalCustomer(Customer):
    __counter = 1000

    def __init__(self, distance_in_kms, customer_name):
        super().__init__(customer_name)
        OccasionalCustomer.__counter += 1
        self.bill_id = "O" + str(OccasionalCustomer.__counter)
        self.__distance_in_kms = distance_in_kms

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def validate_distance_in_kms(self):
        if 1 <= self.__distance_in_kms <= 5:
            return True
        return False

    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            self.__bill_amount = 50
            if self.__distance_in_kms <= 2:
                self.__bill_amount += self.__distance_in_kms * 5
            else:
                self.__bill_amount += self.__distance_in_kms * 7.5
            return self.__bill_amount
        else:
            self.__bill_amount = -1
            return -1


class RegularCustomer(Customer):
    __counter = 100

    def __init__(self, no_of_tiffin, customer_name):
        super().__init__(customer_name)
        RegularCustomer.__counter += 1
        self.bill_id = "R" + str(RegularCustomer.__counter)
        self.__no_of_tiffin = no_of_tiffin

    def validate_no_of_tiffin(self):
        if 1 <= self.__no_of_tiffin <= 7:
            return True
        return False

    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount = 50 * 7 * self.__no_of_tiffin
            return self.bill_amount
        self.bill_amount = -1
        return -1

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin


cus1 = RegularCustomer(2, "cus1")
print(cus1.calculate_bill_amount())
cus2 = OccasionalCustomer(4, "Cus2")
print(cus2.calculate_bill_amount())
