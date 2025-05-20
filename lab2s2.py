class Osnova:
    def init(self, name=None, last_name=None, birth_year=None):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def rozrahynok_age(self, current_year):
        if self.birth_year is None:
            return None
        return current_year - self.birth_year

    def full_name(self):
        return f"{self.name} {self.last_name}" if self.name and self.last_name else None

class DochClass(Osnova):
    def init(self, name=None, last_name=None, birth_year=None, father_name=None, city=None, phone_number=None, email=None, adress=None, hobbi=None):
        super().init(name, last_name, birth_year)
        self.father_name = father_name
        self.city = city
        self.phone_number = phone_number
        self.email = email
        self.adress = adress
        self.hobbi = hobbi

    def age_to_adulthood(self, current_year):
        age = self.rozrahynok_age(current_year)
        if age is None:
            return "Невідома дата народження"
        if age >= 18:
            return "Ви повнолітні"
        return f"До повноліття вам залишилось: {18 - age} років"

    def greeting(self, hour):
        if not self.name:
            return "Привіт!"
        if 6 <= hour < 12:
            return f"Доброго ранку, {self.name}!"
        elif 12 <= hour < 18:
            return f"Доброго дня, {self.name}!"
        elif 18 <= hour < 22:
            return f"Доброго вечора, {self.name}!"
        else:
            return f"Доброї ночі, {self.name}!"

    def additional_info(self):
        return (
            f"По батькові: {self.father_name}\n"
            f"Місто: {self.city}\n"
            f"Телефон: {self.phone_number}\n"
            f"Email: {self.email}\n"
            f"Адреса: {self.adress}\n"
            f"Хоббі: {self.hobbi}"
        )

person = DochClass("Олександр", "Шелепіна", 2006, "Володиморович", "Луцьк", "+38050122947", "lutskhour@ukr.net", "Тиха 10", "Плавання")
print("Вас звуть: ", person.full_name())
print("Ваш вік: ", person.rozrahynok_age(2025))
print(person.age_to_adulthood(2025))
print(person.greeting(10))
print(person.additional_info())