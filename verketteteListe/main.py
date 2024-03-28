import os
import random
from pathlib import Path
from dotenv import load_dotenv


def load_env_variables():
    dotenv_path = Path(
        'C:/Users/Jonat/OneDrive/Desktop/Schule/5Klasse/SWP/Rubner/5BHWII_SWP-R_Gendu_Jonathan/SchereSteinPapierEchseSpock/_.env')
    load_dotenv(dotenv_path)
    print(os.getenv('id'))


def adder(*args):
    return sum(args)


def adder2(**kwargs):
    return sum(kwargs.values())


def my_generator():
    n = 1
    while True:
        yield n
        n += 1


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def len_iterative(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


def main():
    load_env_variables()

    print(adder(1, 2, 3, 4, 5))
    print(adder2(a=1, b=2, c=3, d=4, e=5))

    gen = my_generator()
    print(next(gen), next(gen), next(gen))

    say_hello("World")

    ll = LinkedList()
    for i in range(1, 11):
        ll.append(random.randint(1, 100))
    ll.print_list()
    print("Length of linked list:", ll.len_iterative())

    for data in ll:
        print(data)

    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Caught division by zero error")


if __name__ == "__main__":
    main()
