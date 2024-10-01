###############################################
# Coded By Naim Hassan                                                                       #
# A Product Of Brute-Force 71                                                                       #
# https://github.com/Brute-force71/                                                        #
# You Have No Permission To Copy Any Code or Edit This Tool     #
# But You are Welcomed to Take Knowledge From Here                  #
###############################################


import os
import sys
import time
import requests
import json
import ctypes
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import Fore, Style, init
init()


light_green = Fore.LIGHTGREEN_EX
light_white = Fore.LIGHTWHITE_EX
reset = Fore.RESET

class Output:
    RESET = Fore.RESET
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    LIGHT_BLACK = Fore.LIGHTBLACK_EX
    LIGHT_GRAY = Fore.LIGHTWHITE_EX
    LIGHT_RED = Fore.LIGHTRED_EX
    LIGHT_GREEN = Fore.LIGHTGREEN_EX
    LIGHT_YELLOW = Fore.LIGHTYELLOW_EX
    LIGHT_BLUE = Fore.LIGHTBLUE_EX
    LIGHT_MAGENTA = Fore.LIGHTMAGENTA_EX
    LIGHT_CYAN = Fore.LIGHTCYAN_EX

def psb(z):
    for l in z + "\n":
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.01)
        
def psb1(z):
    for l in z + "\n":
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.000)

def logopsb(z):
    for l in z + "\n":
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.000)


def logo():
    ctypes.windll.kernel32.SetConsoleTitleW(f"[ tempmail ] By CYFER")
    System.Clear()
    Write.Print(f"""
████████╗███████╗███╗   ███╗██████╗ ███╗   ███╗ █████╗ ██╗██╗     
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗████╗ ████║██╔══██╗██║██║     
   ██║   █████╗  ██╔████╔██║██████╔╝██╔████╔██║███████║██║██║     
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║╚██╔╝██║██╔══██║██║██║     
   ██║   ███████╗██║ ╚═╝ ██║██║     ██║ ╚═╝ ██║██║  ██║██║███████╗
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                                                                
                                            © Reverse By CYFER
""", Fore.CYAN, interval=0.000)
logo()

def logout():
    psb(Fore.LIGHTCYAN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTCYAN_EX} Thanks For Using Our Tool.."+ Fore.RESET)
    psb(Fore.LIGHTCYAN_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTCYAN_EX} For More Tools, Visit : \n"+ Fore.RESET)
    psb(Fore.LIGHTMAGENTA_EX + f"  [ https://github.com/rxvxrsx ]\n"+ Fore.RESET)
    sys.exit()

def ver_check():
    psb(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Please Wait...."+ Fore.RESET)
    psb(Fore.LIGHTGREEN_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Fetching Data...."+ Fore.RESET)
    try:
        vernow = open(".version", "r").read()
    except:
        vernow = "None"
    while True:
        try:
            mainver = requests.get("https://raw.githubusercontent.com/rxvxrsx/tempmail/main/.version?token=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").text
            break
        except:
            psb(Fore.LIGHTRED_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} Please Connect To The Internet..."+ Fore.RESET)
            k = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Press Enter To Continue..."+ Fore.RESET)
    if not (vernow == mainver):
        psb(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Tool Update Found..."+ Fore.RESET)
        psb(Fore.LIGHTGREEN_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Updating Tool..."+ Fore.RESET)
        os.system("cd .. && rm -rf tempmail && git clone https://github.com/rxvxrsx/tempmail > /dev/null 2>&1")
        psb(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Tool Update Complete..."+ Fore.RESET)
        psb(Fore.LIGHTGREEN_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Starting Tool..."+ Fore.RESET)
        os.system("cd .. && cd tempmail && python tempmail.py"+ Fore.RESET)
    else:
        psb(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Data Successfully Fetched...!!"+ Fore.RESET)
        psb(Fore.LIGHTGREEN_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} WelCome!!"+ Fore.RESET)


def random_mail():
    json_data = {
    "min_name_length" : 10,
    "max_name_length" : 10
    }
    url =  "https://api.internal.temp-mail.io/api/v3/email/new"
    re = requests.post(url, json = json_data)
    data = json.loads(re.text)["email"]
    return data

# API: https://api.internal.temp-mail.io/api/v3/domains
def domain_choose():
    print(Fore.LIGHTMAGENTA_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}1{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} tippabble.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}2{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} rfcdrive.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}3{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} gonetor.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}4{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} zlorkun.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}5{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} somelora.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}6{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} vvatxiy.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}7{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} dygovil.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}8{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} tidissajiiu.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}9{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} vafyxh.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}10{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} knmcadibav.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}11{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} smykwb.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}12{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} wywnxa.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}13{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} qacmjeq.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}14{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} qejjyl.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}15{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} zvvzuv.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}16{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} bltiwd.com"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}17{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} qzueos.com"+ Fore.RESET)
    
    dom = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Enter Your Domain Choice:> "+ Fore.RESET)
    if not (dom == "17"):
        dom = dom.replace("0", "")
    while not dom in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]:
        print(Fore.LIGHTRED_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} Enter a Correct Choice!!"+ Fore.RESET)
        dom = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Enter Your Domain Choice:> "+ Fore.RESET)
        if not (dom == "17"):
            dom = dom.replace("0", "")
    if (dom == "1"):
        doms = "tippabble.com"
    elif (dom == "2"):
        doms = "rfcdrive.com"
    elif (dom == "3"):
        doms = "gonetor.com"
    elif (dom == "4"):
        doms = "zlorkun.com"
    elif (dom == "5"):
        doms = "somelora.com"
    elif (dom == "6"):
        doms = "vvatxiy.com"
    elif (dom == "7"):
        doms = "dygovil.com"
    elif (dom == "8"):
        doms = "tidissajiiu.com"
    elif (dom == "9"):
        doms = "vafyxh.com"
    elif (dom == "10"):
        doms = "knmcadibav.com"
    elif (dom == "11"):
        doms = "smykwb.com"
    elif (dom == "12"):
        doms = "wywnxa.com"
    elif (dom == "13"):
        doms = "qacmjeq.com"
    elif (dom == "14"):
        doms = "qejjyl.com"
    elif (dom == "15"):
        doms = "zvvzuv.com"
    elif (dom == "16"):
        doms = "bltiwd.com"
    elif (dom == "17"):
        doms = "qzueos.com"
        
    return doms

