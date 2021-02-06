import urllib.request
import json

ID = ['papago_id']

id_num = 0
client_id, client_secret = ID[id_num]

def change_id():
    global id_num
    global client_id, client_secret

    id_num = (id_num+1) % len(ID)
    client_id, client_secret = ID[id_num]


def api_request(string, transTo):
    encText = urllib.parse.quote(string)
    if transTo == 'kor':
        data = "source=en&target=ko&text=" + encText + "&honorific=true"
    elif transTo == 'eng':
        data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()

        res = json.loads(response_body.decode('utf-8'))
        return res['message']['result']['translatedText']

    else:
        return 'translate error'


def translate(string, transTo):
    for i in range(2):
        try:
            translated_str = api_request(string, transTo)
            return translated_str

        except Exception as e:
            change_id()

    return 'api error'


def kor(string):
    return translate(string, 'kor')

def eng(string):
    return translate(string, 'eng')

