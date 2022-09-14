# 1.1 Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# 1.2 Текст и количество повторений нужно ввести с помощью input()

#1.1
text = input('Enter text: ')
num = int(input('Number of repetions: '))
print(text*num)
#1.2
text = input('Enter text: ')
num = int(input('Number of repetions: '))
i = 1
for i in range(i, num+1):
    print(text)
