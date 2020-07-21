#!/usr/bin/env python
# coding: utf-8

# <center>
# ## Автор материала: Юрий Кашницкий, ФКН НИУ ВШЭ
# </center>
# Материал распространяется на условиях лицензии <a href="https://opensource.org/licenses/MS-RL">Ms-RL</a>. Можно использовать в любых целях, кроме коммерческих, но с обязательным упоминанием автора материала.

# # Задачи к уроку 2
# http://informatics.mccme.ru/mod/statements/view.php?id=16205

# In[ ]:


# Python 2 and 3 compatibility
# pip install future
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *


# ## Задача A
# Вычислите $2^{179}$. Выведите на экран вычисленное значение.

# In[ ]:


print(2 ** 179)


# ## Задача B
# Вычислите 20!. Выведите на экран вычисленное значение.

# In[ ]:


n = 1
for i in range(2, 21, 1):
    n *= i
print(n)

# from math import factorial
# print(factorial(20))


# ## Задача C
# Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 179 и 971.

# In[ ]:


from math import sqrt
print(sqrt(179 ** 2 + 971 ** 2))


# ## Задача D
# Запишите букву 'A' (латинскую, заглавную) 100 раз подряд. Сдайте на проверку программу, которая выводит эту строчку (только буквы, без кавычек).

# In[ ]:


print(100 * 'A')


# ## Задача E
# Даны два целых числа. Выведите значение наибольшего из них.

# In[ ]:


a, b = int(input()), int(input())
print(a if a >= b else b)


# ## Задача F
# Даны два целых числа. Программа должна вывести число 1, если первое число больше второго, число 2, если второе больше первого или число 0, если они равны.

# In[ ]:


a, b = int(input()), int(input())
if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)


# ## Задача G
# Число 179 записали 50 раз подряд. Полученное 150-значное число возвели в квадрат. Сколько получилось?

# In[ ]:


print(int('179' * 50) ** 2)


# ## Задача H
# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.

# In[ ]:


from math import sqrt
a, b = int(input()), int(input())
print(sqrt(a ** 2 + b ** 2))


# ## Задача I
# Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).
# Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для решения этой задачи?

# In[ ]:


# insert three integers separated by commas
a, b, c = [int(i) for i in input().split(',')]

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)


# ## Задача J
# Даны три натуральных числа a, b, c. Определите, существует ли треугольник с такими сторонами. Если треугольник существует, выведите строку YES, иначе выведите строку NO.
# Треугольник — это три точки, не лежащие на одной прямой.

# In[ ]:


# insert three integers separated by commas
a, b, c = [int(i) for i in input().split(',')]

d = max(a, b, c)

print("YES" if a + b + c > 2 * d else "NO")


# ## Задача K
# Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом.

# In[ ]:


# insert four integers separated by commas
x1, y1, x2, y2 = [int(i) for i in input().split(',')]

print("YES" if (x1 == x2 or y1 == y2) else "NO")


# ## Задача L
# Число $179^{10}$ записали четыре раза подряд. Из получившегося числа извлекли корень степени 10. Сколько получилось?

# In[ ]:


a = int(pow(179, 10))
b = int(str(a) * 4)
print(pow(b, 0.1))


# ## Задача M
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# In[ ]:


year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("YES")
else:
    print("NO")


# # Задача N
# Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.

# In[ ]:


# insert four integers separated by commas
row1, col1, row2, col2 = [int(i) for i in input().split(',')]

horse_steps = [(-2, 1), (-1, 2), (1, 2), (2, 1),
               (2, -1), (1, -2), (-1, -2), (-2, -1)]

print("YES" if (row2 - row1, col2 - col1) in horse_steps else "NO")

