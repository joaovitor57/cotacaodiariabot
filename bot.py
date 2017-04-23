# encoding: utf-8

import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import unicodedata
import urllib2
import time
import re
from bs4 import BeautifulSoup

def handle(msg):
    chatid = msg['chat']['id']
    comando = msg['text'].encode('utf-8')
    
    page = urllib2.urlopen('http://www.dolarhoje.net.br/')
    soup = BeautifulSoup(page, "html5lib")
    dados = soup.find('div', {'id': 'box'})
    dolarc=dados.contents[6].encode('utf-8')
    dolart=dados.contents[10].encode('utf-8')
    euroc=dados.contents[18].encode('utf-8')
    eurot=dados.contents[22].encode('utf-8')

    pagina = urllib2.urlopen('http://dolarhoje.com/bitcoin/')
    texto = pagina.read().decode('utf-8')
    onde = texto.find('data-text="')
    inicio = onde + 27
    fim = inicio + 7
    bitcoin=texto[inicio:fim].encode('utf-8')

    keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Dólar Comercial"), KeyboardButton(text="Dólar Turismo")],
            [KeyboardButton(text="Euro Comercial"), KeyboardButton(text="Euro Turismo")],
            [KeyboardButton(text="Bitcoin"),  KeyboardButton(text="Ajuda")],
        ])

    if comando == '/start':
        bot.sendMessage(chatid, '''Bem Vindo!!
    Bot desenvolvido por @bergpb!
    /start - Iniciando o Bot
    Use os comandos do teclado abaixo:
    Dólar - Cotação atual do dólar
    Euro - Cotação atual do euro
    Bitcoin - Cotação atual do bitcoin''', reply_markup=keyboard)
        
    elif comando == 'Dólar Comercial':
        bot.sendMessage(chatid,'*Cotação atual do dólar em: *', parse_mode="Markdown")
        bot.sendMessage(chatid,'`%s`'%dolarc,parse_mode="Markdown")
    
    elif comando == 'Dólar Turismo':
        bot.sendMessage(chatid,'*Cotação atual do dólar em: *', parse_mode="Markdown")
        bot.sendMessage(chatid,'`$ %s`'%dolart,parse_mode="Markdown")
    
    elif comando == 'Euro Comercial':
        bot.sendMessage(chatid,'*Cotação atual do euro em:*',parse_mode="Markdown") 
        bot.sendMessage(chatid,'`$ %s`'%euroc,parse_mode="Markdown")
    
    elif comando == 'Euro Turismo':
        bot.sendMessage(chatid,'*Cotação atual do euro em: *',parse_mode="Markdown")
        bot.sendMessage(chatid,'`€ %s`'%eurot,parse_mode="Markdown")
    
    elif comando == 'Bitcoin':
        bot.sendMessage(chatid,'*Cotação atual do bitcoin em: *',parse_mode="Markdown")
        bot.sendMessage(chatid,'`R$ %s`'%bitcoin,parse_mode="Markdown")
    
    else:
        bot.sendMessage(chatid, '''Use os comandos no teclado para que possa ter acesso as opções do bot.''')

    
bot = telepot.Bot('')
bot.message_loop(handle)
              
print 'Aguardando comandos ...'

while 1:
    time.sleep(5)
