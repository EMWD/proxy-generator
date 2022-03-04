import re
import requests
import random
from icecream import ic


class ProxyGenerator():
    addresses_ = []

    def clean_proxy_list(self, adresses: dict) -> list:
        for addres in adresses:
            addres = addres.get('full_ip')
            if addres.count('.') == 3 and addres.count(':') == 1:
                self.addresses_.append(addres)

    def get_from_freeproxy(self) -> list:
        url = 'https://free-proxy-list.net/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.97 Mobile/15E148 Safari/604.1'
        }
        source = str(requests.get(url, headers=headers, timeout=10).text)
        data = [
            list(filter(None, i))[0] for i in re.findall(
                '<td class="hm">(.*?)</td>|<td>(.*?)</td>',
                source
            )
        ]
        pack = [
            dict(zip(['ip', 'port', 'code', 'using_anonymous'], data[i:i+4]))
            for i in range(0, len(data), 4)
        ]
        addresses = [{'full_ip': "{ip}:{port}".format(**i)} for i in pack]
        self.clean_proxy_list(addresses)
        return [addres for addres in self.addresses_]

    def get_random_addres(self) -> str:
        return self.get_from_freeproxy()[random.randint(0, 299)]

    def get_proxy_addres_info_url(self, addres: str) -> str:
        if addres.count(':'):
            addres = addres.split(':')[0]
        return f'https://awebanalysis.com/en/ip-lookup/{addres}/'
