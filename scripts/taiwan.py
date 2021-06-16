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
apiKey = '588ab41cee2f41d0b946967069'

# JSON Requester
rctp = requests.get("https://api.checkwx.com/metar/RCTP?x-api-key=" + apiKey)
rckh = requests.get("https://api.checkwx.com/metar/RCKH?x-api-key=" + apiKey)
rcss = requests.get("https://api.checkwx.com/metar/RCSS?x-api-key=" + apiKey)
rcmq = requests.get("https://api.checkwx.com/metar/RCMQ?x-api-key=" + apiKey)
rcqc = requests.get("https://api.checkwx.com/metar/RCQC?x-api-key=" + apiKey)
rcnn = requests.get("https://api.checkwx.com/metar/RCNN?x-api-key=" + apiKey)
rcfn = requests.get("https://api.checkwx.com/metar/RCFN?x-api-key=" + apiKey)

# Fetch Alert
print("Fetching Latest METAR Report...")

# fetch, parse and display METAR data
try:
    rctp.raise_for_status()
    resp = rctp.json()
    print(f"{bcolors.OKCYAN}Taiwan Taoyuan International Airport{bcolors.ENDC}")
    print(resp['data'])

    rckh.raise_for_status()
    resp = rckh.json()
    print(f"{bcolors.OKCYAN}Kaohsiung International Airport{bcolors.ENDC}")
    print(resp['data'])

    rcss.raise_for_status()
    resp = rcss.json()
    print(f"{bcolors.OKCYAN}Taipei Songshan Airport{bcolors.ENDC}")
    print(resp['data'])

    rcmq.raise_for_status()
    resp = rcmq.json()
    print(f"{bcolors.OKCYAN}Taichung International Airport / Ching Chuang Kang Air Base{bcolors.ENDC}")
    print(resp['data'])

    rcqc.raise_for_status()
    resp = rcqc.json()
    print(f"{bcolors.OKCYAN}Penghu Magong Airport{bcolors.ENDC}")
    print(resp['data'])

    rcnn.raise_for_status()
    resp = rcnn.json()
    print(f"{bcolors.OKCYAN}Tainan International Airport / Tainan Air Base{bcolors.ENDC}")
    print(resp['data'])

    rcfn.raise_for_status()
    resp = rcfn.json()
    print(f"{bcolors.OKCYAN}Taitung Airport{bcolors.ENDC}")
    print(resp['data'])

# Error
except requests.exceptions.HTTPError as e:
    print(e)
