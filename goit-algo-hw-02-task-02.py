from collections import deque

def is_palindrome(string):
    # Перетворюємо рядок у нижній регістр та видаляємо пробіли
    string = string.lower().replace(" ", "")
    
    # Створюємо двосторонню чергу та додаємо всі символи рядка до неї
    char_queue = deque(string)
    
    # Порівнюємо символи з обох кінців черги, доки черга не стане порожньою або не залишиться один символ
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

# Список рядків для перевірки
strings_to_check = [
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "level",
    "algorithm",
    "python",
    "programming",
    "madam",
    "noon"
]

# Перебір кожного рядка у списку
for input_string in strings_to_check:
    # Виклик функції is_palindrome() для кожного рядка
    print(f"Is '{input_string}' a palindrome? - {is_palindrome(input_string)}")
