import requests
from ast import literal_eval
from api.papago import kor, eng


def api_answer(data):
    msg = data['msg']
    sender = data['sender']
    isGroupChat = data['isGroupChat']
    if isGroupChat:
        room = '[' + data['room'] + ']'
        sender += room

    url = "http://api.brainshop.ai/get"

    querystring = {"bid": "bid", "key": "key", "uid": sender, "msg": msg}

    response = requests.request("GET", url, params=querystring)
    reply = literal_eval(response.text)['cnt']

    return reply




def ask(input_data):
    msg = input_data['msg']
    data = input_data.copy()

    eng_msg = eng(msg)
    if eng_msg == 'api error':
        return '당일 데이터 요청 가능량 한계에 도달하였습니다. 개발자에게 문의해 주세요.'

    data['msg'] = eng_msg
    eng_rep = api_answer(data)

    reply = kor(eng_rep)
    if reply == 'api error':
        return '당일 데이터 요청 가능량 한계에 도달하였습니다. 개발자에게 문의해 주세요.'

    return reply





