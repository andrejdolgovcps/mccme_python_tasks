#!/usr/bin/env python
# coding: utf-8

# <center>
# <img src="../img/python_theme.png">
# # MLClass. "Прикладной анализ данных"
# # Модуль "Инструментарий Data Science"
# <img src="../img/mlclass_logo.jpg" height="240" width="240">
# 
# ## Автор материала: Юрий Кашницкий, ФКН НИУ ВШЭ
# </center>
# Материал распространяется на условиях лицензии <a href="https://opensource.org/licenses/MS-RL">Ms-RL</a>. Можно использовать в любых целях, кроме коммерческих, но с обязательным упоминанием автора материала.

# # Задачи к уроку 3
# http://informatics.mccme.ru/mod/statements/view.php?id=16206#1

# In[ ]:


# Python 2 and 3 compatibility
# pip install future
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *


# ## Задача A
# Даны два целых числа A и B (при этом A $\leq$ B). Выведите все числа от A до B включительно.

# In[2]:


a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)


# ## Задача B
# По данному натуральном n вычислите сумму $1^2+2^2+3^2+ \ldots +n^2$.

# In[3]:


n = int(input())
sum = 0
for i in range(1, n+1):
  sum += i**2
print(sum)


# ## Задача C
# По данному целому неотрицательному n вычислите значение n!.

# In[21]:


import math
n = input()
res = math.factorial(n)
print(res)


# Второй способ - собственная реализация факториала

# In[6]:


n = int(input())

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
fac(n)


# ## Задача D
# По данным целым неотрицательным n и k вычислите значение числа сочетаний из n элементов по k, то есть $\frac{n!}{k!(n-k)!}$.

# In[9]:


n = int(input())
k = int(input())

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

c = fac(n)/(fac(k)*fac(n-k))
print(c)


# ## Задача E
# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов. Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду разработки.
# 
# 

# In[2]:


penguine = ["   _~_    ",
            "  (o o)   ",
            " /  V  \ ",
            "/(  _  )\ ",
            "  ^^ ^^   "]
 
n = int(input())
for i in range(len(penguine)):

    print(penguine[i] * n)


# In[17]:


from tabulate import tabulate
headers = ['penguine'] 

penguine = ["   _~_    ",
            "  (o o)   ",
            " /  V  \ ",
            "/(  _  )\ ",
            "  ^^ ^^   "]  
n = int(input())
for i in range(n):
    table = zip(penguine)
    print(tabulate(table, headers=headers))


# ## Задача F
# Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части. Определите, можно ли таким образом отломить от шоколадки ровно k долек.

# In[18]:


n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')


# ## Задача G
# Дано линейное уравнение $ax + b = 0$. Решите уравнение, напечатайте ответ. Если ответов бесконечно много, выведите "INF", если их нет - "NO".

# In[68]:


a = float(input())
b = float(input())

if (a == 0 and b == 0):
    print('INF')
elif (a == 0 and b !=0):
    print('NO')
else: 
    print(round((-b) / (a), 2))


# ## Задача H
# Для данного числа n < 100 закончите фразу “На лугу пасется...” одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

# In[69]:


n = int(input())
name = 'коров'

if n >= 11 and n <= 14:
    print(f'{n} {name}')
else:
    temp = n % 10
    if temp == 0 or (temp >= 5 and temp <= 9):
        print(f'{n} {name}')
    if temp == 1:
        print(f'{n} {name}а')
    if temp >=2 and temp <=4:
        print(f'{n} {name}ы')


# # Задача I. Диофантово уравнение

# Даны числа a, b, c, d. Выведите в порядке возрастания все целые числа от 0 до 1000, которые являются корнями уравнения $ax^3+bx^2+cx+d=0$.

# In[35]:





# ## Задача J
# Квадрат трехзначного числа оканчивается тремя цифрами, равными этому числу. Найдите и выведите все такие числа.

# In[20]:


for n in range(100, 1000):
    if (n ** 2) % 1000 == n:
        print(n)


# ## Задача K
# По данному натуральному $n \leq 9$ выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

# In[25]:


from time import time
 
 
tic = time()

n = int(input())

for i in range(n):
    for j in range(1, i+2):
        print(j, end='')
    print()
    
toc = time()
print() 
print(toc - tic)


# Реализация со строками:

# In[9]:


from time import time
 
 
tic = time()

n=int(input())
s=""
for i in range (n):
    s=s+str(n-n+i+1)
    print(s)
    
toc = time()
print() 
print(toc - tic)


# ## Задача L
# Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три числа a, b, c, затем программа должна менять их значения так, чтобы стали выполнены условия $a \leq b \leq c$, затем программа выводит тройку a, b, c.

# In[40]:


a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)


# ## Задача M
# Давным-давно билет на одну поездку в метро стоил 15 рубля, билет на 10 поездок стоил 125 рублей, билет на 60 поездок стоил 440 рублей. Пассажир планирует совершить n поездок. Определите, сколько билетов каждого вида он должен приобрести, чтобы суммарное количество оплаченных поездок было не меньше n, а общая стоимость приобретенных билетов — минимальна.

# In[24]:


n = int(input())
n1 = 15 
n10 = 125
n60 = 440

S1 = (n // 60)
S2 = ((n - S1*60) // 10)
S3 = n - S1*60 - S2*10 

S_itog = S1*440+S2*125+S3*10
print("число билетов на 60 поездок", S1)
print("число билетов на 10 поездок", S2)
print("число билетов на 1 поездку", S3)


# Попробуйте решить как задачу линейного программирования с помощью SciPy

# In[ ]:





# ## Задача N. Сумма факториалов
# По данному натуральном n вычислите сумму 1! + 2! + 3! + ... +n!. В решении этой задачи можно использовать только один цикл.

# In[59]:


import math
n = int(input())
res = 0
for i in range(1, n+1):
    res = res + int(math.factorial(i))
print(res)

