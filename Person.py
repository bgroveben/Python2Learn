import datetime


class Person:
    """
    Here is an example of a simple custom class which stores information about a person
    name -> str
    birthdate -> datetime object such as datetime.date(1971, 9, 11)

    age() -> method which calculates the age of our person using the birthdate and the current date

    """
    def __init__(self, name, birthdate)
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age


person = Person("Ben", datetime.date(1971, 9, 11))

print(person.name)
print(person.age())
