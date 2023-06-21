import os
import socket
from collections import defaultdict
from http import HTTPStatus


def get_response_body(client_message, addr):
    response_body = defaultdict(str)
    message_list = client_message.split('\r\n')
    request_info = message_list[0].split()
    response_body['Request Method'] = request_info[0]
    response_body['Request Source'] = addr
    status_code = request_info[1].split('=')
    print(message_list)
    if len(status_code) == 2:
        try:
            status = HTTPStatus(status_code[1])
            response_body['Response Status'] = f'{status.name}, {status.value}'
        except ValueError as e:
            response_body['Response Status'] = '200, OK'
    else:
        response_body['Response Status'] = '200, OK'
    for header in message_list[1:-2]:
        header_info = header.split(': ')
        print(header_info)
        response_body[header_info[0]] = header_info[1]

    return response_body


def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('192.168.1.9', 0))
        s.listen(1)
        print(f'start connection on {s.getsockname()}, pid: {os.getpid()}')
        print(f'server {s}')
        while True:
            conn, addr = s.accept()
            print(f'con = {conn}')
            print(f'Соединение от {addr}')
            while True:
                data = conn.recv(2048)
                if data:
                    message = data.decode('utf-8')
                    print(f'Получено сообщение: \n {message}')
                    response_body = get_response_body(message, addr)

                    headers = {
                        'Content-Type': 'application/json',
                        'Content-Length': len(str(response_body))
                    }
                    body = dict(response_body)
                    print('Ответ клиенту')
                    send_data = {}
                    send_data.update(headers)
                    send_data.update(body)
                    print(send_data)
                    bts = conn.send(str(send_data).encode('utf-8'))
                else:
                    print('Нет сообщения от клиента')
                    break
            print('Закрываю соединение')
            s.close()


if __name__ == '__main__':
    echo_server()
