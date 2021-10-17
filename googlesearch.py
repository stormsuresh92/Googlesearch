from requests_html import HTMLSession
import os
import datetime

s = HTMLSession()

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'CGIC=IocBdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45; SID=CAiUx1HynxNGafzHNXj-CvGyXfZ-T6UYNR2AHlXDHZTadMDQDbI8zUBpo6z5JGWLA0sYuA.; __Secure-1PSID=CAiUx1HynxNGafzHNXj-CvGyXfZ-T6UYNR2AHlXDHZTadMDQSgv4TbUuBqOUkER5osgHoQ.; __Secure-3PSID=CAiUx1HynxNGafzHNXj-CvGyXfZ-T6UYNR2AHlXDHZTadMDQxTuq2R6ec-dU8OA35xNYeg.; HSID=AV6rZRrKjFDAGXo8r; SSID=AGWuUUmUFv7CrhOGi; APISID=6T1Xyt2O_7CeoDYd/Ak_XZYyUDeshPykNE; SAPISID=5Lnb_o3km_vQTM8b/AYhtvfPxxXKwWpqWT; __Secure-1PAPISID=5Lnb_o3km_vQTM8b/AYhtvfPxxXKwWpqWT; __Secure-3PAPISID=5Lnb_o3km_vQTM8b/AYhtvfPxxXKwWpqWT; OGPC=19025836-3:; OGP=-19025836:-19025836:; 1P_JAR=2021-10-17-08; NID=511=KYEf8UofONL2ia1XFNne77zl58pkSCmxlf59Ce4ciRG1r5WF5DKeoyAxfQ8B6Eopl29ZjGZ-cDsrpZk47-68DHoShkRTiSh9yTF1wt-2sYYKT06zkFLTHeTg-NsefzXzEkgnbeNH9QjGXyYB5rtHSuWEZ6CU0tH6TbKUMNs5k58YaoBPeXPdQGOPhrPuTGMTrl0uumsaFKbvUIliiFRx2GjxTyK-y3y7vV8rH94VYFX1lckTJkDqeGj5bVV6Y5r7-DlF-jAsmVAXfheAhmNJQjeb7NrS0KCIPVzcSxjNU07qjPvWmYvmiCYSiYRweBRgQmCThpFtANpdmuSU72DZaRJGxUmpNdbcRh3ZCCKdcr_X2OTG6eWRVIAOvaLG8HqIje0U9Q-8HnW7; DV=07gLefXbJyEQ4NvUndzzyhlN79LUyBc; SIDCC=AJi4QfEP2-mgU3Cl2qcJoVd-qZB9X7ALWkNcxXT2jIQgsx9XAjucYToFtKnwYJLPrZ8nwe4-L7k; __Secure-3PSIDCC=AJi4QfGjAyXBDXkLyMjLBy00YqxQtT6zbytyrwipn2gGerLDdDS_VCjUbrU1NuN7BYIHfC3jUm8',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
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