from multiprocessing.pool import ThreadPool
from fake_useragent import UserAgent
from bs4 import BeautifulSoup, SoupStrainer
from colorama import *
import os, sys, time
import requests, random
import cloudscraper, re

#this is my design

wpscan_api = open("wpscan-api.txt","r").read()

jbackup = []
jcomponet = []

joomla_thread = 5
componets_thread = 5

def comp_h(url):
    headers={
        "User-Agent": UserAgent().random
    }
    try:
        kaynak = request(url, cf, headers, {}, {}, "get", 10)
        if (kaynak.status_code == 200):
            comp = url.split("/")[5]
            try:
                kaynak = request(url+comp.replace("com_","")+".xml", cf, headers, {}, {}, "get", 10)
                if ('<extension type="component"' in kaynak.text):
                    soup = BeautifulSoup(kaynak.text,'xml')
                    version = soup.find_all('extension')[0].get('version')
                else:
                    version = "bulunamadı"
            except Exception as e:
                print(e)
                version = "bulunamadı"
            jcomponet.append([url, version, comp, time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())])
    except:
        pass

def backup_h(url):
    headers={
        "User-Agent": UserAgent().random
    }
    try:
        kaynak = request(url, cf, headers, {}, {}, "get", 12)
        if (kaynak.status_code != 404):
            jbackup.append(url)
    except:
        pass

def vbulletin(url, cf):
    pass

