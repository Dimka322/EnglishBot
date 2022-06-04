from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("learn_words", 'учить слова'),
        types.BotCommand("change_quantity", 'установить количество слов для изучения'),
        types.BotCommand("rus_test", "Пройти тестирование по изученным словам (Перевод - Слово)"),
        types.BotCommand("eng_test", "Пройти тестирование по изученным словам (Слово - Перевод)"),
        types.BotCommand("definition_test", "Пройти тестирование по изученным словам (Значение - Слово)"),
        types.BotCommand("all_word_test", 'Пройти тестирование по всем изученным словам'),
        types.BotCommand("show_rus_test_errors", 'Просмотреть слова, в которых были допущены ошибки (Перевод - Слово)'),
        types.BotCommand("show_eng_test_errors", 'Просмотреть слова, в которых были допущены ошибки (Слово - Перевод)'),
        types.BotCommand("show_def_test_errors",
                         'Просмотреть слова, в которых были допущены ошибки (Значение - Слово)'),
        types.BotCommand("show_sen_test_errors",
                         'Просмотреть слова, в которых были допущены ошибки (Вставить пропущенное)'),
        types.BotCommand("get_video", "Видео"),
    ])
