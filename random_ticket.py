import os
import random

def get_numbers_ticket(min, max, quantity):

    i=0
    ticket_list=list()                                          #Створили пустий список
    if (max+1-min)<quantity:                                    #Якщо діапазон нижче ніж кількість чисел \
            ticket_list=None                                        #які потрібно вибрати (значення між min і max)
            print(f'Ви вийшли за діапазон {quantity}')
            return ticket_list                                  #Повертаємо  None
    try:
        for i in range(quantity):                               #Цикл скільки нам потрібно даних
            ticket_list.append(random.randrange(min,max+1))     #Генерація рандмоного числа
            ticket_list.sort()                                  #Сортируємо список по зростанню
        
    except Exception as eror:
        print(f"Error: {eror}")
        start_main_program()
    return ticket_list                                          #Виводимо список лотерельного квітка 


def start_main_program():                                       #Функція ввода данних

    global min, max, quantity                                   #Робимо глобальні змінні
    try:
        
        min=abs(int(input("Min (1)= ")))                        #Вводимо мінімальне абсолютне(+) число 
        max=abs(int(input("Max (1000)= ")))                     #Вводимо максимальне абсолютне число
        quantity=abs(int(input("Number of numbers= ")))         #Вводимо кількість потрібних номерів в білеті 

        
        while min>=1000:                                        #Якщо ми мийшли за діапазон
            print("Ви ввели не правильно введіть ще раз")
            min=abs(int(input("Min (1)= "))) 

        while max >=1000:                                       #Якщо ми мийшли за діапазон
            print("Ви ввели не правильно введіть ще раз")
            max=abs(int(input("Max (1000)= ")))

        while min==max:                                         #Якщо мін та мах однакові5о15211111 
            print(f'Ви ввели мін={min}, та мах= {max} вони однакові')
            min=abs(int(input("Min (1)= ")))                    
            max=abs(int(input("Max (1000)= ")))
        
        if min>max:                                             #Перевірка на всяк випадок якщо мін більше ніж мах міняємо місцями данні
            temp=max
            max=min
            min=temp


    except Exception as eror:
        os.system('cls')
        print(f"Error: {eror}")
        start_main_program()
    

os.system('cls')                                            #Початок программи чистим термінал 
start_main_program()                                        #Головна функція 

ticket_list=list()
print(f'Мінімальний= {min}  Максимальний= {max} Кількість= {quantity}')     #Ввиводимо те що ми записали
ticket_list=get_numbers_ticket(min,max,quantity)                                        #Викликаємо функцію з генерацію рандомних лотерельних білетів
print(f'Список: {ticket_list}')