def joomla(url, cf):
    headers={
        "User-Agent": UserAgent().random
    }
    versiyon_url = ["administrator/manifests/files/joomla.xml","language/en-GB/en-GB.xml","administrator/components/com_content/content.xml","administrator/components/com_plugins/plugins.xml","administrator/components/com_media/media.xml","mambots/content/moscode.xml"]
    joomla_dosyalar = ["robots.txt","htaccess.txt","web.config.txt","LICENSE.txt","README.txt"]
    joomla_config = ['configuration.php_old','configuration.php_new','configuration.php~','configuration.php.new','configuration.php.new~','configuration.php.old','configuration.php.old~','configuration.bak','configuration.php.bak','configuration.php.bkp','configuration.txt','configuration.php.txt','configuration - Copy.php','configuration.php.swo','configuration.php_bak','configuration.php#','configuration.orig','configuration.php.save','configuration.php.original','configuration.php.swp','configuration.save','.configuration.php.swp','configuration.php1','configuration.php2','configuration.php3','configuration.php4','configuration.php4','configuration.php6','configuration.php7','configuration.phtml','configuration.php-dist']
    joomla_panel = ['administrator','admin','panel','webadmin','modir','manage','administration','joomla/administrator','joomla/admin']
    joomla_backup = ['1.txt','2.txt','1.gz','1.rar','1.save','1.tar','1.tar.bz2','1.tar.gz','1.tgz','1.tmp','1.zip','2.back','2.backup','2.gz','2.rar','2.save','2.tar','2.tar.bz2','2.tar.gz','2.tgz','2.tmp','2.zip','backup.back','backup.backup','backup.bak','backup.bck','backup.bkp','backup.copy','backup.gz','backup.old','backup.orig','backup.rar','backup.sav','backup.save','backup.sql~','backup.sql.back','backup.sql.backup','backup.sql.bak','backup.sql.bck','backup.sql.bkp','backup.sql.copy','backup.sql.gz','backup.sql.old','backup.sql.orig','backup.sql.rar','backup.sql.sav','backup.sql.save','backup.sql.tar','backup.sql.tar.bz2','backup.sql.tar.gz','backup.sql.tgz','backup.sql.tmp','backup.sql.txt','backup.sql.zip','backup.tar','backup.tar.bz2','backup.tar.gz','backup.tgz','backup.txt','backup.zip','database.back','database.backup','database.bak','database.bck','database.bkp','database.copy','database.gz','database.old','database.orig','database.rar','database.sav','database.save','database.sql~','database.sql.back','database.sql.backup','database.sql.bak','database.sql.bck','database.sql.bkp','database.sql.copy','database.sql.gz','database.sql.old','database.sql.orig','database.sql.rar','database.sql.sav','database.sql.save','database.sql.tar','database.sql.tar.bz2','database.sql.tar.gz','database.sql.tgz','database.sql.tmp','database.sql.txt','database.sql.zip','database.tar','database.tar.bz2','database.tar.gz','database.tgz','database.tmp','database.txt','database.zip','joom.back','joom.backup','joom.bak','joom.bck','joom.bkp','joom.copy','joom.gz','joomla.back','Joomla.back','joomla.backup','Joomla.backup','joomla.bak','Joomla.bak','joomla.bck','Joomla.bck','joomla.bkp','Joomla.bkp','joomla.copy','Joomla.copy','joomla.gz','Joomla.gz','joomla.old','Joomla.old','joomla.orig','Joomla.orig','joomla.rar','Joomla.rar','joomla.sav','Joomla.sav','joomla.save','Joomla.save','joomla.tar','Joomla.tar','joomla.tar.bz2','Joomla.tar.bz2','joomla.tar.gz','Joomla.tar.gz','joomla.tgz','Joomla.tgz','joomla.zip','Joomla.zip','joom.old','joom.orig','joom.rar','joom.sav','joom.save','joom.tar','joom.tar.bz2','joom.tar.gz','joom.tgz','joom.zip','site.back','site.backup','site.bak','site.bck','site.bkp','site.copy','site.gz','site.old','site.orig','site.rar','site.sav','site.save','site.tar','site.tar.bz2','site.tar.gz','site.tgz','site.zip','sql.zip.back','sql.zip.backup','sql.zip.bak','sql.zip.bck','sql.zip.bkp','sql.zip.copy','sql.zip.gz','sql.zip.old','sql.zip.orig','sql.zip.save','sql.zip.tar','sql.zip.tar.bz2','sql.zip.tar.gz','sql.zip.tgz','upload.back','upload.backup','upload.bak','upload.bck','upload.bkp','upload.copy','upload.gz','upload.old','upload.orig','upload.rar','upload.sav','upload.save','upload.tar','upload.tar.bz2','upload.tar.gz','upload.tgz','upload.zip']
    joomla_dizinler = ['administrator/components','components','administrator/modules','modules','administrator/templates','templates','cache','images','includes','language','media','templates','tmp','images/stories','images/banners']
    try:
        kaynak = request(url, cf, headers, {}, {}, "get", 30)
        print(f"\n{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Header bilgileri")
        for h in kaynak.headers:
            if (ara(h, 1) == False):
                print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTMAGENTA_EX}{h}{Fore.LIGHTWHITE_EX}: {kaynak.headers[h]}")
    except:
        return ""
    try:
        version = ""
        for vu in versiyon_url:
            try:
                kaynak = request(url+"/"+vu, cf, headers, {}, {}, "get", 30)
                aaa = kaynak.status_code
            except:
                continue
            if ("<version>" in kaynak.text):
                soup = BeautifulSoup(kaynak.text,'xml')
                version = soup.find_all('version')[0].text
                break
        if (version != ""):
            print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Joomla Versiyon: {Fore.LIGHTMAGENTA_EX}{version}")
    except Exception as e:
        print(e)

    corevul = "https://raw.githubusercontent.com/OWASP/joomscan/master/exploit/db/corevul.txt"
    try:
        if (version != ""):
            corevult = request(corevul, False, headers, {}, {}, "get", 30).text.splitlines()
            for core in corevult:
                if (version in core.split("|")[0]):
                    veriler = core.split('|')[1]
                    veriler = veriler.split('\\n')
                    baslik = veriler[0]
                    cve = veriler[1].replace("CVE : ","")
                    linkler = []
                    for link in veriler:
                        if ("http://" in link or "https://" in link):
                            if ("EDB :" in link):
                                link = link.replace("EDB : ","")
                            linkler.append(link)
                    print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTRED_EX}[+] {Fore.LIGHTMAGENTA_EX}{baslik}")
                    print(f"{Fore.LIGHTWHITE_EX} |      - {cve}")
                    for link in linkler:
                        print(f"{Fore.LIGHTWHITE_EX} |      - {link}")
    except:
        pass
    try:
        print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Joomla Dizinleri")
        for jd in joomla_dizinler:
            try:
                kaynak = request(url+jd, cf, headers, {}, {}, "get", 10)
            except:
                continue
            if (kaynak.status_code != 404):
                print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTMAGENTA_EX}Durum Kodu: {Fore.LIGHTWHITE_EX}{str(kaynak.status_code)}{Fore.LIGHTMAGENTA_EX} Dizin: {Fore.LIGHTWHITE_EX}: {jd}")
    except:
        pass
    try:
        print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Kontrol Panel")
        for jd in joomla_panel:
            try:
                kaynak = request(url+jd, cf, headers, {}, {}, "get", 10)
            except:
                continue
            if (kaynak.status_code != 404):
                print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTMAGENTA_EX}Durum Kodu: {Fore.LIGHTWHITE_EX}{str(kaynak.status_code)}{Fore.LIGHTMAGENTA_EX} Dizin: {Fore.LIGHTWHITE_EX}: {jd}")
    except:
        pass
    try:
        print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Config Dosyaları")
        for jd in joomla_config:
            try:
                kaynak = request(url+jd, cf, headers, {}, {}, "get", 10)
            except:
                continue
            if (kaynak.status_code != 404 and "Multiple Choices" not in kaynak.text):
                print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTMAGENTA_EX}Durum Kodu: {Fore.LIGHTWHITE_EX}{str(kaynak.status_code)}{Fore.LIGHTMAGENTA_EX} Dizin: {Fore.LIGHTWHITE_EX}: {jd}")
    except:
        pass
    try:
        print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Backup Dosyaları")
        joomla_urller = []
        for backup in joomla_backup:
            joomla_urller.append(url+"/"+backup)
        p = ThreadPool(joomla_thread)
        p.map(backup_h, joomla_urller)
        time.sleep(2)
        if (len(jbackup) != 0):
            for jb in jbackup:
                print(f"{Fore.LIGHTWHITE_EX} | Dizin: {Fore.LIGHTWHITE_EX}: {jb}")
    except Exception as e:
        print(e)
    try:
        print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Diğer Dosyalar")
        for jd in joomla_dosyalar:
            try:
                kaynak = request(url+jd, cf, headers, {}, {}, "get", 10)
            except:
                continue
            if (kaynak.status_code != 404):
                print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTMAGENTA_EX}Durum Kodu: {Fore.LIGHTWHITE_EX}{str(kaynak.status_code)}{Fore.LIGHTMAGENTA_EX} Dizin: {Fore.LIGHTWHITE_EX}: {jd}")
    except:
        pass
    componentslist = "https://raw.githubusercontent.com/OWASP/joomscan/master/exploit/db/componentslist.txt"
    try:
        componentslist = request(componentslist, False, headers, {}, {}, "get", 30).text.splitlines()
        linkler = []
        for comp in componentslist:
            linkler.append(url+"/components/"+comp+"/")
        p = ThreadPool(componets_thread)
        p.map(comp_h, linkler)
        time.sleep(2)
        if (len(jcomponet) != 0):
            for i in jcomponet:
                print(f"{Fore.LIGHTGREEN_EX}[+]-[{i[3]}] {Fore.WHITE}Component: {i[2]}")
                print(f"{Fore.LIGHTWHITE_EX} |      - Url: {Fore.LIGHTMAGENTA_EX}{i[0]}")
                print(f"{Fore.LIGHTWHITE_EX} |      - Version: {Fore.LIGHTMAGENTA_EX}{i[1]}")
    except:
        pass
    

