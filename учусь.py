# comment
# import sys

# print("Рузультат:",5, 15, 52, sep=".", end="!\n")
# print('Second \' \t \\ L\ni\nn\ne')

# print('x y w z')
# from itertools import product
# for x,y,w,z in product(range(0,2),repeat = 4):
# f = ((x <= y) and (y <= w)) or ( z == (x or y))
# if  not f:
# print(x,y,w,z)

# print('x y w z')
# from itertools import product
# for x,y,w,z in product(range(0,2),repeat = 4):
# f = (x == (w or y)) or ((w <= z) and (y <= w))
# if not f:
# print(x,y,w,z)
# a = int(input())
# print(3*a**2 + 5*a - 21)

# a = int(input())
# print((a ** 2 + 10) / (a ** 2 + 1) ** 0.5)


# номер( 2.4 )
# a = int(input())
# print(4*a)

# номер( 2.5 )
# a = int(input())
# print(2*a)

# номер( 2.6 )
# R = 6350
# a = int(input())
# print((2*R*a)**0.5)

# номер( 2.7 )
# a = int(input())
# print('Обем куба:', a**3,'\n' "Площадь боковой поверхности", 4*a**2)

# номер( 2.8 )
# r = int(input())
# from math import pi
# print("Длина окружности", 2*pi*r,'\n' "Площадь круга", pi*r**2)

# номер ( 2.9 (а))
# x = int(input())
# y = int(input())
# print(2*x**3 - 3.44*x*y + 2.3*x**2 - 7.1*y +2)

# номер ( 2.9 (б))
# a = int(input())
# b = int(input())
# print(3.14 * (a + b) ** 3 + 2.75 * b ** 2 - 12.7 * a - 4.1)


# номер ( 2.10 )
# a = int(input())
# b = int(input())
# S = (a + b) / 2
# G = (a * b )**0.5
# print("Среднее арифметическое:", S ,'\n' "Среднее геометрическое:", G)

# номер ( 2.11 )
# print("Введите объём тела")
# V = int(input())
# print("Введите массу тела")
# m = int(input())
# P = m / V
# print("плотность материала тела составляет:", P)

# номер ( 2.12 )
# print("Введите общаю численность населения")
# N = int(input())
# print("Введите площадь территории")
# S = int(input())
# D = N / S
# print("плотность населения", D )

# номер ( 2.13 )
# a = int(input())
# if a == 0:
#   print('Это значение не подходит')
#    sys.exit()
# b = int(input())
# x = -(b/a)
# print(x)


# номер ( 2.14 )
# print("Введитее значение двух катетов", '\n' "1 катет")
# a = int(input())
# print("2 катет")
# b = int(input())
# c = (a**2 + b**2)**0.5
# print("Гипотенуза равняется",c )


#  номер ( 2.15 ) 
# from math import pi
# print ("Введите значения внешнего радиуса:")
# R = int(input())
# print ("Введите значения внутреннего радиуса:")
# r = int(input())
# P = pi*(R**2-r**2)
# print("Площадь кольцы равняется:", P)


#  номер ( 2.16 )
# print("Введитее значение двух катетов", '\n' "1 катет")
# a = int(input())
# print("2 катет")
# b = int(input())
# print("3 катет")
# c = int(input())
# P = a + b + c
# print("Периметр равен:",P)


#  номер ( 2.17 )
# print("Введитее значение основания трапеции", '\n' "1 занчение")
# a = int(input())
# print("2 занчение")
# b = int(input())
# print("Введитее значение высоты трапеции")
# h = int(input())
# x = (a - b) / 2
# L = (x ** 2 + h ** 2) ** 0.5
# P = a + b + 2*L
# print(P)


# номер (6.7)
# n = int(input())
# k = 0
# while k**2<=n:
#     k += 2
#     print(k)


# номер (6.8)
# n = int(input())
# k = 1
# while k**2 <= n:
#     k += 1
#     if k ** 2 % 2 == 0 and k**2 >= n:
#         print(k)

# номер (6.9)
# n = int(input())
# if n % 2 != 0:
#     while n % 2 != 0:
#         print("Ошибка")
#         n = int(input())

# номер(6.10)
# password_1 = input("Придумайте пароль! ")
# password = input("Введите пароль: ")
# while password != password_1:
#     print("Неверный пароль!")
#     password = input("Попробуйдте еще раз: ")
# print("Пороль верный. Добро пожаловать! ")




# номер(6.11)
# n = int(input())
# k = 1
# while k < 10:
#         k +=1
#         if n == 0: break
#         n = int(input())



from itertools import permutations
word = '0123456789'
c = 0
for j in range(1,11):
    for i in permutations(word,j):
        x = ''.join(i)
        if x[0] != '0' and (x[-1] == '5' or x[-1] == '0'):
            c += 1
print(c + 1) #+1 случай когда число равно 0






