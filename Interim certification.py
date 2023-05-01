# Напишите приложение, которое будет запрашивать у пользователя следующие данные
# в произвольном порядке, разделенные пробелом:
# Фамилия Имя Отчество датарождения номертелефона пол
# Форматы данных:
# фамилия, имя, отчество - строки
# дата_рождения - строка формата dd.mm.yyyy
# номер_телефона - целое беззнаковое число без форматирования
# пол - символ латиницей f или m.
# Приложение должно проверить введенные данные по количеству. Если количество не совпадает с требуемым,
# вернуть код ошибки, обработать его и показать пользователю сообщение, что он ввел меньше и больше данных,
# чем требуется.
# Приложение должно попытаться распарсить полученные значения и выделить из них требуемые параметры.
# Если форматы данных не совпадают, нужно бросить исключение, соответствующее типу проблемы.
# Можно использовать встроенные типы java и создать свои. Исключение должно быть корректно обработано,
# пользователю выведено сообщение с информацией, что именно неверно.
# Если всё введено и обработано верно, должен создаться файл с названием, равным фамилии, в него в одну
# строку должны записаться полученные данные, вида
# <Фамилия><Имя><Отчество><датарождения> <номертелефона><пол>
# Однофамильцы должны записаться в один и тот же файл, в отдельные строки.
# Не забудьте закрыть соединение с файлом.
# При возникновении проблемы с чтением-записью в файл, исключение должно быть корректно обработано,
# пользователь должен увидеть стектрейс ошибки.

import os

class CustomError(Exception):
    pass

class NumberOfInputDataWrongError(CustomError):
    """Количество введенных данных не совпадает с требуемым"""

class GenderNotEnteredError(CustomError):
    """Не введен пол в формате: f or m"""

class DateInputError(CustomError):
    """Не введена дата рождения в формате dd.mm.yyyy"""

class NumberEntryError(CustomError):
    """Формат номера телефона - не целое беззнаковое число"""


def split_input_string(input_string):
    person_name = ''
    birth_date = ''
    phone_number = ''
    gender = ''

    for data in input_string:
        if data == 'm' or data == 'f':
            gender = data
        elif data[-4:-1].isdigit() and data[-5] == '.':
            birth_date = data
        elif data.isdigit():
            phone_number = data
        else:
            
            person_name = person_name + ' ' + data
            file_name = (person_name.split())[0] + '.txt'

    if os.path.exists(file_name):
        text_file = open(file_name, 'a+')
        text_file.write(f'\n<{(person_name.split())[0]}><{(person_name.split())[1]}><{(person_name.split())[2]}><{birth_date}><{phone_number}><{gender}>')
        text_file.close()
    else:
        text_file = open(file_name, 'w')
        text_file.write(f'<{(person_name.split())[0]}><{(person_name.split())[1]}><{(person_name.split())[2]}><{birth_date}><{phone_number}><{gender}>')
        text_file.close()

    return person_name, gender, birth_date, phone_number
    
while True:
    input_string = input('Введите следующие данные в произвольном порядке, разделенные пробелом:\n'
                         'фамилия имя отчество - не меняя порядок ФИО\n'
                         'дата_рождения - строка формата dd.mm.yyyy\n'
                         'номер_телефона - целое беззнаковое число без форматирования\n'
                         'пол - символ латиницей f или m : \n').split()

    try:
        gender_entered = False
        date_of_birth_check = False
        phone_number = False

        if len(input_string) < 6:
            raise NumberOfInputDataWrongError(f'ОШИБКА! Количество данных = {len(input_string)} -> меньше требуемых 6\n'
                                              'Попробуйте ввести ещё раз\n')
        elif len(input_string) > 6:
            raise NumberOfInputDataWrongError(f'ОШИБКА! Количество данных = {len(input_string)} -> больше требуемых 6\n'
                                              'Попробуйте ввести ещё раз\n')
        elif not gender_entered:
            for data in input_string:
                if data == 'm' or data == 'f':
                    gender_entered = True
            if gender_entered:
                pass
            else:
                raise GenderNotEnteredError('ОШИБКА ! Не введен пол в формате: f or m')

        elif not date_of_birth_check:
            for data in input_string:
                if data[-4:-1].isdigit() and data[-5] == '.':
                    date_of_birth_check = True
            if date_of_birth_check:
                pass
            else:
                raise DateInputError('Ошибка! не введена дата рождения в нужном формате')
            
        elif not phone_number:
            for data in input_string:
                if data.isdigit():
                    phone_numberk = True
            if phone_number:
                pass
            else:
                raise NumberEntryError('Ошибка! не введен номер телефона, как целое беззнаковое число')       

    except NumberOfInputDataWrongError as e:
        print(e)
    except GenderNotEnteredError as e:
        print(e)
    except DateInputError as e:
        print(e)
    except NumberEntryError as e:
        print(e)
    else:
        split_input_string(input_string)
        break
