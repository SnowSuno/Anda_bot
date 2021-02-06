import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import threading

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'json_file'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)


spreadsheet_url = 'https://docs.google.com/spreadsheets/d/something'


doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('Learn')


def append_thread(key, reply, sender):
    now = time.localtime()
    reg_time = "%04d/%02d/%02d %02d:%02d:%02d" % (
    now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    worksheet.insert_row(['', reg_time, sender, key, reply], 2)

    worksheet.format('A2:E2', {'textFormat': {"foregroundColor": {"red": 0, "green": 0, "blue": 0}}})


def sheetAppend(key, reply, sender):
    append = threading.Thread(target=append_thread, args=(key, reply, sender))
    append.start()



def delete_thread(key):
    row = str(worksheet.find(key).row)
    cells = 'A' + row + ':E' + row
    worksheet.format(cells, {'textFormat': {"foregroundColor": {"red": 0.8, "green": 0.8, "blue": 0.8}}})

def sheetDelete(key):
    delete = threading.Thread(target=delete_thread, args=(key,))
    delete.start()



def change_thread(key, reply, sender):
    delete_thread(key)
    append_thread(key, reply, sender)

def sheetChange(key, reply, sender):
    change = threading.Thread(target=change_thread, args=(key, reply, sender))
    change.start()




