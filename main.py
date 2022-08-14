# Importing stuff 
import telebot
from dotenv import load_dotenv
import os
import requests

# Let's load env vars
load_dotenv()
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

# Let's define stuff
def get_waifuurl():
    contents = requests.get('https://api.waifu.pics/sfw/waifu').json()
    image_url = contents['url']
    return image_url

def get_nekourl():
    contents = requests.get('https://nekos.life/api/v2/img/neko').json()
    image_url = contents['url']
    return image_url

@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Hey there, I'm Tsuzumi 💖 
     I can send you anime waifu & neko images :)
     Send /help to check the commands out. '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['ping'])
def greet(message):
    msg = ''' PONG ⚡! I'm alive :3 '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['repo'])
def greet(message):
    msg = ''' Repository Link -> https://github.com/nisarga-developer/Tsuzumi '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['pong'])
def greet(message):
    msg = ''' (¬_¬ ) '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['cry'])
def greet(message):
    msg = ''' (┬┬﹏┬┬) '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['flip'])
def greet(message):
    msg = ''' (╯°□°）╯︵ ┻━┻ '''
    bot.send_message(message.chat.id, msg)    


@bot.message_handler(commands = ['help'])
def help(message):
    msg = ''' 
    Here are the commands, Senpai!

    /waifu - Get a random waifu image 
    /neko - Get a random neko image
    /ping - Check if the bot's up and working :)
    /help - Get a list of all the commands
    /repo - Get the GitHub repository link of the bot      
    /cry - Makes the bot cry
    /flip - Flip a table
    
    ¯\_(ツ)_/¯
       
    '''
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands = ['waifu'])
@bot.message_handler(regexp=r'waifu')
def waifu(message):
    url = get_waifuurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['neko'])
@bot.message_handler(regexp=r'neko')
def neko(message):
    url = get_nekourl()
    bot.send_photo(message.chat.id, url)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
