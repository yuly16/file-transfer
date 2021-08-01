# reference: https://www.cnblogs.com/xiaokang01/p/9069048.html

from socket import *
import os
import json
import struct
buffer_size = 1024
def main():

    tcp_server = socket(AF_INET, SOCK_STREAM)

    tcp_server.bind(('127.0.0.1', 8000))
    tcp_server.listen(5)
    conn, addr = tcp_server.accept()
    print("successfully connect to client.")
    filename = "./mypicture.jpg"
    filesize = os.path.getsize(filename)

    file_header = {
        "filename": filename,
        "filesize": filesize
    }

    file_header_string = json.dumps(file_header)
    file_header_len = struct.pack("i", len(file_header_string))
    conn.send(file_header_len)
    conn.send(file_header_string.encode("UTF-8"))
    f = open(filename, "rb")
    conn.sendall(f.read())
    f.close()
    
if __name__ == "__main__":
    main()