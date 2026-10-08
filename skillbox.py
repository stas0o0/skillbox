# a = 6
# b = 2
# c = 0
# if b < a:
#     c = a * b
#     print(c)
# from ctypes import c_float_complex
# from itertools import count

# from itertools import count
# from turtledemo.round_dance import stop

# bank = int(input("Введите состояние счета: "))
# course = 75000
# if bank >= course:
#     bank = bank - course
#     print("Курс успешно приобретен!")
# else:
#     print("Не достаточно денег!")
# print("Хорошего дня!")


# number = int(input("Введите число: "))
#
# if number % 2 == 0:
#     print("Число чётное")


# number_1 = int(input("Введите первое число: "))
# number_2 = int(input("Введите второе число: "))
# number_3 = int(input("Сумма этих чисел: "))
# summ = number_1 + number_2
# if summ == number_3:
#     print("Ответ верный: ")
# else:
#     print("Ответ не верный")
#     print("Правельный результат:", summ)


# a = int(input())
# b = int(input())
# c = int(input())
# if c>b and c>a:
#     print(c)
# if b>a and b>c:
#     print(b)
# if a>b and a>c:
#     print(a)


# x = int(input())
# y = int(input())
# if x > y:
#     print(x,"Больше", y)
# if x == y:
#     print(x,"Равен", y)
# if x < y:
#     print(x,"Меньше", y)


# balls = int(input("солько баллов у игра? "))
#    artifact_cost = 55000
# if balls >= artifact_cost :
#     balls -= artifact_cost
#     print("Артефакт успешно приобретён!")
#     if balls < 5000:
#         balls +=1000
#         print("Получен бонус! ")
# else:
#     print("Недостаточно баллов для покупки! ")
# print("Остаток баллов: ", balls)
# print("Удачной игры!")


# money = int(input("Сколько мама дала денег? "))
# cheese = 60
# ice_cream = 20
# if money >= cheese:
#     print("На сыр денег хватило!")
#     money -= cheese
#     if money >= ice_cream:
#         print("И на мороженое тоже")
#     else:
#         print("Денег маловато")
# else:
#     print("Денег не хватило даже на сыр!")


# cargo_1 = int(input())
# cargo_2 = int(input())
# if cargo_1 > cargo_2:
#     print("Первый груз тяжелее второго ")
# elif cargo_1 < cargo_2:
#     print("Второй груз тяжелее первого")
# else:
#     print("Оба груза весят одинаково")


# profit = int(input("Введите свою зарплату"))
# if profit < 0:
#     print("Ошибка: доход не может быть отрицательным")
# else:
#     if profit < 10000 :
#         tax = profit*13/100
#         print("Cтавка налога (13%) равняется: ", tax)
#     elif profit <50000:
#         tax = profit * 20 / 100
#         print("Cтавка налога (20%) равняется: ", tax)
#     else:
#         tax = profit * 30 / 100
#         print("Cтавка налога (30%) равняется: ", tax)


# coin_1 = int(input("Введите вес 1й монетки:"))
# coin_2 = int(input("Введите вес 2й монетки:"))
# coin_3 = int(input("Введите вес 3й монетки:"))
# if coin_1 == coin_2:
#     print("Третия легче")
# elif coin_1 < coin_2:
#     print("Первая легче")
# else:
#     print("Вторя легче")


# older = int(input("Введите  свой возраст: "))
# time = int(input("Введите время за которое вы пробежали 100 метров: "))
# if older <= 18 and time <= 15:
#     print("Вы подходит")
# else:
#     print("Извегите вы неподходите")
# print("Удачи!")


# balls = int(input("Сколько баллов набрал? "))
# medal = int(input("Есть медаль?(Введите (1) при наличии, (0) если нету. "))
# if balls >= 280 and medal == 1:
#     print("Поздравляем! Ты поступил! ")
# else:
#     print("К сожелению, ты не прошёл в наш университет.")


# temperature = int(input("Введите температуру: "))
# if temperature < 0 or temperature > 100:
#     print("Опасно! Температура не подходит!")
# else:
#     print("Температура в пределах нормы.")


# time = int(input("Введтите время: "))
# if time >=8 and time <=10 or time >= 12 and time < 14 or time >= 15 and time < 18 or time >= 20 and time < 22:
#     print("Можно получить посылку")
# else:
#     print("Посылку получить нельзя")


# password_1 = input("Придумайте пароль! ")
# password = input("Введите пароль: ")
# while password != password_1:
#     print("Неверный пароль!")
#     password = input("Попробуйдте еще раз: ")
# print("Пороль верный. Добро пожаловать! ")