def ara(t, n):
    if (n == 1):
        l = ["report-to","nel","link","alt-svc","set-cookie"]
        for i in l:
            if (t.lower() in i):
                return True
    return False

def wordpress(url, cf):
    headers={
        "User-Agent": UserAgent().random
    }
    headers2 = {
        "Authorization":"Token token="+wpscan_api
    }
    wordpress_dizinler = [
        "/robots.txt","/feed/","/xmlrpc.php","/wp-sitemap.xml"
    ]
    try:
        kaynak = request(url, cf, headers, {}, {}, "get", 30)
        print(f"\n{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Header bilgileri:")
        for h in kaynak.headers:
            if (ara(h, 1) == False):
                print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTMAGENTA_EX}{h}{Fore.LIGHTWHITE_EX}: {kaynak.headers[h]}")
    except:
        return ""
    try:
        print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Wordpress Dizinleri:")
        for wpd in wordpress_dizinler:
            try:
                kaynak = request(url+wpd, cf, headers, {}, {}, "get", 30)
            except:
                continue
            print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTMAGENTA_EX}Durum Kodu: {Fore.LIGHTWHITE_EX}{str(kaynak.status_code)}{Fore.LIGHTMAGENTA_EX} Dizin: {Fore.LIGHTWHITE_EX}: {wpd}")
            
    except:
        pass
    try:
        kaynak = request(url+"/feed", cf, headers, {}, {}, "get", 30).text
        if ('https://wordpress.org/?v=' in kaynak):
            soup = BeautifulSoup(kaynak,'xml')
            version = soup.find_all('generator')[0].text
            if(len(version) > 0):
                version = version.replace("https://wordpress.org/?v=","")
            else:
                version = "bulunamadı"
        else:
            version = "bulunamadı"
        print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}WordPress Versiyon: {Fore.LIGHTMAGENTA_EX}{version}")
    except:
        pass
    if (version != "bulunamadı"):
        wurl = "https://wpscan.com/api/v3/wordpresses/" + version.replace(".","")
        try:
            xf = False
            wpscan = request(wurl, xf, headers2, {}, {}, "get", 30)
            for vuln in wpscan.json()[version]["vulnerabilities"]:
                print(f"{Fore.LIGHTWHITE_EX} | {Fore.LIGHTRED_EX}[+] {Fore.LIGHTMAGENTA_EX}{vuln['title']}")
                for ref in vuln['references']["url"]:
                    print(f"{Fore.LIGHTWHITE_EX} |      - {ref}")
                cve = "https://cve.mitre.org/cgi-bin/cvename.cgi?name=" + vuln['references']["cve"][0]
                print(f"{Fore.LIGHTWHITE_EX} |      - {cve}")
                print(f"{Fore.LIGHTWHITE_EX} |      - https://wpscan.com/vulnerability/{vuln['id']}")
        except:
            pass
    try:
        theme = re.compile(r'wp-content/themes/(.*?)/')
        ver = re.compile(r'/?ver=(([0-9]*\.?[0-9]*)*)')
        ciklet = []
        kaynak = request(url, cf, headers, {}, {}, "get", 30).text
        if ("http://" in url):
            xd = "^http://"
        else:
            xd = "^https://"
        soup = BeautifulSoup(kaynak, "html.parser")
        mm = ["link","script"]
        xx = ["href","src"]
        for m in mm:
            for x in xx:
                for link in soup.find_all(m,attrs={x: re.compile(xd)}):
                    ciklet.append(link.get(x))
        data = []
        for cik in list(set(ciklet)):
            if ("/plugins/" in cik):
                nurl = url + "/wp-content/plugins/" + cik.split("/")[5] + "/readme.txt"
            elif ("/themes/" in cik):
                nurl = url + "/wp-content/themes/" + cik.split("/")[5] + "/readme.txt"
            else:
                continue
            try:
                kaynak = request(nurl, cf, headers, {}, {}, "get", 30)
            except:
                continue
            try:
                aaaaa = kaynak.status_code
            except:
                continue
            if (kaynak.status_code == 200):
                version = ""
                for c in kaynak.text.splitlines():
                    if ("Stable tag:" in c):
                        version = c.replace("Stable tag: ", "")
                        break
                if (version != ""):
                    y = False
                    for ch in data:
                        if (cik.split("/")[5] == ch[2]):
                            y = True
                            break
                    if (y == True):
                        continue

                    if ("/plugins/" in cik):
                        data.append(["plugin", version, cik.split("/")[5]])
                    elif ("/themes/" in cik):
                        data.append(["theme", version, cik.split("/")[5]])
        for d in data:
            if (d[0] == "plugin"):
                print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Plugin: {d[2]}")
                print(f"{Fore.LIGHTWHITE_EX} |      - Version: {d[1]}")
            elif (d[0] == "theme"):
                print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Theme: {d[2]}")
                print(f"{Fore.LIGHTWHITE_EX} |      - Version: {d[1]}")
    except Exception as e:
        print(e)
    kullanicilar = []
    try:
        surl = url + "/wp-json/wp/v2/users/"
        kaynak = request(surl, cf, headers, {}, {}, "get", 30).json()
        for k in kaynak:
            kullanicilar.append(k["slug"])
    except:
        pass

    for n in range(1,30):
        try:
            ourl = url + "/?author="+str(n)
            kaynak = request(ourl, cf, headers, {}, {}, "get", 30)
            u = re.findall('href="https://haubooks.org/author/(.*?)/feed/"', kaynak.text)[0]
            kullanicilar.append(u)
        except:
            pass
    kullanicilar = list(set(kullanicilar))
    if (len(kullanicilar) != 0):
        print(f"{Fore.LIGHTGREEN_EX}[+]-[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}{len(kullanicilar)} kullanıcı bulundu.")
        for k in kullanicilar:
            print(f"{Fore.LIGHTWHITE_EX} |      - Kullanıcı Adı: {Fore.LIGHTMAGENTA_EX}{k}")
        


