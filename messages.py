import requests
from time import sleep
from bs4 import BeautifulSoup
from scrolling_text import display, clear_display
from servo import move

display('Running', 0)
url = 'https://gist.githubusercontent.com/greatmoves/4692d8f5cc668f47d2fc60a304c527ce/'
oldhash = ''
while 1:
    html = requests.get(url).text
    raw = BeautifulSoup(html, 'html.parser')
    button = raw.find('div', class_= "file-actions flex-order-2 pt-0")
    hash = button.contents[1].attrs['href']
    if(hash == oldhash):
        sleep(5)
        print('No changes')
        continue
    oldhash = hash
    text = requests.get('https://gist.githubusercontent.com' + hash).text
    display(text,0)
    move()
    sleep(60)
