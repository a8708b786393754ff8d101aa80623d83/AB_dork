import requests
import base64
from bs4 import BeautifulSoup


def get_proxy(method: str = 'https') -> dict:
    """Recupere les proxies est leur port

    Args:
        method (str, optional): methode http. Defaults to 'https'.

    Returns:
        dict: donnée des proxies
    """

    links = {'http': 'http://free-proxy.cz/fr/proxylist/country/all/http/ping/level1',
             'https': 'http://free-proxy.cz/fr/proxylist/country/all/https/ping/all/level1'}
    data = {'ip': [], 'port': []}
    if method in links:

        r = requests.get(links[method])
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find('tbody').find_all('tr')

        for tr in table:
            ip = tr.find('script')
            port = tr.find('span', class_='fport')
            if port:
                data['port'].append(port.text)

                base_64_encode = ip.text.split(
                    'document.write(Base64.decode("')
                ip_encode = base_64_encode[1].split('"))')[0]
                bs64_byte = bytes(ip_encode, encoding='utf-8')
                data['ip'].append(
                    str(base64.b64decode(bs64_byte), encoding='utf-8'))

    return data