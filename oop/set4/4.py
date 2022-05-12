# lex_auth_012753080343093248327
# Start writing your code here

class FruitInfo:
    __fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    __fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            return FruitInfo.__fruit_price_list[
                FruitInfo.__fruit_name_list.index(fruit_name)
            ]
        else:
            return -1

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list


class Purchase:
    __counter = 101

    def __init__(self, customer, fruit_name, quantity):
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__purchase_id = None
        self.__quantity = quantity

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        if self.__fruit_name in FruitInfo.get_fruit_name_list():
            price_per_kg = FruitInfo.get_fruit_price(self.__fruit_name)
            price = price_per_kg * self.__quantity
            if (
                max(FruitInfo.get_fruit_price_list()) == price_per_kg
                and self.__quantity > 1
            ):
                price *= 0.98
            elif (
                min(FruitInfo.get_fruit_price_list()) == price_per_kg
                and self.__quantity >= 5
            ):
                price *= 0.95
            if self.__customer.get_cust_type() == "wholesale":
                price *= 0.9
            self.__purchase_id = "P" + str(Purchase.__counter)
            Purchase.__counter += 1
            return price
        else:
            return -1


class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name

    def get_cust_type(self):
        return self.__cust_type


customer1 = Customer("cus1", "Retail")
customer2 = Customer("cus2", "wholesaler")
pur1 = Purchase(customer1, "Pear", 5)
pur1.calculate_price()
pur2 = Purchase(customer2, "Sweet Lime", 5)
pur2.calculate_price()
print(pur1.calculate_price())
print(pur2.calculate_price())
