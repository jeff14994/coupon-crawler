# Coupon Crawler
## Why writing this repo? 
- Hope to increase the opportunity to get the 50% off coupon
<img src="https://github.com/jeff14994/coupon-crawler/blob/main/resources/origin.gif" width="400" height="700"/>

## Demo: 
- Obtain coupons automatically 
![alt-text](https://github.com/jeff14994/coupon-crawler/blob/main/resources/demo.gif)

## Observe the packets with Burp Suite
- headers:
    - <img src="https://github.com/jeff14994/coupon-crawler/blob/main/resources/packets.png" width="200" height="350"/>
## Bypass the check
- Use [free proxies](https://free-proxy-list.net/) to bypass
## Packages to install
- `pwntools`
- `requests`
- `BeautifulSoup`
- `dotenv`
## How to run the script?
- Clone this repo to local
    - `git clone https://github.com/jeff14994/coupon-crawler.git` 
- Step into the directory
    - `cd coupon-crawler`
- Create an `.env` with the [env_example](https://github.com/jeff14994/coupon-crawler/blob/main/env_example) and change the file name to `.env`
- run `main.py`
