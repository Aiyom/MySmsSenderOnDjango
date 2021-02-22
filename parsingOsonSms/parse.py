import requests


def logining(phonenumber, msg, params=None):

    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 ',
               'accept': '*/*'}
    datas = {
        'email': 'Your log in',
        'password': 'Your password'
    }

    s = requests.Session()
    log = s.post('https://cab.osonsms.com/login', data=datas, headers=HEADERS, params=params)
    if log:
        print('success')
    else:
        print('error')

    datas2 = {
        'sms_sender': 'MOI',
        'phonenumbers': phonenumber,
        'message': msg,
        'login': 'moi'
    }
    send = s.post("https://cab.osonsms.com/sms-rassylka/fast-send", data=datas2, headers=HEADERS, params=params)
    if send:
        print(send.status_code)
        print('success')
    else:
        print(send.status_code)
        print('error')
