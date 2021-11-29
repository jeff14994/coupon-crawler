import requests
from bs4 import BeautifulSoup
def get_proxy_ip():
    url = "https://free-proxy-list.net/"
    # 發起請求
    response = requests.get(url)
    # 剖析
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    # 使用 class 去取 table
    table = soup.find("table", {"class": "table table-striped table-bordered"})
    # 將該table 所有 td tag 取出來
    # print(table)
    all_proxy = table.findChildren('tr',recursive=True)
    # print(all_proxy)
    # 將所有 IP 變成 list
    all_ip = []
    for i in range(len(all_proxy)):
        try:
            # 去除第一個欄位
            if all_proxy[i].td == None:
                continue
            # 將所有 td tag 取出來 [:2] 表示取 td tag list 的前兩個元素（即 IP 與 port）
            all_list = all_proxy[i].findChildren('td',recursive=True)[:2] 
            # print(all_list)
            # 將個別 ip:port 綁在一起成字串
            ip = ""
            for i in range(len(all_list)):
                ip += str(all_list[i].text)
                # 中間加 ":"
                if(i == 0):
                    ip += ":"
            all_ip.append(ip)
        except:
            pass
    # print(all_ip)
    return all_ip
if __name__ == "__main__":
    proxy_ips = get_proxy_ip()
    print(f"Obtain IP numbers: {len(proxy_ips)}")
