"""
Алгоритм вычисления значения функции F(n) задан следующими соотношениями:

F(n) = 1 при n = 0;
F(n) = 2 * F(1 - n) + 3 * F(n - 1) + 2 при n > 0;
F(n) = -F(-n) при n < 0.

Чему равна сумма цифр значения функции F(50)?

Формат вывода: программа должна печатать только одно число - ответ на задачу.
"""
import sys
from functools import cache

sys.setrecursionlimit(10000)


@cache
def f(n):
    if n == 0:
        return 1
    if n < 0:
        return -f(-n)
    return 2 * f(1 - n) + 3 * f(n - 1) + 2


a = str(f(50))
ans = 0
for el in a:
    ans += int(el)
print(ans)
