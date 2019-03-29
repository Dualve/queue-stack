"""Стек - абстрактный тип данных.
Представляет собой список элементов, организованных
по принципу последним пришел - первым вышел.
То есть доступ есть к последним символам"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """Проверка на пустой список"""
        return self.items == []

    def push(self, item):
        """Добавление элемента в стэк"""
        self.items.insert(0,item)

    def pop(self):
        """Удаление элемента из стэка"""
        return self.items.pop(0)

    def peek(self):
        """Возвращает элемент стэка"""
        return self.items[0]

    def size(self):
        """Возваращает длину стэка"""
        return len(self.items)


stack = Stack()
stack.push(input())
stack.push(input())
print(stack.pop())
print(stack.peek())
stack.pop()
if stack.isEmpty():
    print("FIREfireFIRE")
