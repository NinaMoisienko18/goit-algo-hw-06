from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value) #викликаємо батьківський конструктор, передаючи класу Name значення value


class Phone(Field):
    def __init__(self, value):
        number_pattern = r"\b\d{10}\b"
        if re.match(number_pattern, value):
            super().__init__(value)

        else:
            count_figures = []
            for i in value:
                count_figures.append(i)

            print(f"Number - {value} - incorrect, it has {len(count_figures)} figures")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone):
        if phone in self.phones:
            return phone
        else:
            return f"Number: {phone} not in Adress book."

    def add_phone(self, phone):
        self.pnone = Phone(phone)
        if len(self.phones) == 0 or phone not in self.phones:
            self.phones.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, phone_old, phone_new):
        old_number = Phone(phone_old)
        new_number = Phone(phone_new)
        if old_number in self.phones and new_number not in self.phones:
            idx = self.phones.index(old_number)
            self.phones[idx] = new_number
        else:
            return f"Such number {old_number} isn't in Adress book"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(map(str, self.phones))}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

        else:
            return f"Record for {name} not found in Address book."

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            return f"Record for {name} not found in Address book."



book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
book.delete("Jane")
print(book.find("Jane"))

nina_recors = Record("Nina")
nina_recors.add_phone("2312154354436756765")
nina = book.find("Nina")
print(nina)
