import pytelebot

# Creating the bot
bot = pytelebot ('5783797534:AAEilbLwla_AJECopw8oIBt1k6TdzrpXn8Y')

# The function processing "/start" command.
@bot.message_handler(commands=["start"])
def start (m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь')

# Message from user
@bot.message_handler(content_types=["text"])
def handle_text (message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

# Starting the bot/
bot.polling(none_stop=True, interval=0)