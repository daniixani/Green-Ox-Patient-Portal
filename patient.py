import json
from datetime import datetime, date


class Patient:
    def __init__(self, name: str, birthday: str = None):
        self.name = name
        self.birthday = birthday

    def read(self):
        """reads the contents of the file"""
        raw = open(f'patients/{self.name}.json').read()
        data = json.loads(raw)

        self.name = data["name"]
        self.birthday = data["birthday"]

    def age(self):
        """calcualtes the age of the patient based on birthday"""
        today = date.today()
        birthday = datetime.strptime(self.birthday, "%m/%d/%Y")
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    def save(self):
        """saves the patient to a file"""
        file = open(f"patients/{self.name}.json", "w")

        file.write(json.dumps({
            'name': self.name,
            'birthday': self.birthday
        }))

    def __repr__(self):
        """this is defines how it's printed when you use print(str())"""
        return self.name

    def __str__(self):
        """this is defines how it's printed when you use print()"""
        return f"name: {self.name}\nage: {self.age()}"
