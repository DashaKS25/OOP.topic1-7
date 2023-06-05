import json

class Phone:
    def __init__(self, number):
        self.number = number
        self.call_counter = 0

    def set_number(self, number):
        self.number = number

    def get_call_count(self):
        return self.call_counter

    def receive_call(self):
        self.call_counter += 1

    def __str__(self):
        return f"Phone number: {self.number}, Call count: {self.call_counter}"

def total_call_count(phones):
    total_count = 0
    for phone in phones:
        total_count += phone.get_call_count()
    return total_count

phone1 = Phone('123456789')
phone2 = Phone('987654321')
phone3 = Phone('555555555')

phone1.set_number('111111111')
phone2.set_number('222222222')
phone3.set_number('333333333')

phone1.receive_call()
phone1.receive_call()
phone2.receive_call()
phone2.receive_call()
phone2.receive_call()
phone3.receive_call()
phone3.receive_call()
phone3.receive_call()
phone3.receive_call()

phones = [phone1, phone2, phone3]
total_calls = total_call_count(phones)
print("Amount received calls:", total_calls)

data = []
for phone in phones:
    data.append({
        'number': phone.number,
        'call_count': phone.get_call_count()
    })

with open('call_logs.json', 'a') as file:
    json.dump(data, file, indent=4)
