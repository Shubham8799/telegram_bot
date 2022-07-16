import telegram
from telegram import ChatAction, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,CallbackQueryHandler,PicklePersistence
from telegram.ext.dispatcher import run_async
from telegram_bot_pagination import InlineKeyboardPaginator
import logging
import os
import requests
from tpblite import TPB
t = TPB()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

@run_async
def start(update,context):
	name=update.message.chat.first_name
	update.message.reply_text("Hi! "+name+"\nWelcome to google interview Bot 😃,\n using this help you to crack googler interview get started")

print("hello🙋‍♂️ my future Googler") 
print("hello I am a Google interview bot") 
print("so, my future Googler") 
name = input("what is your name : ") 
print (" Nice 😊 to meet you : " + name ) 
print(" So, : " + name ) 
print(" Basically I'll take your interview😉 ") 
print(" Are you excited") 
print(" And I also provide you google interview questions for your googler preparation ") 
print (" Than you can crack Google interview ") 
print(" So, let's start ") 
introducing = input(" Introduce your self ") 
print (" Ok nice. ") 
print (" Come to the next question ") 
favorite = input ("What is your favorite Google product, and how would you improve it?") 
print (" Ok ") 
goals = input ("Tell me about a time when you set and achieved a goal?") 
print (" Ohh good ") 
question= input ("Could manhole covers be any shape other than round, like a rectangle?") 
print (" Hmmm") 
algorithm= input ("Explain the algorithm for finding the power set of a given set.") 
print ("such a nice answer") 
print ("ok ") 
print (" A basic question ") 
ceo = input("who is the ceo of google?.") 
print= (" One more too basic question ") 
googlefounder= input (" Who is founder of Google ") 
#('ok the last question') 
about = input ("How would you explain programming and programming languages to a 10-year old?") 
#Ok  
#This interview is complete 
input("We will give you answer after checking .type ok to confirm : ") 
input("Have a nice day")
