import json
import urllib.request
from colorama import Fore, init
import webbrowser
init()

def logo():
    print(Fore.RED)
    logo = f"""
  ___ ___ _                 _           
 |_ _| _ \ |   ___  __ __ _| |_ ___ _ _ 
  | ||  _/ |__/ _ \/ _/ _` |  _/ _ \ '_|
 |___|_| |____\___/\__\__,_|\__\___/_|  
"""
    print(logo)

logo()

while True:
    print(Fore.LIGHTYELLOW_EX)
    ip_adress = input("Enter target IP : ")
    url = "http://ip-api.com/json/"
    anwser = urllib.request.urlopen(url + ip_adress)
    ipdata = anwser.read()
    values = json.loads(ipdata)

    print(Fore.LIGHTYELLOW_EX + "\nIP: " + Fore.LIGHTWHITE_EX + values['query'])
    print(Fore.LIGHTYELLOW_EX + "City: "  + Fore.LIGHTWHITE_EX + values['city'])
    print(Fore.LIGHTYELLOW_EX + "Country: " + Fore.LIGHTWHITE_EX + values['country'])
    print(Fore.LIGHTYELLOW_EX + "ZIP code: "  + Fore.LIGHTWHITE_EX + values['zip'])
    print(Fore.LIGHTYELLOW_EX + "ISP: "  + Fore.LIGHTWHITE_EX + values['isp'])

    print(Fore.LIGHTYELLOW_EX)
    map = input("Open map with target IP ? Y or N : ")
    if map == "Y" or "y" or "yes":
        webbrowser.open("https://www.infosniper.net/index.php?lang=&ip_address=" + ip_adress)
    else:
        exit()

    break


