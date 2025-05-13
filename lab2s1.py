class Osnova:
    def __init__(self, name=None, last_name=None, birth_year=None):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def rozrahynok_age(self, current_year):
        if self.birth_year is None:
            return None
        return current_year - self.birth_year

    def full_name(self):
        return f"{self.name} {self.last_name}" if self.name and self.last_name else None

person = Osnova("Шелепіна", "Олександр", 2006)

print("Вас звуть: ", person.full_name())   
print("Ваш вік: ", person.rozrahynok_age(2025))  
person_default = Osnova()
print(person_default.rozrahynok_age(2025))  
print(person_default.full_name())