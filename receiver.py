import socket
import os
import hidden
import struct

download_folder = os.getcwd() + "/" + "files"
print(hidden.DESKTOP, hidden.PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((hidden.DESKTOP, hidden.PORT))

s.settimeout(5)
s.listen()

imgs = 0
print("Running")
while True:
    try: 
        conn, address = s.accept()
    except TimeoutError:
        print("No connections within 5 seconds")
        break

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
    imgs += 1
    if not imgs % 100: print(f"Images Received: {imgs}")

    conn.close()

