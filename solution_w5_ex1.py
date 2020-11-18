import socket
import time

class Client:

    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.sock = self._service_connection(self.ip, self.port, self.timeout)

    def put(self, key, value, timestamp=None):
        if timestamp == None:
            timestamp = int(time.time())
        mess = f"put {key} {value} {timestamp}\n"
        result = self._get_server_respond(mess)
        if result.find('ok',0,2) < 0:
            raise ClientError(result)

    def get(self, key):
        mess = f"get {key}\n"
        result = self._get_server_respond(mess)
        if result.find('ok',0,2) >= 0:
            return self._parse_server_respond(result)
        else:
            raise ClientError(result)

    def _get_server_respond(self, message):
        data = ''
        try:
            self.sock.send(message.encode("utf-8"))
            print(f"Отправлен запрос: {ascii(message)}")
            data = self.sock.recv(1024)
            print("Получен ответ: {}".format(ascii(data.decode("utf-8"))))
        except socket.timeout:
            print("send data timeout")
        except socket.error as ex:
            print("send data error:", ex)
        return data.decode("utf-8")

    def _parse_server_respond(self, message):
        # parse message: 'ok\n<useful_mess>\n\n'
        useful_mess = message[3:-2].splitlines()
        if useful_mess == '':
            return {}
        data = {}
        for line in useful_mess:
            if len(line.split()) != 3:
                print(f"Ответ сервера содержит невалидные данные: {line}")
                raise ClientError(message)
            key, val, time = line.split()
            try:
                if key in data:
                    value = data[key]
                    value.append((int(time), float(val)))
                    data[key] = sorted(value, key=lambda item: item[0])
                else:
                    data[key] = [(int(time), float(val))]
            except ValueError:
                print(f"Ответ сервера содержит невалидные данные: {line}")
                raise ClientError(message)
        return data

    def _service_connection(self, ip, port, timeout):
        sock =  socket.create_connection((ip, port), timeout)
        return sock


class ClientError(Exception):
    pass