'''
Натуральные числа.
Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр (прописью) и их количество выводится отдельно.
'''

dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
output_arr = []

k = int(input('Число К: \n'))

gived_num = '1'

choice = input('Как вводятся лексемы:\n1) Вручную; \n2) Из файла; \n').lower()

if choice in ['1', 'one', 'hand', 'вручную']:
    while gived_num:
        gived_num = input('Число из потока: \n')

        if gived_num in ['0', 'exit', 'stop', 'cancel', 'out']:
            break

        num = 0

        try:
            num = int(gived_num)
        except:
            print('Неверно заданно натуральное число.')
            continue

        n = len(gived_num)

        if (n > k) and (n % 2 == 0) and (num % 2 != 0):
            output_arr.append(gived_num)

elif choice in ['2', 'two', 'file', 'из файла']:
    file_name = input('Имя файла:\n')
    gived_num = ''

    with open(file_name, 'r') as file:
        while gived_num != '000':
            gived_num = ''
            c = file.read(1)

            if not c:
                break

            while c != ' ' and c:
                gived_num += c
                c = file.read(1)

            num = 0

            try:
                num = int(gived_num)
            except:
                continue

            n = len(gived_num)

            if (n > k) and (n % 2 == 0) and (num % 2 != 0):
                output_arr.append(gived_num)

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