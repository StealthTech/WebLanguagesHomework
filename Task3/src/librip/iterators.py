# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.ignore_case = kwargs.get('ignore_case', False)

        if self.ignore_case:
            self.items = list(set([i.casefold() for i in items]))
        else:
            self.items = list(set(items))

        self.__index = 0
        self.__max = len(self.items)

    def __next__(self):
        # Нужно реализовать __next__
        if self.__index >= self.__max:
            raise StopIteration

        result = self.items[self.__index]
        self.__index += 1
        return result

    def __iter__(self):
        return self
