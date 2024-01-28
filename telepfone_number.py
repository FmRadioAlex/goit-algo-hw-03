import os
import re

raw_numbers = [
    "380501234567",
    "    +38(050)123-32-34",
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):
    p='\d+'                                             # '\d'- Збігається з будь-якою десятковою цифрою. Дорівнює[0-9]
    phone_number=''.join(re.findall(p,phone_number))    # Метод re.findall()повертає список рядків, що містить усі збіги.
    if len(phone_number)==10:
        phone_number="+38"+phone_number
    elif len(phone_number)==12:
        phone_number="+"+phone_number
    return phone_number

os.system('cls')
for k,numbers in enumerate(raw_numbers):
    raw_numbers[k]=normalize_phone(numbers)
   
print("Нормалізовані номери телефонів для SMS-розсилки:", raw_numbers)