def cms_bul(url, cf):
    headers={
        "User-Agent": UserAgent().random
    }
    joomla = ["/administrator/","/administrator/language/en-GB/install.xml","/administrator/help/en-GB/toc.json","/plugins/system/debug/debug.xml"]
    for jm in joomla:
        try:
            kaynak = request(url+jm, cf, headers, {}, {}, "get", 30).text
            if ('mod-login-username' in kaynak or '<author>Joomla!' in kaynak or "COMPONENTS_BANNERS_BANNERS" in kaynak):
                return "joomla"
        except:
            continue
    wordpress = ["/wp-login.php","/wp-admin/upgrade.php","/","/wp-includes/js/jquery/jquery.js"]
    for wp in wordpress:
        try:
            kaynak = request(url+wp, cf, headers, {}, {}, "get", 30).text
            if ('id="user_login"' in kaynak or url.split('/')[2]+"/wp-content/" in kaynak or url.split('/')[2]+"/wp-inclues" in kaynak or "(c) jQuery Foundation" in kaynak):
                return "wordpress"
        except:
            continue
    xenforo = ["/"]

def request(url, cf, headers, data, params, method, timeout):
    try:
        if (cf == True):
            if (method.lower() == "get"):
                scraper = cloudscraper.CloudScraper()
                kaynak = scraper.get(url, headers=headers, params=params, timeout=timeout)
                return kaynak
            else:
                scraper = cloudscraper.CloudScraper()
                kaynak = scraper.post(url, headers=headers, data=data, timeout=timeout)
                return kaynak
        else:
            if (method.lower() == "get"):
                kaynak = requests.get(url, headers=headers, params=params, timeout=timeout)
                return kaynak
            else:
                kaynak = requests.post(url, headers=headers, data=data, timeout=timeout)
                return kaynak
    except:
        return ""

