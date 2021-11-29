import os
from dotenv import load_dotenv
load_dotenv()
def create_header():
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
    return headers
if __name__ == "__main__":
    headers = create_header()
    print(f"Headers: ", headers)