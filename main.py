# Admin Finder version 1 By Zed-Team
# Telegram Channel : @Arch_TM
# Admin : @Cra3ked
 
from requests import get,status_codes

from sys import argv
from os import system
try:
    from colorama import Fore,init
    init(autoreset=False)
except ModuleNotFoundError:
    system('pip install colorama')
    print("OK I'M Install Module <colorama> ! If not Installed try agin =  Window : pip install colorama --user  ,, Linux : sudo pip install colorama")
import finder
import printer



def main():
    if len(argv) <= 2:
        printer.printer_help()
    else:
        if argv[1] == "-h":
            printer.printer_help()
        elif argv[1].lower() == "-u":
            if len(argv) >= 3:
                Target = argv[2]
                if "https://" in Target:
                    Target = Target.replace('https://','http://')
                elif "http://" not in Target:
                    Target = "http://" + Target
                elif "/" not in Target.endswith():
                    Target = Target + "/"
                try:
                    test_req = get(Target)
                    if test_req.status_code == 200:
                        finder.Find_admin_page(Target)
                    else:
                        printer.printer_connection_failed()
                except Exception:
                    printer.printer_connection_failed()
        


if __name__ == "__main__":
    printer.about_programer()
    main()