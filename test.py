from unittest.mock import patch

try:
    import requests
except ImportError:
    raise AssertionError('Модуль requests не установлен. Посмотрите в README, что нужно для этого сделать.')

try:
    import telegram
    from telegram import Bot
    from telegram.ext import Updater
except ImportError:
    raise AssertionError('Модуль telegram не установлен. Посмотрите в README, что нужно для этого сделать.')


@patch.object(Bot, 'send_message')
@patch.object(Updater, 'start_polling')
@patch.object(Updater, 'idle')
def main(idle_mock, start_polling_mock, send_message_mock):
    try:
        import main

        try:
            assert isinstance(main.kitchen_chat_id, str), "Переменная kitchen_chat_id должна быть строкой."
        except AttributeError:
            raise AssertionError('Убедитесь, что id кухни назван, как kitchen_chat_id')


        try:
            assert isinstance(main.updater, Updater), "Переменная updater должна быть класса Updater."
        except AttributeError:
            raise AssertionError('Убедитесь, что экземпляр класса Updater называется, как updater')


        try:
            assert isinstance(main.menu_url, str), "Переменная menu_url должна быть строкой."
        except AttributeError:
            raise AssertionError('Убедитесь, что URL меню назван, как menu_url')
        
        try:
            start_polling_mock.assert_called_once()
        except AssertionError:
            raise AssertionError('Убедитесь, что вы вызвали метод start_polling у updater.')
        
        try:
            idle_mock.assert_called_once()
        except AssertionError:
            raise AssertionError('Убедитесь, что вы вызвали метод idle у updater.')
    except telegram.error.InvalidToken:
        raise AssertionError('Убедитесь, что токен для класса Updater передан валидный.')


if __name__ == '__main__':
    main()
    print('Все тесты прошли успешно.')