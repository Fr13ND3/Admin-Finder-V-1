from os import system
try:
    from colorama import Fore,init
    init(autoreset=False)
except ModuleNotFoundError:
    system('pip install colorama')
    print("OK I'M Install Module <colorama> ! If not Installed try agin =  Window : pip install colorama --user  ,, Linux : sudo pip install colorama")

def printer_help():
    """ To display help text """
    print(Fore.LIGHTBLACK_EX+"""Usage:
    python main.py -h  == For Helping
    python main.py -u www.target.com == For Run Script
           """)


def printer_connection_failed():
    print(Fore.RED+"Error ! Please Check Your Target or Internet Connection")


def printer_found_page(target):
    return Fore.GREEN + f"[+] Url Found : {target}"


def printer_not_found_page(target):
    return Fore.RED + f"[-] Url NotFound : {target}"


def about_programer():
    print(Fore.GREEN + "        Admin Page Finder v1")
    print(Fore.WHITE + "      Telegram CH : @Arch_Team")
    print(Fore.RED + "    Telegram programer : @Cra3ked")
    print(Fore.WHITE + "**************************************")