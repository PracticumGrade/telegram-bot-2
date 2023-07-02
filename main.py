# Разместите здесь импорты
# Вам понадбится импортировать requests,
# ReplyKeyboardMarkup, CommandHandler, Updater,
# MessageHandler и Filters.
# Посмотрите в уроках, как они импортируются.

# Это id чата кухни. Для теста укажите свой.
# Узнать его можно при помощи @userinfobot
kitchen_chat_id = ...
# Эта переменная должна быть экземпляром класса Updater.
# Здесь же укажите токен своего бота
updater = ...
# Здесь укажите URL до меню. Посмотрите его в тексте задания.
menu_url = ...


def get_menu():
    """Получить меню из внешнего источника и вернуть его в читаемом виде"""
    # С помощью requests.get(...) получите меню.
    # Его URL вы указали выше. 
    response = ...
    # Превратите response в json
    response_json = ...
    # names — пустой список, проинициализируйте его
    names = ...
    # С помощью цикла for наполните names названиями позиций
    # Откройте menu_url в браузере, посмотрите, как выглядит json
    # и как из него достать имена.
    menu_prefix = 'Сегодня в меню: '
    # Соедините имена в одну строку через запятую.
    # Помните про метод ".join"?
    menu_names = ...
    menu = menu_prefix + menu_names
    return menu


def show_menu(update, context):
    # Получите chat_id из update.effective_chat
    chat_id = ...
    # В message поместите результат вызова функции get_menu
    message = ...
    context.bot.send_message(chat_id, message)


def process_order(update, context):
    # Получите effective_chat из update
    chat = ...
    # Получите сообщение клиента из update.message.text
    client_message = ...
    # Проверьте, что сообщение клиента начинается с «Закажи»
    if ...:
        order_message_prefix = 'Новый заказ: '
        # Отправьте сообщение на kitchen_chat_id
        context.bot.send_message(
            chat_id=...,
            text=order_message_prefix + update.message.text,
        )
        # Отправьте клиенту сообщение 
        # 'Передали сообщение на кухню, приходите завтра за заказом в любое время!'
        context.bot.send_message(
            chat_id=...,
            text=...
        )
    else:
        # Отправьте клиенту сообщение 
        # 'Начните сообщение с «Закажи», чтобы передать заказ на кухню.'
        context.bot.send_message(
            chat_id=...,
            text=...
        )


def wake_up(update, context):
    # Получите effective_chat из update
    chat = ...
    # Получите first_name из update.message.chat
    name = ...
    # Создайте ReplyKeyboardMarkup с командой /menu.
    # Подсмотрите в уроке, как это сделать
    button = ...

    # Отправьте сообщение "Добро пожаловать, {имя}"
    # С кнопкой menu
    context.bot.send_message(
        chat_id=...,
        text=...,
        reply_markup=...
    )
    # Отправьте меню
    context.bot.send_message(
        chat_id=...,
        text=...
    )
    # Отправьте текст
    # 'Начните сообщение с «Закажи», чтобы передать заказ на кухню.'
    context.bot.send_message(
        chat_id=...,
        text=...
    )


# Добавьте обработчики команд 'start' и 'menu', а также обработчик текстовых сообщений.
# На 'start' вызывайте wake_up
updater.dispatcher.add_handler(...)
# На 'menu' — show_menu
updater.dispatcher.add_handler(...)
# У обработчика сообщений — MessageHandler — должен быть фильтр Filters.text
# и в ответ он должен вызывать process_order 
updater.dispatcher.add_handler(...)

# Стартуйте polling
# Вызовите для этого на объекте updater 
# методы start_polling и idle.
