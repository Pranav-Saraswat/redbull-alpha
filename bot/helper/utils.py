import os
from bot import data, download_dir, cc
from pyrogram.types import Message
#from .ffmpeg_utils import encode, get_thumbnail, get_duration, get_width_height

def on_task_complete():
    del data[0]
    if len(data) > 0:
      add_task(data[0])
def add_task(message: Message):
    try:
      msg = message.reply_text("❤️", quote=True)
      filepath = message.download(file_name=download_dir)
      msg.edit("💛")
      if cc == "z5":
        msg.edit("🤍")
        os.system("echo "+ filepath +" python3 zee5.py")
      if cc == "ma":
        msg.edit("🖤")
        os.system("echo '"+ filepath +"' | python3 mail.py")
      msg.edit("💚")
#      new_file = encode(filepath)
#      if new_file:
#        msg.edit("Video Encoded Successfully\nGetting Metadata 🐭")
#        duration = get_duration(new_file)
#        thumb = get_thumbnail(new_file, download_dir, duration / 4)
#        width, height = get_width_height(new_file)
#        msg.edit("Uploading 🐭")
#        message.reply_video(new_file, quote=True, supports_streaming=True, thumb=thumb, duration=duration, width=width, height=height)
#        os.remove(new_file)
#        os.remove(thumb)
#        msg.edit("Video Successfully Encoded to x265 🐭")
#      else:
#        msg.edit("Something Went Wrong While Encoding :(\nTry Again Later 🐭")
#        os.remove(filepath)
    except Exception as e:
      msg.edit(f"```{e}```")
    on_task_complete()
