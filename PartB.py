import unittest

class Animal:
    def __init__(self, name):
        self.name = name

def is_this_an_anminal(obj):
    return isinstance(obj, Animal)


class TestIsInstanceOfAnimal(unittest.TestCase):
    def test_object_is_instance_of_animal(self):
        cat = Animal('Cat')
        self.assertTrue(is_this_an_anminal(cat), "Animal")

    def test_object_is_not_instance_of_animal(self):
        not_an_animal = "i am an animal"
        self.assertFalse(is_this_an_anminal(not_an_animal), "not an animal")


if __name__ == '__main__':
    unittest.main()

    import unittest


    class Car:
        pass


    def is_car_instance(obj):
        return isinstance(obj, Car)


    class TestNotCarInstance(unittest.TestCase):
        def test_string_is_not_car(self):
            self.assertFalse(is_car_instance('hello'))

        def test_number_is_not_car(self):
            self.assertFalse(is_car_instance(42))

        def test_list_is_not_car(self):
            self.assertFalse(is_car_instance(['car', 'bike']))


    if __name__ == '__main__':
        unittest.main()

        import unittest


        class Box:
            def __init__(self, content):
                self.content = content


        def are_identical(obj1, obj2):
            return obj1 is obj2


        class TestObjectsIdentical(unittest.TestCase):
            def test_identical_objects(self):
                box1 = Box('Apple')
                box2 = box1  # Same reference
                self.assertTrue(are_identical(box1, box2))

            def test_non_identical_objects(self):
                box1 = Box('Apple')
                box2 = Box('Apple')  # Different references
                self.assertFalse(are_identical(box1, box2))


        if __name__ == '__main__':
            unittest.main()




import unittest

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


class TestPhoneUpdates(unittest.TestCase):
    def setUp(self):
        self.phone = Phone(500, "Blue", 2020, "Galaxy S10", "Samsung")
        self.smartphone = Smartphone(1600, "Purple", 2024, "Iphone16 Pro Max", "Apple", "iOS")

    def test_update_price(self):
        self.phone.update_price(600)
        self.assertEqual(self.phone.price, 600)

    def test_update_brand(self):
        self.phone.update_brand("Nokia")
        self.assertEqual(self.phone.brand, "Nokia")

    def test_update_color(self):
        self.phone.update_color("Red")
        self.assertEqual(self.phone.color, "Red")

    def test_update_operating_system(self):
        self.smartphone.update_operating_system("Android")
        self.assertEqual(self.smartphone.operating_system, "Android")


if __name__ == '__main__':
    unittest.main()


