# Разместите здесь импорты

kitchen_chat_id = ...
menu_url = ...


updater = ...


def get_menu():
    ...


def show_menu(update, context):
    ...


def process_order(update, context):
    ...


def wake_up(update, context):
    ...


# Здесь добавьте обработчиков:
# * для команды 'start' — чтобы вызывалась функция wake_up
# * для команды 'menu' — чтобы вызывалась функция show_menu
# * для произвольного текста — чтобы вызывалась функция process_order

# Запустите polling