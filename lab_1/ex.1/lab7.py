#1. Информация об учебных курсах. Напишите программу, которая создает словарь, содержащий номера курсов и номера аудиторий, 
# где проводятся курсы. Словарь должен иметь приведенные в табл. 1 пары "ключ: значение". Программа должна также создать словарь,
# содержащий номера курсов и имена преподавателей, которые ведут каждый курс. Словарь должен иметь приведенные в табл. 
# 2 пары "ключ: значение".Программа также должна создать словарь, содержащий номера курсов и время проведения каждого курса. 
# Словарь должен иметь приведенные в табл. 3 пары "ключ: значение". Программа должна позволить пользователю ввести номер курса, 
# а затем показать номер аудитории, имя преподавателя и время проведения курса.

aud = {
        'CS101': '3004',
        'CS102': '4501',
        'CS103': '6755',
        'CS104': '1244',
        'CS105': '1411',
    }
prof = {
        'CS101': 'Хайнс',
        'CS102': 'Альварадо',
        'CS103': 'Рич',
        'NT110': 'Берк',
        'SM241': 'Ли',
    }
time = {
        'CS101': '8:00',
        'CS102': '9:00',
        'CS103': '10:00',
        'NT110': '11:00',
        'SM241': '13:00',
    }
a = input("Введите номер курса: ")


if a in aud.keys():
        print('Аудитория: ', aud[a])
if a in prof.keys():
        print('Преподаватель: ', prof[a])
if a in time.keys():
        print('Время: ', time[a])
if a not in aud.keys() and a not in prof.keys() and a not in time.keys():
        print('Нет данных.')