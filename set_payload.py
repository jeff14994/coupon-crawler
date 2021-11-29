import json
import random
import string
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