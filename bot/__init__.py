import os, requests
from pyrogram import Client
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
#sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
prov = requests.get(os.environ.get("APRO_URL"))
a = prov.text.splitlines()
ap = len(a)
print("Total no of Authprized users"+str(ap))
if ap == 2:
   sudo_uss = a[0]+" "+a[1]
if ap == 5:
  sudo_uss = a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4]
if ap == 6:
  sudo_uss = a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4]+" "+a[5]
if ap == 7:
  sudo_uss = a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4]+" "+a[5]+" "+a[6]
if ap == 8:
  sudo_uss = a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4]+" "+a[5]+" "+a[6]+" "+a[7]
if ap == 9:
  sudo_uss = a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4]+" "+a[5]+" "+a[6]+" "+a[7]+" "+a[8]
if ap == 10:
  sudo_uss = a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4]+" "+a[5]+" "+a[6]+" "+a[7]+" "+a[8]+" "+a[9]
sudo_users = list(set(int(x) for x in sudo_uss.split()))
cc = os.environ.get("CUR_CHE")
app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
data = []
crf = []
watermark =[]

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
