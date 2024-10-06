import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 
pokemons2 = []
@bot.message_handler(commands=['start'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        pokemons2.append(pokemon)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_message(message.chat.id, 'Фото твоего Покемона')
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, 'Крик твоего покемона!')
        bot.send_document(message.from_user.id, pokemon.send_sound())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username  in Pokemon.pokemons.keys():
         bot.send_message(message.chat.id, pokemons2[0].info()[0])
         bot.send_message(message.chat.id, 'Фото твоего Покемона')
         bot.send_photo(message.chat.id, pokemons2[0].info()[1])
         bot.send_message(message.chat.id, 'Крик твоего покемона!')
         bot.send_document(message.chat.id, pokemons2[0].info()[2])
      
    else:
        bot.reply_to(message, "Ты еще не создал своего покемона")

bot.infinity_polling(none_stop=True)

