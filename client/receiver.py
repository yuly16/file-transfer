from socket import *
import struct
buffer_size = 1024
import os
import json
def main():
    f = open("./config", "r")
    config = f.readlines()
    f.close()
    ip_address = config[0].strip()
    port = int(config[1].strip())
    print("ready to connect server.....")
    try:
        tcp_server = socket(AF_INET, SOCK_STREAM)
        tcp_server.connect((ip_address, port))
        print("connect success!")
    except error:
        print("can't connect server.")
        os.system("pause")
        exit(1)

    try:
        data = tcp_server.recv(10)
        head_len = struct.unpack("i", data)[0]
        print(head_len)
        data = tcp_server.recv(head_len)
        file_header = json.loads(data.decode("UTF-8"))
        print(file_header)
        print(file_header["filename"])
        f = open(file_header["filename"], "wb")
        cursor = 0
        while cursor < file_header["filesize"]:
            data = tcp_server.recv(buffer_size)
            f.write(data)
            cursor += buffer_size
            print("progress:" + str(cursor/file_header["filesize"]))
        f.close()
        print("file receive success!")
    except error:
        print("network is disconnected!")
        os.system("pause")
        exit(1)
if __name__ == "__main__":
    main()