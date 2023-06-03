import telebot

bot = telebot.TeleBot('6184574078:AAFXfr_ZdezisfBuBGKPpbVKCMJD8ZcrrYM')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(commands=['hello'])
def hello(message):
    text = 'Привіт, як твої справи?'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['python'])
def python(message):
    text = 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability ' \
           'with the use of significant indentation via the off-side rule.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['pip_info'])
def pip_info(message):
    text = 'Менеджер пакунків Python. Команда pip install використовується для встановлення будь-якого програмного пакета ' \
           'з онлайн-репозиторію загальнодоступних пакетів або Індексу пакетів Python (PyPI, Python Package Index).'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['print_info'])
def print_info(message):
    text = 'Команда для друку повідомлень на екрані або на іншому стандартному пристрої виведення.' \
           'Команда print може використовуватися для друку будь-якого типу об`єкта - цілого числа, рядки, списку, кортежу та інших.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['class_info'])
def class_info(message):
    text = 'Команда створення класів. Python підтримує об`єктно-орієнтоване програмування та дозволяє користувачам ' \
           'створювати класи та ініціалізувати об`єкти. Клас може складатися з змінних з модифікаторами доступу, ' \
           'функцій з типами, що повертаються, і навіть інших класів (вкладений клас).'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['type_info'])
def type_info(message):
    text = 'Команда для перевірки типу чи класу об`єкта.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['range_info'])
def range_info(message):
    text = 'Команда для генерації послідовності цілих чисел, починаючи з 0 за замовчуванням і закінчуючи n ' \
           'де n не включено в згенеровані числа. Ця команда переважно використовується в циклах for.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['round_info'])
def round_info(message):
    text = 'Команда заокруглення числа до заданої точності в десяткових розрядах. ' \
           'Дозволяє скоротити кількість цифр після коми у числі плаваючої коми до вказаного значення.' \
           'round(number, digits) ' \
           'number — число з плаваючою комою; ' \
           'digits — кількість цифр після десяткової точки (опційно; за замовчуванням – 0).'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['input_info'])
def input_info(message):
    text = 'Команда для отримання введення користувача. Виконання програми буде зупинено доти, доки користувач ' \
           'не введе будь-яке значення, яке буде перетворено функцією input() у рядок. ' \
           'Якщо як вхідні дані потрібно взяти ціле число, його потрібно перетворити явно.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['def_info'])
def def_info(message):
    text = 'Команда визначення функції Python дає можливість обертати повторно використовуваний код усередині функцій, ' \
           'щоб викликати його пізніше, коли це необхідно. Функція def дозволяє мінімізувати надмірність коду.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['len_info'])
def len_info(message):
    text = "Команда len або функція len() використовуються для розрахунку кількості елементів в об'єкті. " \
           "Якщо об'єкт є рядком, то функція len() повертає кількість присутніх символів. Якщо об'єкт є список або кортеж, " \
           "він поверне кількість елементів, присутніх у цьому списку або кортежі. " \
           "При спробі передати len() ціле значення, функція видає помилку."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['isalnum_info'])
def isalnum_info(message):
    text = "Команда isalnum() перевіряє, чи всі символи цього рядка є буквенно-цифровими чи ні. Він повертає логічне значення."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['capitalize_info'])
def capitalize_info(message):
    text = "Строкова функція capitalize() повертає рядок, змінюючи перший символ на верхній регістр, а інші переводячи в нижній. " \
           "Якщо перший символ вже у верхньому регістрі, а також є цілим числом або будь-яким спеціальним символом, " \
           "команда нічого не робить."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['find_info'])
def find_info(message):
    text = "Команда find() використовується для пошуку підрядка у рядку. Якщо така знайдена, find() повертає індекс першого " \
           "входження підрядка, інакше повертає -1."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['count_info'])
def count_info(message):
    text = "Рядкова функція count() повертає кількість входжень підрядка в рядковий об'єкт." \
           "У кортежі метод count() використовується для підрахунку входжень елемента в кортеж."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['center_info'])
def center_info(message):
    text = "Команда center() використовується для вирівнювання рядка по центру із заповненням вказаним символом."
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['append_info'])
def append_info(message):
    text = "Команда списку append() використовується для додавання елемента до кінця списку."
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['copy_info'])
def copy_info(message):
    text = "Команда copy() створює нову копію списку об'єкта. Вона повертає новий об'єкт списку."
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['insert_info'])
def insert_info(message):
    text = "Команда insert() додає елемент до зазначеного місця в об'єкті списку."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['pop_info'])
