from pwn import *
from find_proxy import get_proxy_ip
from headers import create_header
from set_payload import set_payload
from connection import start_to_connect
context.log_level = 'info'
# Two steps
# Step 1: Spin the wheel and get the coupon
# Step 2: Check the coupon to see if it's 50% discount
url = f"{os.environ['URL']}"
headers = create_header()
# info(headers)
# Get proxy servers IPs
proxy_ips = get_proxy_ip()
# info(proxy_ips)
def main():
    while True:
        p = log.progress("Start digging coupon: \n")
        data = {}
        data = set_payload()
        try:
            response = start_to_connect(url, headers, data, proxy_ips, p)
            # p.success("Get responses: ")
            result = response.text
            p.success(result)
            # Don't log the message larger than 1000 chardacters
            if len(response) < 1000:
                with open("discount.txt", "a") as target:
                    target.write(response + "\n")
            if "50% Discount" in response:
                info("Got Good luck!!")
                info(response)
        except:
            pass
main()