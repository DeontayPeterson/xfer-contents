import socket
import os
import hidden
import struct

file_dir = os.getcwd() + "/" + "files" 
all_files = os.listdir(file_dir)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hidden.DESKTOP, hidden.PORT))

for filename in all_files:
    file_path = os.path.join(file_dir, filename)

    with open(file_path, 'rb') as f:
        file_bytes = f.read()

    file_name_b = filename.encode('utf-8')
    file_name_len = len(file_name_b)
    file_size = len(file_bytes)
    s.sendall(struct.pack('!H%dsQ%ds' % (file_name_len, file_size), file_name_len, \
                          file_name_b, file_size, file_bytes ))

s.close()

    

