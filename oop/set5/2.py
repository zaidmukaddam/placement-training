class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity

    def validate_quantity(self):
        if 1 <= self.__quantity <= 5:
            return True
        return False

    def get_quantity(self):
        return self.__quantity

    def get_customer_name(self):
        return self.__customer_name


class Pizzaservice:
    counter = 100

    def __init__(self, customer, pizza_type, additional_topping):
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = None
        self.__service_id = None

    def validate_pizza_type(self):
        if (
            self.__pizza_type.lower() == "small"
            or self.__pizza_type.lower() == "medium"
        ):
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            Pizzaservice.counter += 1
            pizza_cost = 0
            self.__service_id = self.__pizza_type[0] + \
                str(Pizzaservice.counter)
            if self.__pizza_type.lower() == "small":
                pizza_cost = 150
                if self.__additional_topping:
                    pizza_cost += 35
            elif self.__pizza_type.lower() == "medium":
                pizza_cost = 200
                if self.__additional_topping:
                    pizza_cost += 50

            self.pizza_cost = pizza_cost * self.__customer.get_quantity()
        else:
            self.pizza_cost = -1

    def get_service_id(self):
        return self.__service_id

    def get_customer(self):
        return self.__customer

    def get_pizza_type(self):
        return self.__pizza_type

    def get_additional_topping(self):
        return self.__additional_topping


class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__distance_in_kms = distance_in_kms
        self.__delivery_charge = 0

    def validate_distance_in_kms(self):
        if 1 <= self.__distance_in_kms <= 10:
            return True
        return False

    def calculate_pizza_cost(self):
        if not self.validate_distance_in_kms():
            self.pizza_cost = -1
            return
        super().calculate_pizza_cost()
        if self.pizza_cost != -1:
            if self.__distance_in_kms <= 5:
                self.__delivery_charge = 5 * self.__distance_in_kms
            else:
                self.__delivery_charge = 5 * 5 + \
                    7 * (self.__distance_in_kms - 5)
            self.pizza_cost += self.__delivery_charge
        else:
            self.pizza_cost = -1

    def get_delivery_charge(self):
        return self.__delivery_charge

    def get_distance_in_kms(self):
        return self.__distance_in_kms


cus1 = Customer("cus1", 3)
pizza = Doordelivery(cus1, "mediumm", True, 8)
pizza.calculate_pizza_cost()
print(pizza.pizza_cost)
print(pizza.get_delivery_charges())
