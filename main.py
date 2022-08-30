# импортируем библиотеку
import telebot
# подключаем токен полученный BotFather в телеграм
token = '5303619912:AAHYzyWPlNwyy9S9YJ6a0lZnV05QYUuW1Jk'
# переменная bot со значением telebot.TeleBot и аргументом (token)
bot = telebot.TeleBot(token)

# регестрируем функцию(которая ниже) в телеграме, как обработчик для каких либо сообщений
@bot.message_handler(content_types=["text"])

# создаём функцию обработчик echo с аргументом message
def echo(message):
# функция send_message и тип bot. эта функция принимает 2 параметра введенное сообщение  индетификатор телеграм message.chat.id и текст, который будет отправлен пользователю. обработка сообщения в котором прописывается ответ на сообщение.значение message.text можно поменять на любой текст и он будет выводится на любую команду
    bot.send_message(message.chat.id, message.text)

# функция, которая постоянно обращается к серверам телеграм (Лонгполинг)
bot.polling(none_stop=True)