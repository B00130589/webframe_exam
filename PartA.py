class Phone:
    def __init__(self, price, color, year, model, brand):
        self.price = price
        self.color = color
        self.year = year
        self.model = model
        self.brand = brand

    def display(self):
        print(f"Price: {self.price}, Color: {self.color}, Year: {self.year}, Model: {self.model}, Brand: {self.brand}")

    def update_price(self, price):
        if isinstance(price, (int, float)):
            self.price = price
        else:
            print("Price must be a number")

    def update_color(self, color):
        if isinstance(color, str):
            self.color = color
        else:
            print("Color must be a string")

    def update_year(self, year):
        if isinstance(year, int):
            self.year = year
        else:
            print("Year must be an integer")

    def update_model(self, model):
        if isinstance(model, str):
            self.model = model
        else:
            print("Model must be a string")

    def update_brand(self, brand):
        if isinstance(brand, str):
            self.brand = brand
        else:
            print("Brand must be a string")


class Smartphone(Phone):
    def __init__(self, price, color, year, model, brand, operating_system):
        super().__init__(price, color, year, model, brand)
        self.operating_system = operating_system

    def display(self):
        super().display()
        print(f"Operating System: {self.operating_system}")

    def update_operating_system(self, operating_system):
        if isinstance(operating_system, str):
            self.operating_system = operating_system
        else:
            print("Operating System must be a string")


# Instances
new_phone = Smartphone(1600, "Space Purple", 2024, "Iphone16 pro max", "Apple", "IOS")
old_phone = Phone(100, "Black", 1999, "Motorolla", "Motorola")

# Show initial attributes
new_phone.display()
old_phone.display()

# Update attributes
new_phone.update_brand("Huawei")
new_phone.update_price(1000)
new_phone.update_operating_system("Android")

old_phone.update_brand("Nokia")
old_phone.update_price(300)

# Show updated attributes
new_phone.display()
old_phone.display()
