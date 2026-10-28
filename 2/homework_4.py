
from abc import ABC, abstractmethod


class Product(ABC):
    products_count = 0

    def __init__(self, name, price):
        self.name = name
        self.__price = price
        Product.products_count += 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if self.is_valid_price(value):
            self.__price = value
        else:
            print("Цена должна быть больше 0")

    @abstractmethod
    def get_info(self):
        pass

    def __str__(self):
        return self.get_info()

    @classmethod
    def show_products_count(cls):
        print("Количество товаров:", cls.products_count)

    @staticmethod
    def is_valid_price(price):
        return price > 0


class Electronic(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def get_info(self):
        return f"{self.name}, цена: {self.price}, гарантия: {self.warranty} лет"


class Delivery:
    def calculate_delivery(self):
        return 300


class Discount:
    def calculate_discount(self):
        return self.price * 0.10


class Smartphone(Electronic, Delivery, Discount):
    def __init__(self, name, price, warranty, manufacturer, model):
        super().__init__(name, price, warranty)
        self.manufacturer = manufacturer
        self.model = model

    def get_info(self):
        return (
            f"Смартфон: {self.name}, цена: {self.price}, "
            f"гарантия: {self.warranty} лет, "
            f"производитель: {self.manufacturer}, модель: {self.model}"
        )


class Laptop(Electronic):
    def __init__(self, name, price, warranty, manufacturer):
        super().__init__(name, price, warranty)
        self.manufacturer = manufacturer

    def get_info(self):
        return (
            f"Ноутбук: {self.name}, цена: {self.price}, "
            f"гарантия: {self.warranty} лет, "
            f"производитель: {self.manufacturer}"
        )


phone = Smartphone("Galaxy", 50000, 2, "Samsung", "S25")
laptop = Laptop("ROG Strix", 80000, 3, "ASUS")

products = [phone, laptop]

for product in products:
    print(product.get_info())

print()
print("Стоимость доставки:", phone.calculate_delivery())
print("Скидка на смартфон:", phone.calculate_discount())

print()
print("Цена смартфона:", phone.price)
phone.price = 55000
print("Новая цена:", phone.price)

print()
print("Проверка цены:", Product.is_valid_price(1000))
Product.show_products_count()

print()
print(phone)
