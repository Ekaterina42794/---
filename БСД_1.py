'''Практическое задание
Практическое задание по уроку "Базовые структуры данных"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.
Практическое задание по уроку "Базовые структуры данных"
Цель: применить и закрепить базовые знания о структурах данных, решив набор задач.

Формат решения:
Можете написать код всех задач в одном файле main.py.
Можете написать код в разных файлах к каждой задаче: task1.py, task2.py и т.д.

Задачи.
Предисловие:
Если в задаче говориться о том, что нужно вывести результат арифметических действий, сравнения и других операций,
то вам нужно сначала составить выражение с исходными данными, а не вывести результат этого выражения сразу.
Пример: сложите числа 12 и 89, вычтите число1 и выведите результат на экран,
Верно: print(12 + 89 - 1)
Не верно: print(100)



Задача 2 (просто) "Логика":
Напишите в начале программы однострочный комментарий: "2nd program".
Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
 Предполагаемый результат: True

Задача 3 (средне) "Школьная загадка":
Напишите в начале программы однострочный комментарий: "3rd program".
Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 без приоритета.
Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
Выведите на экран(в консоль) результат сравнения этих двух выражений.
Предполагаемый результат (с использованием ==): False

Задача 4 (сложно) "Первый после точки":
Напишите в начале программы однострочный комментарий: "4th program".
Дана строка '123.456'.
Вывести на экран первую цифру после запятой - 4.
Начало алгоритма решения:
Преобразуйте в строку в дробное число. ('123.456' -> 123.456)
Умножьте на 10, чтобы сместить 4 в целую часть. (1234.56)
Следующие шаги алгоритма составьте самостоятельно. В них вам понадобится команда int() и остаточное деление на 10.

Примечания:
Старайтесь не торопиться и делать перерывы, если зашли в тупик при решении.
Выполняйте задания пошагово: написали строку -> проверили, что она делает -> перешли к следующей.
Для вывода значений используйте команду(функцию) print(). Можно перечислять сразу несколько значений.
Для отделения целой части от дробно числа можно использовать команду(функцию) int()
Основные арифметические действия: +, -, *, /, //, %, **.
Основные операторы сравнения: <, >, ==, !=, <=, >=.
Логические операторы: or(или), and(и).
Файл(-ы) прикрепите к этому домашнему заданию в виде архива или ссылки на GitHub репозиторий с вашим кодом.'''

# Задача 1 (просто) "Арифметика":
# Напишите в начале программы однострочный комментарий: "1st program".
# Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
# Предполагаемый результат: 15.0
print("Задача 1 - Арифметика")
#"1st program"
print('(9^0.5)*5 =',(9**0.5)*5)
print()
#Задача 2 (просто) "Логика":
# Напишите в начале программы однострочный комментарий: "2nd program".
# Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
# Предполагаемый результат: True
print('Задача 2 - "Логика"')
#"2nd program"
print('9.99>9.98 и 1000 не = 1000.1   -  ',9.99>9.978 and 1000!=1000.1)
print('9.99>9.98 или 1000 не = 1000   -  ',9.99>9.978 or 1000!=1000)
print('9.99=9.98 или 1000 не = 1000   -  ',9.99==9.978 or 1000!=1000)
print()

#Задача 3 (средне) "Школьная загадка":
# Напишите в начале программы однострочный комментарий: "3rd program".
# Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 без приоритета.
# Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
# Выведите на экран(в консоль) результат сравнения этих двух выражений.
# Предполагаемый результат (с использованием ==): False
print('Задача 3 - "Школьная загадка"')
#"3rd program"
a=2*2+2
b=2*(2+2)
print('2*2+2=',a)
print('2*(2+2)=',b)
print(a,'>',b,'-', a>b)
print(a,'=',b,'-', a==b)
print(a,'<',b,'-', a<b)
print()

print('Задача 4 - "Первый после точки"')
#Задача 4 (сложно) "Первый после точки":
# Напишите в начале программы однострочный комментарий: "4th program".
# Дана строка '123.456'.
# Вывести на экран первую цифру после запятой - 4.
# Начало алгоритма решения:
# Преобразуйте в строку в дробное число. ('123.456' -> 123.456)
# Умножьте на 10, чтобы сместить 4 в целую часть. (1234.56)
# Следующие шаги алгоритма составьте самостоятельно. В них вам понадобится команда int() и остаточное деление на 10.


#"4th program"
# 1ый вариант
a = '123.456'
a = float(a)
print(a, type(a))
a = a * 10
a = a % 10
a=int(a)
print(a,type(a))
print()

# 2ой вариант
print('"123.456"')
b = '123.456'
print('1-ая цифра после запятой из строки - ', b[4])
c = b[4]
c=int(c)
print(c, type(c))

