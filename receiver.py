import socket
import os
import hidden
import struct

download_folder = os.getcwd() + "/" + "files"
print(hidden.DESKTOP, hidden.PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((hidden.DESKTOP, hidden.PORT))

s.listen()

print("Running")
while True:
    conn, address = s.accept()

    file_info = conn.recv(struct.calcsize('!H'))
    file_name_len = struct.unpack('!H', file_info)[0]
    file_info = conn.recv(file_name_len)
    file_name = file_info.decode('utf-8')
    file_info = conn.recv(struct.calcsize('!Q'))
    file_size = struct.unpack('!Q', file_info)[0]
    file_contents = b""
     
    while len(file_contents) < file_size:
        chunk = conn.recv(file_size - len(file_contents))
        if not chunk:
            break

        file_contents += chunk


    with open(os.path.join(download_folder, file_name), 'wb') as f:
        f.write(file_contents)

    conn.close()

