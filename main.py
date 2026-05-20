#4-masala
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):
        self.__salary += amount
        print("Oylik oshirildi")


e1 = Employee("Jasur", 500)

print(e1.name)
print(e1.get_salary())

e1.increase_salary(200)
print(e1.get_salary())
