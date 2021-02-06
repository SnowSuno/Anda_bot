
def rawMsg(input_data):
    msg = input_data['msg']
    text = msg[2:].lstrip()
    
    if text != '':
        if text[0] == '야':
            text = text[1:].lstrip()
    else:
        input_data['msg'] = '소개'

    input_data['msg'] = text
    return input_data