def pop_info(message):
    text = "Метод pop() використовується для видалення елемента із зазначеної позиції у списку. " \
           "Він повертає елемент після видалення його зі списку."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['reverse_info'])
def reverse_info(message):
    text = "Метод reverse() змінює порядок всіх елементів списку. Команда змінює вихідний об'єкт списку та нічого не повертає."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['sort_info'])
def sort_info(message):
    text = "Метод sort() за промовчанням використовується для сортування елементів списку в порядку зростання."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['index_info'])
def index_info(message):
    text = "Метод index() використовується для пошуку індексу першого входження елемента. " \
           "Якщо елемент не знайдений у всьому кортежі, буде виведено помилку ValueError."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['add_info'])
def add_info(message):
    text = "Команда add() дозволяє додати новий елемент у множину."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['clear_info'])
def clear_info(message):
    text = "Функція clear() видаляє всі елементи set. Вона не приймає жодних параметрів."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['discard_info'])
def discard_info(message):
    text = "Команда discard() дозволяє видалити вказаний елемент із набору. " \
           "Якщо елемент не знайдено в наборі, він не видасть помилку."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['remove_info'])
def remove_info(message):
    text = "Команда remove() також використовується для видалення зазначеного елемента з множини. " \
           "Від команди discard() вона відрізняється повідомленням про помилку, яке виводиться, якщо зазначений елемент не знайдено."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['difference_info'])
def difference_info(message):
    text = "Метод difference() використовується для отримання множини, що містить різницю двох множин. " \
           "У ньому будуть лише ті елементи, які присутні лише в одній множині та відсутні в іншій. " \
           "Наприклад, difference() для множин setA {1,2,3} і setB {2, 4, 6} буде {1,3}."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['difference_update_info'])
def difference_update_info(message):
    text = "Метод difference_update() дозволяє отримати набір елементів, які є в першій множині і не є спільними для обох. " \
           "Це означає, що difference_update() видаляє елементи, що існують в обох множинах. " \
           "Він не повертає новий set, а просто видаляє загальні елементи з першої множини."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['intersection_info'])
def intersection_info(message):
    text = "Метод intersection() відображає множину, що містить елементи, які існують у всіх зазначених множинах."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['issubset_info'])
def issubset_info(message):
    text = "Метод issubset() перевіряє, чи всі елементи множини setA присутні в setB. Команда повертає логічне значення."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['symmetric_difference_info'])
def symmetric_difference_info(message):
    text = "Метод symmetric_difference() повертає симетричну різницю двох множин, що містить всі елементи, за винятком загальних."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['union_info'])
def union_info(message):
    text = "Метод union() повертає всі елементи з обох множин, крім повторюваних."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['if_elif_else'])
def if_elif_else(message):
    text = "Ці оператори Python, які також називають операторами розгалуження або операторами умовного керування, " \
           "дозволяють змінювати хід виконання програми в залежності від умов."
    bot.send_message(message.chat.id, text)

import datetime
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    date_now = datetime.datetime.now()
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'і тобі привіт')
    elif message.text == 'python':
        bot.send_message(message.chat.id, 'о, ти вивчаєшь пайтон? круто')

    elif message.text == 'поточний день':
        bot.send_message(message.chat.id,  f'today is  {date_now.strftime("%d.%m.%Y")}')
    elif message.text == 'день тижня':
        bot.send_message(message.chat.id, f'today is {date_now.strftime(" %A")}')
    elif message.text == 'поточний час':
        bot.send_message(message.chat.id,  f'now {date_now.strftime("%H:%M:%S")}')
    elif message.text == 'номер тижня':
        bot.send_message(message.chat.id,  f'now is the  {date_now.strftime("%W")}th week of the year')

    elif message.text == 'python logo':
        photo = open('Python-logo-notext.svg.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'datetime documentation':
        doc = open('documentation.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'math':
        doc = open('math_documentation.html', 'r', encoding='utf-8')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'random':
        doc = open('random.documentation.html', 'r', encoding='utf-8')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'calendar':
        doc = open('calendar.documentation.html', 'r', encoding='utf-8')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'os':
        doc = open('os.documentation.html', 'r', encoding='utf-8')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'collections':
        doc = open('collections.documentation.html', 'r', encoding='utf-8')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'csv':
        doc = open('csv.documentation.html', 'r', encoding='utf-8')
        bot.send_document(message.chat.id, doc)

    else:
        bot.send_message(message.chat.id, 'я тебе не розумію')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'класне фото')


bot.polling(none_stop=True)
















