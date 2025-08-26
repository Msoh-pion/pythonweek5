
# Parent Class

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

    # Default info
    def show_info(self):
        return f"Part: {self.name}, Price: {self.__price}, Stock: {self.stock}"

    # Default action (will be overridden by subclasses)
    def move(self):
        print("Generic part has no movement.")



# Child Classes


class EnginePart(CarPart):
    def __init__(self, name, price, stock, horsepower):
        super().__init__(name, price, stock)
        self.horsepower = horsepower

    # Method override (Polymorphism)
    def show_info(self):
        return f"Engine Part: {self.name}, {self.horsepower} HP, Price: {self.get_price()}, Stock: {self.stock}"

    # Polymorphic move() method
    def move(self):
        print("Powering the car 🚗")


class LightingPart(CarPart):
    def __init__(self, name, price, stock, brightness):
        super().__init__(name, price, stock)
        self.brightness = brightness

    def show_info(self):
        return f"Lighting Part: {self.name}, Brightness: {self.brightness} lumens, Price: {self.get_price()}, Stock: {self.stock}"

    def move(self):
        print("Illuminating the road 💡")


class WheelPart(CarPart):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size

    def show_info(self):
        return f"Wheel Part: {self.name}, Size: {self.size} inches, Price: {self.get_price()}, Stock: {self.stock}"

    def move(self):
        print("Rolling smoothly 🛞")



# Create Objects
# ==========================
spark_plug = CarPart("Spark Plug", 500, 20)
engine_oil = EnginePart("Engine Oil", 1500, 10, 120)
headlight = LightingPart("LED Headlight", 3000, 5, 1200)
wheel = WheelPart("Alloy Wheel", 7000, 4, 18)

# Print details
print(spark_plug.show_info())
print(engine_oil.show_info())
print(headlight.show_info())
print(wheel.show_info())

# Encapsulation in action
spark_plug.set_price(-200)   # ❌ invalid
spark_plug.set_price(600)    # ✅ update
print("Updated:", spark_plug.show_info())

# Polymorphism in move()
print("\n--- Testing move() ---")
parts = [spark_plug, engine_oil, headlight, wheel]
for part in parts:
    part.move()

