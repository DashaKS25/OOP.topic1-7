import json

class Phone:
    def __init__(self, number):   # Задаємо клас Телофон
        self.number = number
        self.call_counter = 0

    def set_number(self, number):   # Створюємо поле для опису
        self.number = number

    def get_call_count(self):         #Повертаємо к-ть прийнятих дзвінків
        return self.call_counter

    def receive_call(self):          #Приймаємо дзвінки, лічильник +1
        self.call_counter += 1

def total_call_count(phones):
    total_count = 0
    for phone in phones:
        total_count += phone.get_call_count()
    return total_count

# Створення об'єктів телефонів
phone1 = Phone('123456789')
phone2 = Phone('987654321')
phone3 = Phone('555555555')

# Зміна номерів телефонів
phone1.set_number('111111111')
phone2.set_number('222222222')
phone3.set_number('333333333')

# Прийом дзвінків
phone1.receive_call()
phone1.receive_call()
phone2.receive_call()
phone2.receive_call()
phone2.receive_call()
phone3.receive_call()
phone3.receive_call()
phone3.receive_call()
phone3.receive_call()

# Підрахунок загальної кількості прийнятих дзвінків
phones = [phone1, phone2, phone3]
total_calls = total_call_count(phones)
print("Amount recive calls:", total_calls)

# Збереження інформації про дзвінки у файл
data = []
for phone in phones:
    data.append({
        'number': phone.number,
        'call_count': phone.get_call_count()
    })

with open('call_logs.json', 'a') as file:     #Зберігаємо інформацію про прийняті дзвінки у файл
    json.dump(data, file)
