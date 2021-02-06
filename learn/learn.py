import pickle
from application.default_commands import default
from learn.google_spread import sheetAppend, sheetChange, sheetDelete

learn_notice = 'learn notice'

# file save
def save(learnt_data):
    with open('data.pickle', 'wb') as fw:
        pickle.dump(learnt_data, fw)

def load():
    with open('data.pickle', 'rb') as fr:
        return pickle.load(fr)



# learning
def learn(key, reply, sender):
    error_msg = '죄송합니다. 기본 명령어는 가르칠 수 없어요.'
    success_msg = '네! 앞으로 가르쳐 주신 대로 대답할게요!'
    changed_msg = '원래 알던 건 다른 거였는데...앞으론 이렇게 대답할게요!'

    if in_default(key):
        return error_msg

    changed = False
    data = load()

    if key in data:
        changed = True
    data[key] = {'reply': reply, 'register': sender}
    save(data)



    if changed:
        sheetChange(key, reply, sender)
        return changed_msg

    sheetAppend(key, reply, sender)
    return success_msg

def delete(key):
    error_msg = '죄송합니다. 기본 명령어는 잊을 수 없어요.'
    success_msg = '네! 기억 속에서 삭제할게요!'
    fail_msg = '죄송해요...그런 말을 배운 기억이 없어요...'
    
    if in_default(key):
        return error_msg
    
    data = load()
    try:
        del(data[key])
        save(data)
        sheetDelete(key)
        return success_msg

    except KeyError:
        return fail_msg

def say(key):
    data = load()
    if key in data:
        return data[key]['reply']
    return None


# else
def check_register(key):
    default_msg = '이 명령어는 개발자님이 가르쳐 주신 기본 명령어에요!'

    if in_default(key):
        return default_msg

    data = load()
    if key in data:
        register = data[key]['register']
        return '이 말은 ' + register + '님이 가르쳐 주셨어요!'

    else:
        return '아무도 저한테 그런 말은 가르쳐 준 적 없어요...'

def in_default(key):
    temp_data = {'msg': key, 'sender': 'temp_sender_from_learn'}
    if default(temp_data) is not None:
        return True

    elif command(temp_data) is not None:
        return True

    return False

def command(data):
    msg = data['msg']

    if msg == '가르치기':
        return 'intro'

    elif msg[:2] == '배워':
        return 'learn'

    elif msg[:2] == '잊어':
        return 'del'

    elif msg.replace(' ', '')[:5] == '가르친사람':
        return 'reg'

    return None

# 전체 총합
def teach_learn(data):
    msg = data['msg']
    sender = data['sender']

    mode = command(data)

    format_error = '가르치기 형식을 다시 확인해 주세요!'

    if mode == 'intro':
        intro_message = '아래와 같은 방법으로 저를 가르칠 수 있어요!@nm@' \
                        '@nm@배워 /[질문] /[대답]\n' \
                        '잊어 [질문]\n' \
                        '가르친사람 /[질문]' \
                        '@nm@ex) 안다야 배워 /넌 누구니 /저는 안다에요!' \
                        '@nm@*주의사항*\n' \
                        '1. 안다에게 가르친 말은 안다가 초대되어 있는 \'모든 톡방\'에서 작동합니다.\n' \
                        '2. 안다가 배웠던 말을 다시 배우는 경우, 원래 배웠던 말은 잊어버리고 새로 배운 말을 기억합니다.\n' \
                        '3. 안다의 기본 명령어(안녕, 배워 등)은 배우거나 잊게 할 수 없습니다.\n' \
                        '4. 안다에게 가르친 말을 누가 가르쳤는지 누구나 확인할 수 있습니다. 안다에게는 바르고 고운 말만 가르쳐주세요!'

        return intro_message

    elif mode == 'learn':
        try:
            strings = msg.split('/')

            key = strings[1].strip()
            reply = strings[2].strip()

            if reply == '':
                return format_error


            return learn(key, reply, sender)


        except IndexError:
            return format_error

    elif mode == 'del':
        try:
            strings = msg.split('/')
            key = strings[1].strip()

            return delete(key)

        except IndexError:
            return format_error


    elif mode == 'reg':
        try:
            strings = msg.split('/')
            key = strings[1].strip()

            return check_register(key)

        except IndexError:
            return format_error



    else:
        return '오류 발생. 개발자에게 문의해 주세요.'


