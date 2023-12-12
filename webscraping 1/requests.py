from urllib import request
from urllib.request import Request, urlopen
 
url = "https://parkslivestock.com/"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()
print(webpage)