# Parent class
class CarPart:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price   # encapsulation (private attribute)
        self.stock = stock

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("❌ Price must be positive!")

    def show_info(self):
        return f"Part: {self.name}, Price: {self.__price}, Stock: {self.stock}"


# Child class (Inheritance)
class EnginePart(CarPart):
    def __init__(self, name, price, stock, horsepower):
        super().__init__(name, price, stock)
        self.horsepower = horsepower

    # Method override (Polymorphism)
    def show_info(self):
        return f"Engine Part: {self.name}, {self.horsepower} HP, Price: {self.get_price()}, Stock: {self.stock}"


# Another Child class
class LightingPart(CarPart):
    def __init__(self, name, price, stock, brightness):
        super().__init__(name, price, stock)
        self.brightness = brightness

    def show_info(self):
        return f"Lighting Part: {self.name}, Brightness: {self.brightness} lumens, Price: {self.get_price()}, Stock: {self.stock}"



spark_plug = CarPart("Spark Plug", 500, 20)
engine_oil = EnginePart("Engine Oil", 1500, 10, 120)
headlight = LightingPart("LED Headlight", 3000, 5, 1200)

# Print details
print(spark_plug.show_info())
print(engine_oil.show_info())
print(headlight.show_info())

# Encapsulation in action
spark_plug.set_price(-200)   # ❌ invalid
spark_plug.set_price(600)    # ✅ update
print("Updated:", spark_plug.show_info())