def create_mail():
    url = "https://api.internal.temp-mail.io/api/v3/email/new"
    name = input(Fore.LIGHTCYAN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTCYAN_EX} Enter Email Name:> "+ Fore.RESET)
    domain = domain_choose()
    data = name+"@"+domain
    cost_data = {
        "name" : name,
        "domain" : domain
    }
    j = requests.post(url, json = cost_data)
    return data


def print_mail(data):
    data = json.loads(data)

    if not os.path.exists(".tmp"):
        os.system("touch .tmp")

    em_cont = 1
    for em_data in data:
        data_id = str(em_data["id"])
        opn = open(".tmp", "r").read()

        if data_id in opn:
            continue
        else:
            wrt = open(".tmp", "w")
            wrt.write(opn + "\n" + data_id)
            wrt.close()

        frm = em_data["from"]
        cc = em_data["cc"]
        if cc is None:
            cc = "None"

        to = em_data["to"]
        sub = em_data["subject"]
        mail_data = em_data["body_text"]
        attch = em_data["attachments"]

        psb(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Inbox   : {Fore.RESET}{em_cont}")
        print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} From    : {Fore.RESET}{frm}")
        print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} To      : {Fore.RESET}{to}")
        print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} CC      : {Fore.RESET}{cc}")
        print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Subject : {Fore.RESET}{sub}")
        print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Mail    :\n\n{Fore.RESET}{mail_data}")

        if not (attch == "[]"):
            atc_num = 1
            for atc in attch:
                id = atc["id"]
                down = "https://api.internal.temp-mail.io/api/v3/attachment/" + id + "?download=1"
                print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Attachment No : {Fore.RESET}{atc_num}")
                print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} File Name : {Fore.RESET}{atc['name']}")
                print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} File Size : {Fore.RESET}{str(atc['size'])}[ Bytes ]{Fore.LIGHTGREEN_EX}")
                print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Download From Here : {Fore.RESET}{down}")
                atc_num += 1

        em_cont += 1


    
def invox(mdata):
    psb(Fore.LIGHTYELLOW_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTYELLOW_EX} Press {Fore.LIGHTWHITE_EX}CTRL+C {Fore.LIGHTYELLOW_EX}To Go Back To Main Menu...")
    psb(Fore.LIGHTGREEN_EX + f"\n\t\t{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}*{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTGREEN_EX} Inbox {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}*{Fore.LIGHTYELLOW_EX}]"+ Fore.RESET)
    url = "https://api.internal.temp-mail.io/api/v3/email/"+mdata+"/messages"
    while True:
        try:
            re = requests.get(url).text
            if not re == "[]\n":
                print_mail(re)
            time.sleep(0.000)
        except KeyboardInterrupt:
            break


