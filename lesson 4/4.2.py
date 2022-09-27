# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных
# аргументов и выводит их построчно в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def emp(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}:{v}')

emp(surname = 'Ivanov', name = 'Ivan', age = 30, job = 'QA')