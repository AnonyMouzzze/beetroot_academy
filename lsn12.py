# Task 1 School
class Person:
    def __init__(self, fullname, job, sex, age):
        self.fullname = fullname
        self.job = job
        self.sex = sex
        self.age = age


class Student(Person):
    def __init__(self, fullname, job, sex, age):
        super().__init__(fullname, job, sex, age)
        self.scholarship = 1000


class Teacher(Person):
    def __init__(self, fullname, job, sex, age, subject):
        super().__init__(fullname, job, sex, age)
        self.subject = subject


# Task 3 Product Store
class Product:
    def __init__(self, prod_type, name, price):
        self.type = prod_type
        self.name = name
        self.price = price
        self.amount = 0
        self.discount = 0


class ProductStore:
    def __init__(self):
        self.products = []

    def add(self, product, amount):
        self.products.append(product)
        product.amount = amount
        print('Product was added')

    def set_discount(self, identifier, percent):
        for product in self.products:
            if product.name == identifier or product.type == identifier:
                product.discount = percent
                product.price = product.price - (product.price*percent/100)
        print(f'Discount {percent} for products was set')

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name and product.amount >= amount:
                product.amount -= amount
                print('Product was successfully sold')

    def get_income(self):
        return len(self.products)

    def get_all_products(self):
        products = []
        for product in self.products:
            products.append(
                {
                    'type': product.type,
                    'name': product.name,
                    'price': product.price,
                    'amount': product.amount,
                    'discount': product
                }
            )
        return products

    def get_product_info(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product.name, product.amount,