def see_mail():
    logo()
    if os.path.exists(".mail"):
        old_mails = open(".mail", "r").readlines()
        mn = 1
        psb1(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Your Created Emails : \n")
        for mail in old_mails:
            psb1(Fore.LIGHTGREEN_EX + f"{Fore.LIGHTGREEN_EX}"+str(mn)+": "+ Fore.RESET + mail)
            mn = mn + 1
    else:
        time.sleep(0.000)
        psb1(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} You Currently Have No Old Mail Address"+ Fore.RESET)


def log_old():
    logo()
    try:
        old_mails = open(".mail", "r").readlines()
        mn = 1
    except:
        psb1(Fore.LIGHTRED_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} You Currently Have No Old Mail Address {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX}"+ Fore.RESET)
        return None
    if not (old_mails == "[]"):
        psb1(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Copy The Mail You Want To Restore and Past Below...\n"+ Fore.RESET)
        for mail in old_mails:
            if (mail == ""):
                continue
            psb1(Fore.LIGHTGREEN_EX + f"{Fore.LIGHTGREEN_EX}"+str(mn)+": "+ Fore.RESET + mail)
            mn = mn + 1
        mold = input(Fore.LIGHTGREEN_EX + f"\n    {Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Past Your Mail:> "+ Fore.RESET)
        while not mold+"\n" in old_mails and not mold in old_mails and not mold == "":
            psb1(Fore.LIGHTRED_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Only Past Emails From Above..."+ Fore.RESET)
            mold = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Past your Mail:> "+ Fore.RESET)
        if (mold == ""):
            mold = None
        return mold
    else:
        psb1(Fore.LIGHTRED_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} You Currently Have No Old Mail Address {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX}"+ Fore.RESET)
        return None


def remove():
    logo()
    psb1(Fore.LIGHTYELLOW_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTYELLOW_EX} Removing All Old Mail's Data..."+ Fore.RESET)
    psb1(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Please Wait...."+ Fore.RESET)
    time.sleep(0.000)
    try:
        os.system("rm .mail")
    except:
        pass
    try:
        os.system("rm .tmp")
    except:
        pass
    psb1(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Successfully Removed All Old Mails Data..."+ Fore.RESET)


def main():
    logo()
    psb(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Choose Your Method..."+ Fore.RESET)
    print(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}01{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Genarate Random Mail"+ Fore.RESET)
    print(Fore.LIGHTGREEN_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}02{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Custom Mail Address"+ Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}03{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} See Mails You Created"+ Fore.RESET)
    print(Fore.LIGHTCYAN_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}04{Fore.LIGHTWHITE_EX}]{Fore.LIGHTCYAN_EX} Log In To Old Mails"+ Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}05{Fore.LIGHTWHITE_EX}]{Fore.LIGHTYELLOW_EX} Remove All Old Mail's Data"+ Fore.RESET)
    print(Fore.LIGHTRED_EX + f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}00{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} Exit"+ Fore.RESET)
    op = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Choose Your Option:> "+ Fore.RESET).replace("#", "").replace("00", "0")
    while not op in ["1", "2", "3", "4", "5", "0"]:
        print(Fore.LIGHTRED_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} Choose a Correct Option!!"+ Fore.RESET)
        op = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Choose Your Option:> "+ Fore.RESET).replace("#", "").replace("00", "0")
    if (op == "1"):
        mdata = random_mail()
        do_mail(mdata)
        o = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Press ENTER To Go Back...."+ Fore.RESET)
    elif (op == "2"):
        mdata = create_mail()
        do_mail(mdata)
        o = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Press ENTER To Go Back...."+ Fore.RESET)
    elif (op == "3"):
        see_mail()
        o = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Press ENTER To Go Back...."+ Fore.RESET)
    elif (op == "4"):
        mdata = log_old()
        if not (mdata == None):
            do_mail(mdata)
        o = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Press ENTER To Go Back...."+ Fore.RESET)
    elif (op == "5"):
        remove()
        o = input(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Press ENTER To Go Back...."+ Fore.RESET)
    elif (op == "0"):
        logout()
    
    
def do_mail(mdata):
    if not os.path.exists(".mail"):
        os.system("touch .mail")
    fmopn = open(".mail", "r").read()
    fmout = open(".mail", "w")
    if not (fmopn == "") and not (mdata in fmopn):
        fmout.write(fmopn+"\n"+mdata)
    elif (fmopn == ""):
        fmout.write(mdata)
    else:
        fmout.write(fmopn)
    fmout.close()
    logo()
    psb(Fore.LIGHTGREEN_EX + f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}*{Fore.LIGHTWHITE_EX}]{Fore.LIGHTGREEN_EX} Your Created Mail : "+ Fore.RESET+mdata)
    invox(mdata)
    

if __name__ == "__main__":
    ver_check()
    while True:
        main()

