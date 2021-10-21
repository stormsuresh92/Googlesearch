from requests_html import HTMLSession
import datetime

s = HTMLSession()

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Connection':'keep-alive'
}


def page(x):
    url = f'https://www.google.com/search?q={query}&start={x}'
    r = s.get(url, headers=header)
    r.html.render(sleep=2, timeout=15)
    cont = r.html.find('.yuRUbf')
    for item in cont:
        try:
            title = item.find('h3', first=True).text
        except:
            title = ''
        try:
            link = item.find('a', first=True).attrs['href']
        except:
            link = ''
    output = open(f'{query}'+'.tsv', 'a')
    output.write(title + '\t' + link + '\n')
    output.close()
    
startime = datetime.datetime.now()           
query = input('Enter keyword here:')
endpage = int(input('Enter end page:'))
print('DATA EXTRACTING...') 
for x in range(10, endpage):
    page(x)
        
endtime = datetime.datetime.now()

print('Finished')
print(':::::::::::::::::')
print('TIME TAKEN TO TASK COMPLETE:', endtime-startime)
print(':::::::::::::::::')
