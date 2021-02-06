from flask import Flask
from flask import request
from chatbot import chatbot

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    try:
        room = request.form['room']
        msg = request.form['msg']
        sender = request.form['sender']
        isGroupChat = request.form['isGroupChat']
        input_data = {'room': room, 'msg': msg, 'sender': sender, 'isGroupChat': isGroupChat}
        print(sender + ' : ' + msg)

        result = chatbot(input_data)
        print(result)
        result = result.replace('\n', '$$$')

        return result
    except Exception as e:
        error_msg = '[Error] ' + str(e)
        print(error_msg)
        return error_msg


if __name__ == "__main__":
    app.run('internal_ip_address', port='internal_port', debug=True)
