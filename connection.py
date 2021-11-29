import random
import requests
from pwn import *
def start_to_connect(url, headers, data, proxy_ips, p):
    ip = random.choice(proxy_ips)
    p.status(f'Use proxy IP: {ip}')
    response = requests.post(url, headers=headers, data=data, proxies={'http': ip, 'https': ip}, timeout=10)
    return response