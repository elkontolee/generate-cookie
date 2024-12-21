import os
import requests
import sys

from bs4 import BeautifulSoup as Bs4

url = 'https://n.facebook.com'
xurl = url + '/login.php'

UserAgent = ("Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/59.0.3071.125 Mobile Safari/537.36")


def login():
    try:
        user = input('[✦] Username/Email/Number: ')
        pswd = input('[✦] Password: ')
        req = requests.Session()
        req.headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en_US', 'cache-control': 'max-age=0',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1',
            'user-agent': UserAgent})
        with req.get(url) as response_body:
            inspect = Bs4(response_body.text, 'html.parser')
            inspeksi = inspect.find('input', {'name': 'bi_xrwh'})['value']
            cookie = str(req.cookies.get_dict())[1:-1].replace("'", "").replace(",", ";").replace(":", "=")
            if 'checkpoint' in cookie:
                sys.exit("\033[1;31mAccount terminated by Facebook!\033[0m")
            elif 'c_user' in cookie:
                print(f'\n   [\033[38;5;83mCOOKIES\033[0m] \033[38;5;208m{cookie}\033[0m\n\n')
                open('cookies.txt', 'a').write(f'[Cookie] - {cookie}\n\n')
                open('cookie.log', 'w').write(cookie)
                os.system('xdg-open https://github.com/josifkhan')
            else:
                sys.exit("\033[38;5;208mIncorrect details\033[0m")
    except requests.exceptions.ConnectionError:
        sys.exit('No internet')
    except KeyboardInterrupt:
        sys.exit("[+] Stopped!")
