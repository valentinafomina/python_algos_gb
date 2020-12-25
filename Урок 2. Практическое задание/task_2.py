"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
even_numbers = 0
odd_numbers = 0


def odd_or_even_count(user_input, i):
    global even_numbers
    global odd_numbers
    if i != len(user_input):
        res = (int(user_input[i])) % 2
        if res == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
        odd_or_even_count(user_input, i + 1)


odd_or_even_count(input('Введите натуральное число: '), 0)
print(odd_numbers, even_numbers)


