from queue import Queue
import time

# Створити чергу заявок
queue = Queue()

# Функція generate_request():
def generate_request():
    # Створити нову заявку
    new_request = "New request"
    # Додати заявку до черги
    queue.put(new_request)
    print("New request added to the queue")

# Функція process_request():
def process_request():
    # Якщо черга не пуста:
    if not queue.empty():
        # Видалити заявку з черги
        request = queue.get()
        # Обробити заявку (мімітуємо обробку, просто виводимо)
        print("Processing request:", request)
    else:
        # Інакше, якщо черга пуста:
        print("Queue is empty")

# Головний цикл програми:
def main():
    # Поки користувач не вийде з програми:
    while True:
        # Виконати generate_request() для створення нових заявок
        generate_request()
        # Виконати process_request() для обробки заявок
        process_request()
        # Затримка перед генерацією наступної заявки
        time.sleep(1)

if __name__ == "__main__":
    main()
