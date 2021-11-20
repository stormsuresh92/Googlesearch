from requests_html import HTMLSession
import pandas as pd
from alive_progress import alive_bar
from time import sleep

s = HTMLSession()

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Connection':'keep-alive'
}


alldata = []
def page(x):
    url = f'https://www.google.com/search?q={query}&start={x}'
    r = s.get(url, headers=header)
    r.html.render(sleep=5, timeout=30)
    cont = r.html.find('.yuRUbf')
    with alive_bar(len(cont), title=f'Getting page {x}', bar='classic2', spinner='classic') as bar:
        for item in cont:
            try:
                title = item.find('h3', first=True).text
            except:
                title = ''
            try:
                link = item.find('a', first=True).attrs['href']
            except:
                link = ''
            dic = {
                'Title':title,
                'Urls':link
            }
            alldata.append(dic)
            sleep(0.1)
            bar()

          
query = input('Enter keyword here:')
endpage = int(input('Enter end page:'))
for x in range(0, endpage):
    page(x)
       
df = pd.DataFrame(alldata)
df.to_csv(f'{query}'+ '.csv', index=False)
print('\n')
print('Download completed')
input()
