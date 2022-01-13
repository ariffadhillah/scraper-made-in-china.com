from cgitb import html
from operator import le
import requests
from bs4 import BeautifulSoup

# baseurl = 'https:'

def login():
    print ('login...')

    cookies = {
    'pid': 'TgyLjMuNy4yNDYyMDIyMDEwMzAxNDUwOTAyNjQyNDMzNzg4M',
    'webp': 't',
    '__pd': '1foduabo5b11',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22BKftQySzHMGL_00%22%2C%22first_id%22%3A%2217e1be5310722-065018dc8860bd-7d20675d-1024000-17e1be531083e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217e1be5310722-065018dc8860bd-7d20675d-1024000-17e1be531083e%22%7D',
    '_ga_VEFCZRQMG4': 'GS1.1.1642094454.6.0.1642094467.47',
    '_ga': 'GA1.2.299548638.1641145513',
    '_fbp': 'fb.1.1641145515691.2004972831',
    'lg_name': 'ariffadhillah33%40gmail.com',
    'lg': 'SPoguQp2S3nMUdGe/d8Y4Q==~@~kt2t60qo+F5to8HVORruXg==~@~F3b1Jij1uaJQMLPGzmuXg2dS9mQLS1tH~@~F3b1Jij1uaKgNGPJpvMjTXWYSIDCf1WdGz8SWarPPoo=~@~+VDYBf+8FIvH9Gztu3sFNw==~@~',
    'cto_bundle': 'S4rwvl9FcUlpV2Rad24wZCUyRmxab0FQQU5XczNZMFZtYXRNbkdjUzc1TzZ3RnpLZ0ZmRkZIZXVhWVk2UjBSbHBPVmx5eFN2TEdLZHJ4SHphWlN3OGltVUJYR1RRSDRKQ1hjdlJKdWtyZmlqVnR5MEVMRmhzcVl3aEZXOXRheU0wVkxlSnZSeVNhQng0dCUyQjN1YWhHNXFXRnNVQ2F3JTNEJTNE',
    'sf_img': 'AM',
    '_uat': 'Tc2MTcwMzc4MQM.VAxWEIxNDExMDYwMDAwV%7EVAxWEM5Mjg4NTMyMjUV%7EVAxWEIxNDExMDYwMDAwV%7EVAxTUs2MTY1OTkyNjQV%7EVAxWEIxNDExMDYwMDAwV%7EVAxWEs2MTUzNjY0NDQV%7EVAxTUM3MjQyMDI1MDIV%7EVAxWEIxOTAyMDMwMDAwV%7EVAxWEIxNDExMDYwMDAwV.9.20220113195857',
    '_gid': 'GA1.2.1196471754.1642036435',
    '_clck': 'bd3puj|1|ey3|0',
    '_clsk': '1k5lx6y|1642094461580|1|0|b.clarity.ms/collect',
    '_kwd': 'HJvZF9+RmVlZCBQcm9jZXNzaW5nIE1hY2hpbmVyeQciEsfHJvZF9+bWFudWZhY3R1cmluZyAmIHByb2Nlc3NpbmcgbWFjaGluZXJ5c',
    '_psl': 'yJmYyI6WyIxOSJdfQe',
    '_cat': 'ERffjE5MDIwMzAwMDAU',
    '_cwd': 'cKiJmnpljUYR',
    '_skwd': '29tX35QZWxsZXQgUHJlc3N+ISxjb21fflBlbGxldAY',
    '_pd': 'TI4ODUzMjI1OiEsfzI0MjAyNTAyN',
    'JSESSIONID': '8BEA9A65DEC7C572E5EB3C01444B7BF5',
    'se': 'TgyLjMuNi4xMTUyMDIyMDExNDAxMjA0MTY2MjQ3NTYwMjI5M',
    'lang': 'en',
    'dpr': '1',
    'cid': 'jAyMjAxMTQwMTIxMTQxNTAwMDA6MTkyNjA4MjA2NDE5MjQ1MTE5NDIM',
    'sid': 'DkyMDcxMzIyODQ2MTQzMTM6MTgyLjMuNi4xMTU6MTc2MTcwMzc4MTowMAN',
    '_uetsid': '13dd2670740e11ec89adefde055638ef',
    '_uetvid': 'bd118da06bf311ecbb7701cbd715a34b',
    '_gat_UA-37452587-1': '1',
    'LOGT': 'pmZOngNcahOCY6subwyJWB/mxDrBMGY0',
    'CPID': 'NJgOhQ0h6pCxHU213GNnuwOM+XImv8as',
    'LVT': 'NJgOhQ0h6pCo5SALH6kQFfrqeLpeyFmQ',
    'loginSource': '1',
    'cbid': 'Tc2MTcwMzc4MTowMAM',
    'wel_name': 'XJpZgQ',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://login.made-in-china.com/',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }

    productlink = []
    
    for x in range(1,6):
        res = requests.get(f'https://www.made-in-china.com/manufacturers-directory/item3/Earphone-Case-{x}.html', headers=headers, cookies=cookies)
            
        soup = BeautifulSoup(res.content, 'lxml')

        productlist = soup.find_all('h2', class_='company-name')

        
        for item in productlist:
            for link in item.find_all('a', href=True):
                # productlink.append(baseurl + link['href'])
                print(link['href'])
        print(len(productlist))
                
    print(len(productlink))
        
        # f = open('./res.html', 'w+')
        # f.write(res.text)
        # f.close()

        


def get_url():
    print ('get_url...')

def get_details():
    print ('get_details...')


def create_csv():
    print ('create_csv...')

def run():
    login()
    get_url()
    get_details()

if __name__ == '__main__':
    run()






