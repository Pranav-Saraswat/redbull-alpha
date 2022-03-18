from pyrogram import filters
from bot import app, data, sudo_users, cc
from bot.helper.utils import add_task
from pyrogram import types
from bot import (
    data,
    crf,
    watermark
)
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import os
if cc == "z5":
  che = "Zee 5"
if cc == "ma":
  che = "Mail Acess"
@app.on_message(filters.incoming & filters.command(['start', 'help']))
def help_message(app, message):
    message.reply_text(f"Hey {message.from_user.mention()} 💙.", quote=True)

@app.on_message(filters.user(sudo_users) & filters.incoming & (filters.document))
def encode_video(app, message):
    if message.document:
     message.reply_text("Added To Queue⏲️\n Please Be Patient", quote=True) 
    data.append(message)
    if len(data) == 1:
      add_task(message)
@app.on_message(filters.user(sudo_users))
def sudo(app, message):
    if message.text == "/boob":
      message.reply_text(f"•••••HELP••••• \n Ω Send any file to check it \n Ω Toggle coming soon\n Ω Current Module " + che)
    elif message.text == "/fcrm":
      os.system("python3 floodcrm.py")
    elif message.text == "/eag":
      os.system("python3 eag.py")
    elif "/udemyset" in message.text:
      os.system("rm acc.txt")
      upsa = message.text.split(' ')
      line = upsa[1].strip()
      try:
       combo=line.split(':')
       eml=combo[0].strip()
       pwd=combo[1].strip()
      except:
        message.reply_text("Something went wrong\n Maybe wrong format")
      try:
       apiss = open('acc.txt','r')
       apis = apiss.readlines()
      except:
       apiss = open('acc.txt','w')
       apiss.close()
       apiss = open('acc.txt','r')
      apiss = open('acc.txt', 'w')
      apiss.write(eml+"|"+pwd)
      apiss = apiss.close()
      message.reply_text("Creds added !")
    elif message.text == "/udemy":
      message.reply_text(f"•••Initating Udemy Module•••")
      message.reply_text("🖤")
      os.system("python3 udemy.py")
      message.edit("💚")
      message.reply_text(f"Enrollment done")
    elif message.text == "/mubi":
      os.system("python3 mubi.py")
    else:
        message.reply_text("hehe wrong cmd")
app.run()
