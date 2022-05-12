
class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None

    def validate_flower(self):
        flowers = ("Orchid", "Rose", "Jasmine")
        if self.__flower_name.title() in flowers:
            return True
        return False

    def validate_stock(self, required_quantity):
        if self.__stock_available >= required_quantity:
            return True
        return False

    def sell_flower(self, required_quantity):
        if (
            self.validate_flower()
            and self.validate_stock(required_quantity)
            and self.__stock_available >= required_quantity
        ):
            self.__stock_available -= required_quantity

    def check_level(self):
        order_level = {"Orchid": 15, "Rose": 25, "Jasmine": 40}
        if (
            self.validate_flower()
            and self.__stock_available < order_level[self.__flower_name.title()]
        ):
            return True
        return False

    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name

    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg

    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available

    def get_flower_name(self):
        return self.__flower_name

    def get_price_per_kg(self):
        return self.__price_per_kg

    def get_stock_available(self):
        return self.__stock_available


rose = Flower()
rose.set_flower_name("Rose")
rose.set_price_per_kg(45)
rose.set_stock_available(56)
rose.sell_flower(45)
print(rose._Flower__stock_available)
print(rose.check_level())
