REQUEST GET "https://api.mullvad.net/www/accounts/<key>/"
  HEADER "Host: api.mullvad.net" 
  HEADER "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0" 
  HEADER "Accept: application/json, text/plain, */*" 
  HEADER "Accept-Language: en-US,en;q=0.5" 
  HEADER "Accept-Encoding: gzip, deflate, br" 
  HEADER "Origin: https://mullvad.net" 
  HEADER "Connection: keep-alive" 
  HEADER "Referer: https://mullvad.net/en/account/" 



REQUEST POST "https://dashboard.blomp.com/authorize" 

  CONTENT "email=<USER>&password=<PASS>&rember=on&login=login" 

  CONTENTTYPE "application/x-www-form-urlencoded" 
  HEADER ": scheme: https" 
  HEADER "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" 
  HEADER "accept-encoding: gzip, deflate, br" 
  HEADER "accept-language: en-US,en;q=0.9" 
  HEADER "cache-control: max-age=0" 
  HEADER "content-length: 71" 
  HEADER "content-type: application/x-www-form-urlencoded" 
  HEADER "origin: https://dashboard.blomp.com" 
  HEADER "referer: https://dashboard.blomp.com/" 
  HEADER "sec-fetch-dest: document" 
  HEADER "sec-fetch-mode: navigate" 
  HEADER "sec-fetch-site: same-origin" 
  HEADER "sec-fetch-user: ?1" 
  HEADER "sec-gpc: 1" 
  HEADER "upgrade-insecure-requests: 1" 
  HEADER "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"