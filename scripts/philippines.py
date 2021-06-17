import requests
import json

# for console text coloring
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Put your API key here
apiKey = "API KEY HERE'

# JSON Requester
rpli = requests.get("https://api.checkwx.com/metar/RPLI?x-api-key=" + apiKey)
rplc = requests.get("https://api.checkwx.com/metar/RPLC?x-api-key=" + apiKey)
rplb = requests.get("https://api.checkwx.com/metar/RPLB?x-api-key=" + apiKey)
rpll = requests.get("https://api.checkwx.com/metar/RPLL?x-api-key=" + apiKey)
rpvm = requests.get("https://api.checkwx.com/metar/RPVM?x-api-key=" + apiKey)
rpvp = requests.get("https://api.checkwx.com/metar/RPVP?x-api-key=" + apiKey)
rpvd = requests.get("https://api.checkwx.com/metar/RPVD?x-api-key=" + apiKey)
rpmd = requests.get("https://api.checkwx.com/metar/RPMD?x-api-key=" + apiKey)
rpmz = requests.get("https://api.checkwx.com/metar/RPMZ?x-api-key=" + apiKey)
rpmr = requests.get("https://api.checkwx.com/metar/RPMR?x-api-key=" + apiKey)

# Fetch Alert
print("Fetching Latest METAR Report...")

# fetch, parse and display METAR data
try:
    rpli.raise_for_status()
    resp = rpli.json()
    print(f"{bcolors.OKCYAN}Laoag International Airport{bcolors.ENDC}")
    print(resp['data'])

    rplc.raise_for_status()
    resp = rplc.json()
    print(f"{bcolors.OKCYAN}Clark International Airport{bcolors.ENDC}")
    print(resp['data'])

    rplb.raise_for_status()
    resp = rplb.json()
    print(f"{bcolors.OKCYAN}Subic Bay International Airport{bcolors.ENDC}")
    print(resp['data'])

    rpll.raise_for_status()
    resp = rpll.json()
    print(f"{bcolors.OKCYAN}Ninoy Aquino International Airport (Manila International Airport){bcolors.ENDC}")
    print(resp['data'])

    rpvm.raise_for_status()
    resp = rpvm.json()
    print(f"{bcolors.OKCYAN}Mactan Cebu International Airport{bcolors.ENDC}")
    print(resp['data'])

    rpvp.raise_for_status()
    resp = rpvp.json()
    print(f"{bcolors.OKCYAN}Puerto Princesa International Airport{bcolors.ENDC}")
    print(resp['data'])

    rpvd.raise_for_status()
    resp = rpvd.json()
    print(f"{bcolors.OKCYAN}Sibulan Airport{bcolors.ENDC}")
    print(resp['data'])

    rpmd.raise_for_status()
    resp = rpmd.json()
    print(f"{bcolors.OKCYAN}Fransisco Bangoy International Airport{bcolors.ENDC}")
    print(resp['data'])

    rpmz.raise_for_status()
    resp = rpmz.json()
    print(f"{bcolors.OKCYAN}Zamboanga International Airport{bcolors.ENDC}")
    print(resp['data'])

    rpmr.raise_for_status()
    resp = rpmr.json()
    print(f"{bcolors.OKCYAN}Zamboanga International Airport{bcolors.ENDC}")
    print(resp['data'])

# Error
except requests.exceptions.HTTPError as e:
    print(e)
