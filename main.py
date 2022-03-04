import time
from icecream import ic
from selenium.webdriver.common.proxy import *
from selenium.webdriver.chrome.options import Options
from WebDriver import WebDriver
from ProxyGenerator import ProxyGenerator


pg = ProxyGenerator()
for i in range(1):
    addres = pg.get_random_addres()
    proxy = Proxy(
        {
            'proxyType': ProxyType.MANUAL,
            'httpProxy': addres,
            'sslProxy': addres,
            'noProxy': ''
        }
    )

    options = Options()
    options.proxy = proxy
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = WebDriver().get_driver()
    driver.get("http://diploma48.com")
    time.sleep(3)
    driver.get(pg.get_proxy_addres_info_url(addres))
    time.sleep(3)
