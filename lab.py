'''
Натуральные числа.
Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр (прописью) и их количество выводится отдельно.
'''
#Проверка числа по условию задачи
def check_num(gived_num, k):
    if gived_num.isdigit() and (int(gived_num) % 2 != 0)and(len(gived_num) % 2 == 0)and(len(gived_num) > k):
        return True
    return False

#Словарь с цифрами
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
#Лист для вывода
output_arr = []
#Число К
k = int(input('Число К: \n'))
#Баффер
gived_num = '1'
#Выбор файла
file_name = "text.txt"

try:
    open(file_name, 'r')
except:
    print('Файл отсутствует в директории проекта')
    exit()

with open(file_name, 'r') as file:
    while 1:
        gived_num = file.readline().replace('\n', '')
        if not gived_num:
            #print('Файл закончился')
            break
        if check_num(gived_num, k):
            output_arr.append(gived_num)

#Вывод подходящих чисел
for output_num in output_arr:
    print(output_num)
    cifr = []
    for i in output_num:
        if i not in cifr:
            cifr.append(i)
    cifr = sorted(cifr, key= lambda x: int(x))
    print('Количество использованных цифр:')
    print(len(cifr))
    cifr_propis = list(map(lambda x: dc_cifr[x], cifr))
    print('Использованные цифры:')
    print(*cifr_propis, sep=', ')
    print('___________________\n')