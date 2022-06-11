#imports
import telebot
import random
from telebot import types
from decouple import config

#API of bot
TOKEN = config('API_KEY')
bot = telebot.TeleBot(TOKEN)
print(f"{TOKEN} \n")
#puplic var
sudo = 1655098601
botName = ["kroli", "krol", "كرولي"]
admin_msg = {
  'ban': ["ban", "baned","kick", "حظر", "بان", "باند"]
}
usersMsg ={
    "hi" : ["hi", "hello", "hey", "hai"],
    "hi_ar" : ["هلا", "هلو", "هاي" ],
    "slam_ar" : ["سلام عليكم", "السلام عليكم", "سلام العليكم"],
    'botName' : ["bot", "بوت"]
}
botMsg ={
  "laveChat" : "sorry, but this chat im dosnt work in it. :(",
  'botNameReply' : ["هلا", "شو محتاج", "مو فارغ", "مشغول", "هلا بيك عيوني"],
  "ifMsgNotFromSudo" : "انت لست ادمن للقيام بالامر",
  'ifMessageNotReplyBan' : "يجب ان ترد على الشخص الي تريده يتبند"
}



# methdods
#
@bot.message_handler(commands=["start"])
def msg_hand(message):
    print("bot has reply of /start")


    Keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='↫main channel .',
                                         url='https://t.me/MYMFYK')
    button3 = types.InlineKeyboardButton(text=". OWNER↬",
                                         url='https://t.me/nnk0o')

    Keyboard.add(button1, button3)

    bot.send_message(
      message.chat.id,
                    text= "welcome to kroli \n ↫a group telegram bot↬",
                     reply_markup=Keyboard)

#...........


@bot.message_handler(func=lambda m: True)
def msg_handerl_main(message):
    msg = message.text.split()
    chat_id = message.chat.id
    #..................................
    #a ban method work if you send ban
    if message.text.lower() in admin_msg["ban"]:

        if message.from_user.id == sudo:
            if message.reply_to_message:
                text = message.reply_to_message.from_user.id
                text2 = message.reply_to_message.from_user.username
                try:
                    bot.kick_chat_member(
                  chat_id,
                  text
                )
                    bot.send_message(
                  chat_id,
                  text= "the user: {} Banned ∅ " .format(text2)
                )
                except:
                  bot.reply_to(
                    message,
                    "err" #will this message change...
                )  
#...........................

    if message.text.lower() in usersMsg["hi"] : 
        bot.reply_to(
            message,
            "Hello!"
        )
    if message.text.lower() in usersMsg["hi_ar"]     :
        bot.reply_to(
        
            message,
            
            "هلا ،كيفك"
            
            )   

#..........................................................................                        
            
    if message.text.lower() in usersMsg["botName"] :
      if message.text.lower() :
        list1 = ["هلا", "شو محتاج", "مو فارغ", "مشغول", "هلا بيك عيوني"]
        ran = random.choice(list1)
        bot.reply_to(
            message,
            f"{ran}"
        )
       
#.................................................
#message of if someone join or left your group
#@bot.my_chat_member_handler()
#def memberUpdate(message:types.#ChatMemberUpdated) :
#    newMember = message.new_chat_member
#    allowList = []
#    if new.status == 'member' and message.#chat.id not in allowlist :

@bot.my_chat_member_handler()   
def leavA(message:types.ChatMemberUpdated):
  update = message.new_chat_member
  if update.status == "member" :
    bot.send_message(
      message.chat.id,
    f"{botMsg['laveChat']}"
    )
    bot.leave_chat(message.chat.id)

        
        

#polling
def run():
  print("BOT IS RUNNING...")
  bot.infinity_polling()
run()
