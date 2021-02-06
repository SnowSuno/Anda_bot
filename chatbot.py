from application.functions import rawMsg
from learn.learn import command, teach_learn, say
from application.default_commands import default
from ai.anda_ai import ask

TESTMODE = True
LEARN = True
SAY_LEARNT_MSG = True
AI_ANSWER = True


def chatbot(input_data):  # room, msg, sender, isGroupChat = input_data
    data = rawMsg(input_data)
    #차단 기능
    if data['sender'] == 'banned_by_abuse':
        return '개발자에 의해 직접 차단되었습니다. 안다에게는 바르고 고운 말을 사용해 주세요.'
    if data['sender'] == 'banned_by_overload':
        return '개발자에 의해 직접 차단되었습니다. 과도하게 많은 메시지를 보내지 말아주세요.'

    # 서버 테스트
    if TESTMODE:
        if data['msg'] == 'servertest':
            return 'online server running'

        if data['msg'] == "test":
            return "room : "+data[0]+", msg : "+data[1]+", sender : "+data[2]

    # 기본 명령어
    if default(data) is not None:
        return default(data)

    # 가르치기 기능
    # 배워 /[이런 말을 했을때] /[이런 말을 해요]
    # 잊어 /[잊을 내용]
    # 가르친사람 /[내용]
    if command(data) is not None:
        if LEARN:
            return teach_learn(data)

        else:
            return '가르치기 기능은 현재 비활성화 되었습니다ㅠㅠ'

    if SAY_LEARNT_MSG:
        reply = say(data['msg'])

        if reply is not None:
            return reply


    
    # 대화하기 기능

    ans = '죄송합니다. 대화하기 기능은 현재 비활성화 되었습니다ㅠㅠ'
    if AI_ANSWER:
        ans = ask(input_data)
    return ans