def wkontrol(url):
    req = requests.get(url)
    wf = [
        "cloudflare","Cloudfront","ddos-guard","imunify360","mod_security","Sucuri","WatchGuard"
    ]
    for w in wf:
        if (w in req.headers["Server"]):
            return w
    return ""

def videooner():
    url = "https://raw.githubusercontent.com/cannibal-hannibal/listeler/main/videolar.txt"
    kaynak = requests.get(url).text
    link = random.choice(kaynak.splitlines())
    return link

def sarkioner():
    url = "https://raw.githubusercontent.com/cannibal-hannibal/listeler/main/sarkilar.txt"
    kaynak = requests.get(url).text
    link = random.choice(kaynak.splitlines())
    return link

def banner():
    if (sys.platform == "win32"):
        os.system("cls")
    else:
        os.system("cls")

    print(fr"""{Fore.LIGHTGREEN_EX}

 ██████╗███╗   ███╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║     ██╔████╔██║███████╗    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║     ██║╚██╔╝██║╚════██║    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗██║ ╚═╝ ██║███████║    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═════╝╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{Fore.LIGHTMAGENTA_EX}

  [ V0.1 | Coded By Will Graham  | Github: @cannibal-hannibal  | Telegram: @wwillgraham]

    """)

def main():
    banner()
    #f"{Fore.LIGHTMAGENTA_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Hedef siteyi giriniz: "
    url = input(f"{Fore.LIGHTMAGENTA_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Hedef siteyi giriniz: ")
    if (url.strip() == ""):
        print(f"{Fore.LIGHTRED_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}İşlemlerin başlatılabilmesi için bir hedef belirtmeniz gerekiyor. ")
        exit()
    elif ("http" not in url.strip()):
        print(f"{Fore.LIGHTRED_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Girilen url'nin başında http:// veya https:// olması zorunludur. ")
        exit()
    sure =  time.time()
    print(f"\n{Fore.LIGHTCYAN_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Güvenlik açığı taraması biraz uzun sürebilir. Dilerseniz önerdiğimiz şarkı veya video'yu izliyebilirsiniz. ")
    print(f"{Fore.LIGHTCYAN_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Video: {Fore.LIGHTYELLOW_EX}{videooner()}")
    print(f"{Fore.LIGHTCYAN_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Şarkı: {Fore.LIGHTYELLOW_EX}{sarkioner()}\n")
    print(f"{Fore.LIGHTCYAN_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Güvenlik duvarı kontrol ediliyor... ")
    kontrol = wkontrol(url)
    if (kontrol.strip() != ""):
        cevap = input(f"\n{Fore.LIGHTMAGENTA_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Sitede günenlik duvarı bulundu, devam etmek ister misiniz?(E/H): ")
        if (cevap.upper() == "H"):
            exit()
        print("")
    else:
        print(f"{Fore.LIGHTCYAN_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Site de herhangi bir {Fore.LIGHTMAGENTA_EX}güvenlik duvarı bulunamadı. ")
    global cf
    if (kontrol.strip() == "cloudflare"):
        cf = True
    else:
        cf = False
    print(f"{Fore.LIGHTCYAN_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Sitenin içerik yönetim sistemi tespit ediliyor... ")
    cms = cms_bul(url, cf)
    print(f"{Fore.LIGHTCYAN_EX}[{time.strftime('%m.%d.%Y %H:%M:%S', time.localtime())}] {Fore.WHITE}Sitenin içerik yönetim sistemi: {Fore.LIGHTMAGENTA_EX}{cms.title()}")
    if (cms == "wordpress"):
        wordpress(url, cf)
    elif (cms == "joomla"):
        joomla(url, cf)
    elif (cms == "vbulletin"):
        vbulletin(url, cf)
    sure = time.gmtime(time.time() - sure)
    print(f"{Fore.LIGHTCYAN_EX}[*]{Fore.WHITE} İşlem süresi: {Fore.LIGHTMAGENTA_EX}{sure.tm_hour} {Fore.WHITE}saat {Fore.LIGHTMAGENTA_EX}{sure.tm_min} {Fore.WHITE}dakika {Fore.LIGHTMAGENTA_EX}{sure.tm_sec} {Fore.WHITE}saniye")
    print(f"{Fore.LIGHTGREEN_EX}[*]{Fore.WHITE} Tarama bitmiştir.")
    
if (__name__=="__main__"):
    try:
        init()
        main()
    except KeyboardInterrupt:
        exit()