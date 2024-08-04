from phone import Phone
from name import Name

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
         self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
         self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone, new_phone):
         self.phones = [Phone(new_phone) if p.value == old_phone else p for p in self.phones]
     
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"