# balans = int(input("Сколько денег пришло? "))
# while balans > 5000:
#     prise = int(input("Введите стоистоть товара: "))
#     balans -= prise
# print("Внимание! На болансе мало денег! Остановитесь!")
# print("Баланс счета", balans)


# number = int(input('Введите число: '))
# total = 0
# while number != 0:
#     total += numb
#     number = int(input('Введите число: '))
# print(total)


# number = 0
# while number < 98:
#     number += 7
#     print(number)


# weather = int(input("`Введите градусы на улице: "))
# km = 0
# while weather > 15:
#     km += 20
#     weather -= 2
#     if  weather < 15:
#         break
#     km += 10
# print(km)


# numbers = int(input("Ведите число: "))
# summ = 0
# while numbers != 0:
#     last_num =  numbers % 10
#     summ += last_num
#     if numbers == 5:
#         break
#     numbers = numbers // 10
#     print(last_num)
# print(summ)


# books = int(input("Сколько книг выдал библиотекарь? "))
# summ =  0
# summ_2 = 0
# while summ != books:
#     books_chek = int(input("Сколько книг просмотрено? "))
#     restoration = int(input("Сколько из них требует реставрации? "))
#     summ += books_chek
#     summ_2 += restoration
#     if summ_2 >= 5:
#         print("Библиотекарь: На сегодня всё. Благодарю за помощь!")
#         print("Ура! Практика завершена!")
#         break
#     if summ >= books:
#         print("Библиотекарь: На сегодня всё. Благодарю за помощь!")
#         print("Цель практики ещё не достигнута — встретимся завтра.")
#         break


# money = int(input("Введите стартовую сумму: "))
# while money  <= 10000:
#     number = int(input("Сколько выпало на кубике? "))
#     if number != 3:
#         money = money + 500
#         print("Выиграли 500 рублей!")
#     else:
#         money = 0
#         print("Вы проиграли всё!")
#         break
# print("Игра закончена.")
# print("Итого осталось: ", money)


# count = 10
# while count <= 10:
#     if count == 0:
#         print('Время вышло!')
#         break
#     else:
#         print(count)
#         count -= 1


# while True:
#     active = int(input("Продолжаем работать? 1/0: "))
#     if active == 0:
#         print("Приложение закрывается…")
#         break
# print("Работа завершена")


# exit_code = 550
# while True:
#     print("Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!")
#     user_code = int(input("Введите код: "))
#     if user_code == exit_code:
#         print("Код верный, завершаю работу...")
#         break


# count = int(input("сколько раз вывести програу? "))
# count_1 = 0
# while count_1 < count:
#     print("Я — программист!")
#     count_1 += 1


# count = int(input("Введите количесвто напоминаний: "))
# count_1 = 0
# while count_1 < count:
#     count_1 += 1
#     print("Вы хотели не забыть о чём-то")


# print("Программа для отслеживания температуры")
# count_failures = 0
# stop_program = False
# last_temperature = -999
#
# while not stop_program:
#     sensor = int(input("Какая температура на датчике? "))
#     if sensor == last_temperature:
#         count_failures += 1
#         print("Внимание: дублирующее значение температуры", sensor, "обнаружено!")
#         print("Зафиксировано сбоев датчика:", count_failures)
#
#         continue_collecting_data = int(input("Хотите продолжить сбор данных? 1-да, 0-нет: "))
#         if continue_collecting_data == 0:
#             print("Сбор данных остановлен")
#             stop_program = True
#     last_temperature = sensor


# n = int(input("Введите число: "))
# number = 1
# while number <= n:
#   print(number**3)
#   number +=

# n = int(input())
# y = len(str(n))
# print(y)


#
# print("Начался восьмичасовой рабочий день.")
# n = 1
# summ = 0
# num = 0
# while n <= 8:
#     print(n,"-час")
#     n += 1
#     work = int(input("Сколько задач решит Максим? "))
#     summ += work
#     while num == 0:
#         wife = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
#         break
#     if wife == 1:
#         num = 1
# print("Рабочий день закончился. Всего выполнено задач:", summ)
#
# if num == 1:
#     print("Нужно зайти в магазин.")
# else:
#     print()


# x = int(input("Вклад в банке: "))
# y = int(input("Проценты: "))
# p = int(input("Порог вклада: "))
# n = 0
# while x < p:
#     n += 1
#     print(n,"год.",x + (((x / 100)*y)//1))
#     x = x + (((x / 100)*y)//1)
# print("Кол-во лет для достижения порога:",n)


