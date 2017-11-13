#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'},
]

# Реализация задания 1
gen = field(goods, 'title')
for i in range(4):
    print(i + 1, next(gen))

gen = field(goods, 'title', 'no_match')
for i in range(4):
    print(i + 1, next(gen))

gen = field(goods, 'title', 'price')
for i in range(4):
    print(i + 1, next(gen))

gen = field(goods, 'price')
for i in range(4):
    print(i + 1, next(gen))
