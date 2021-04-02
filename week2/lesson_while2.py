# Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее.
# Напишите функцию ask_user() которая с помощью функции input() просит пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
# программа давала ему соотвествующий ответ.


my_dict = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Сиги есть?": "Не курю"}

def ask_user():
    while True:
        question = input('Задайте вопрос: ')
        if question in my_dict:
            print(my_dict[question])
            break

ask_user()