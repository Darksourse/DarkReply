# Модуль для Hikka
# Позволяет использовать команды .reply и .answer

class ReplyAnswerModule:
    def __init__(self):
        self.replies = {}  # Словарь для хранения заданных текстов

    def handle_message(self, message):
        # Обработка входящего сообщения
        if message.startswith(".reply "):
            # Извлекаем текст после команды .reply
            _, reply_text = message.split(" ", 1)
            # Сохраняем текст в словаре
            self.replies[message.chat_id] = reply_text
            return "Текст успешно задан для ответа!"
        elif message == ".answer":
            # Отправляем сохраненный текст
            if message.chat_id in self.replies:
                return self.replies[message.chat_id]
            else:
                return "Текст для ответа не задан."
        else:
            return None  # Не обрабатываем другие сообщения

# Создаем экземпляр модуля
reply_answer_module = ReplyAnswerModule()

# Регистрируем его в Hikka
hikka.register_module(reply_answer_module)
