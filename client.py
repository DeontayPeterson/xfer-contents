import socket
import os

# Name of directory that contains files you want trasnfered.
dir_name = 'files'

cwd = os.getcwd()
target_dir_path = cwd + "\\" + dir_name # Replace \\ with / on pi.
contents = os.listdir(target_dir_path)
print(contents)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

