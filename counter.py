#!/usr/bin/python3
# created by r2dr0dn (younes-benl)
import json
import requests
from colorama import Fore,Back
url = "https://raw.githubusercontent.com/r2dr0dn/Counter/master/data.json"
data = requests.get(url).content
visual = json.loads(data)
print(Fore.WHITE + """
                                                    Covid-19 Live Counter
                                                     by Ybenel (r2dr0dn)
""")
for countries in visual['countries']:
    print("\033[01;36m" + "Country: " + Fore.GREEN + countries['country'] + Fore.BLUE + "\nCases: " + Fore.RED + countries['cases'] + Fore.YELLOW + " New Cases: " + Fore.MAGENTA + countries['new_cases'] + Fore.GREEN + " Total Deaths: " + Fore.BLUE + countries['total_deaths'] + Fore.CYAN + " New Deaths: " + Fore.GREEN + countries['new_deaths'] + Fore.RED + " Total Recovered: " + Fore.YELLOW + countries['total_recoverd'] + Fore.CYAN + " Active Cases: " + Fore.MAGENTA + countries['active_cases'] + Fore.WHITE + " Surious Cases: " + Fore.GREEN +countries['surios_cases'])
