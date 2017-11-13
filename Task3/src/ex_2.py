#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2
u = Unique(data1)
print(', '.join([str(i) for i in u]))

u = Unique(data2)
print(', '.join([str(i) for i in u]))

u = Unique(['a', 'A', 'b', 'B'])
print(', '.join([str(i) for i in u]))

u = Unique(['a', 'A', 'b', 'B'], ignore_case=True)
print(', '.join([str(i) for i in u]))

gen = gen_random(1, 3, 10)
print(', '.join([str(i) for i in gen]))
