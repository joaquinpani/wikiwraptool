import requests
from bs4 import BeautifulSoup

mainurl = "https://es.wikipedia.org"

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

respuesta = requests.get(mainurl,headers=headers)

print(respuesta)