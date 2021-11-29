import requests
import json
import find_proxy
import random
from  time import sleep
from pwn import *
import string
from dotenv import load_dotenv
load_dotenv()
# Two steps
# Step 1: Spin the wheel and get the coupon
# Step 2: Check the coupon to see if it's 50% discount
url = f"{os.environ['URL']}"
headers = {}
headers["Host"] = f"{os.environ['Host']}"
headers["User-Agent"] = f"{os.environ['User-Agent']}"
headers["Accept"] = f"{os.environ['Accept']}"
headers["Accept-Language"] = f"{os.environ['Accept-Language']}"
headers["Accept-Encoding"] = f"{os.environ['Accept-Encoding']}"
headers["Content-Type"] = f"{os.environ['Content-Type']}"
headers["Pf-Widget-Version"] = f"{os.environ['Pf-Widget-Version']}"
headers["Content-Length"] = f"{os.environ['Content-Length']}"
headers["Origin"] = f"{os.environ['Origin']}"
headers["Connection"] = f"{os.environ['Connection']}"
headers["Referer"] = f"{os.environ['Referer']}"
headers["Sec-Fetch-Dest"] = f"{os.environ['Sec-Fetch-Dest']}"
headers["Sec-Fetch-Mode"] = f"{os.environ['Sec-Fetch-Mode']}"
headers["Sec-Fetch-Site"] = f"{os.environ['Sec-Fetch-Site']}"
# print(headers)
# Get proxy servers IPs
proxy_ips = find_proxy.get_proxy_ip()
# print(proxy_ips)
def set_payload():
    # Get data from json.file
    data = {}
    # Opening JSON file
    with open('json.file') as json_file:
        data = json.load(json_file)
    payload_content = []
    payload = string.ascii_letters
    for i in payload:
        payload_content.append(i)
    random.shuffle(payload_content)
    payload_content = "".join(payload_content)[:5]
    # print(payload_content)
    # Change email
    data['inputs']["email"] = payload_content + payload_content[::-1][2:4] + "@gmail.com"
    data['visitor_token'] = data['visitor_token'][:-2] + str(round(random.random() * 9))
    # print(data)
    data = json.dumps(data).encode('utf-8')
    # print(data)
    return data
def start_to_connect(headers, data, proxy_ips):
    ip = random.choice(proxy_ips)
    print('Use', ip)
    r = requests.post(url, headers=headers, data=data, proxies={'http': ip, 'https': ip}, timeout=10)
def main():
    while True:
        data = {}
        data = set_payload()
        try:
            info("Start attack: ")
            start_to_connect(headers, data, proxy_ips)
            info("Get responses: ")
            response = r.text
            print(response)
            # Don't log the message larger than 1000 characters
            if len(response) < 1000:
                with open("discount.txt", "a") as target:
                    target.write(response + "\n")
            if "50% Discount" in response:
                print("Got Good luck!!")
                print(response)
        except:
            pass
main()