# number = int(input("Введите число: "))
# isPrime = True
# for divider in range(2, number):
#     if number % divider == 0:
#         isPrime = False
#         break
# if isPrime:
#     print("Число простое")
# else:
#     print("Число составное")


# seconds = int(input('Введите время для обратного отсчёта (в секундах): '))
# print('Таймер установлен на', seconds, 'секунд.')
# for timer in range(seconds, 0, -1):
#    print('Осталось секунд:', timer)
#    answer = int(input('Введите 1, если еда готова, или 0, чтобы продолжить: '))
#    if answer == 1:
#        print('Ваша еда готова, можете забрать! Таймер был прерван на', timer, 'секундах')
#        break
# else:
#    print('Ваша еда готова. Осторожно, горячo!')


# summ = 1
# for i in range(100,0,-4):
#     print("К началу месяца ",summ," у вас останется", i, 'кг гречки')
#     summ += 1
# print("К началу месяца", summ, 'у вас останется 0 кг гречкиm')
# print("Запасы гречки закончились!")


# start = -2
# end =  2
# step = -1
# if start < end:
#     start, end = end, start
# if step > 0:
#     step = -step
#
# for x in range(start, end - 1, step):
#     y = x ** 3 + 2 * (x ** 2) - 4 * x + 1
#     print('В точке', x, 'функция равна', y)


# educational_grant = 10000
# expenses = 12000
# total_enough = 0
# for i in range(1, 11):
#     not_enough = expenses - educational_grant
#
#     print(i, "месяц: траты", expenses, "рублей, не хватает", not_enough, "рублей.")
#     total_enough += int(expenses - educational_grant)
#     expenses += int(0.03 * expenses)
#
# print("Сумма денег, которую необходимо получить у родителей:", total_enough, "рублей.")


# a = int(input())
# print(a)
# x = 0
# for i in range(a, 100,2):
#     print(i)
# while a %2==0:
#     x +=1
# print(x)


# upper_letter = "Ы"
# lower_letter = "ы"
# upper_count = 0
# lower_count = 0
#
# phrase_in = input("Введите текст: ")
# for symbol in phrase_in:
#     if symbol == upper_letter:
#         upper_count += 1
#     elif symbol == lower_letter:
#         lower_count += 1
#
# print("Больших букв Ы: ", upper_count)
# print("Маленьких букв Ы: ", lower_count)


# rows = 5
# sittings = 7
# meters = 3
#
#
# print('Сцена')
#
# sittings_symbols = "=" * sittings + " "
# meters_symbols = "*" * meters + " "
#
# to_print = sittings_symbols + meters_symbols + sittings_symbols
# for _ in range(rows):
#     print(to_print)


# text = input("Ввелите тест: ")
# max_len = 0
# length = 0
# for sym in text:
#     if sym != ' ':
#         length += 1
#     else:
#         length = 0
#     if length > max_len:
#         max_len = length
#
# print('Длина самого длинного слова:', max_len)


# stalls = "abababaaaa"
# milk = 0
# milk_stalls = 2
# for stall in stalls:
#      if stall == 'b':
#           milk += milk_stalls
#      milk_stalls += 2
# print('Произведено молока за день:', milk)


# for i in range(6):
#     for j in range(6):
#         number = i+j*2
#         print(number, end="\t")
#     print()

# n = int(input("Введите число: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# x_lim = int(input("Введите ширину: "))
# y_lim = int(input("Введите высоту: "))
# for y in range(y_lim):
#     for x in range(x_lim):
#         if x == 0 or x == x_lim-1:
#             print("|", end='')
#         elif y == 0 or y == y_lim-1:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()


# summ = 0
# number = int(input("Ввелите количество чисел: "))
# for i in range(number):
#     num1 = int(input("Введите число: "))
#     if num1 >1:
#         divisors = 0
#         for j in range(1, num1+1):
#             if num1 % j == 0:
#                 divisors += 1
#         if divisors == 2:
#             summ += 1
# print("Количество простых чисел в последовательности: ", summ)


# num = int(input("Введите количество чисел: "))
#
# max_summ =-1
# best_number = 0
#
# for i in  range(num):
#     number = int(input("Введите число: "))
#     temp = number
#     sum_digits = 0
#     while temp > 0:
#         sum_digits += temp % 10
#         temp //= 10
#     if sum_digits > max_summ:
#         max_summ = sum_digits
#         best_number = number
# print("Число", best_number, "имеет максимальную сумму цифр", max_summ)


# height = int(input("Введите высоту пирамиды: "))
# for i in range(1, height + 1):
#     for j in range(height - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("#", end="")
#     print()
