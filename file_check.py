import hashlib
import os.path
from sys import argv


def hash_file(f_name, algorithm):
    alg_dict = {'md5': hashlib.md5(), 'sha1': hashlib.sha1(), 'sha256': hashlib.sha256()}
    for key in alg_dict:
        if algorithm == key:
            h = alg_dict[key]

    with open(f_name, 'rb') as f_handle:
        chunk = 0
        while chunk != b'':
            chunk = f_handle.read(1024)
            h.update(chunk)

    return h.hexdigest()


script, input_path, dir_path = argv
print(input_path, dir_path)

with open(input_path, 'r') as file_list:
    for line in file_list:
        data = line.split()
        print(data[0])
        file_path = dir_path + '\\' + data[0]
        print(file_path)
        if os.path.exists(file_path):
            if hash_file(file_path, data[1].lower()) == data[2].lower():
                print(data[0], 'OK')
            else:
                print(data[0], 'FAIL')
        else:
            print(data[0], 'NOT FOUND')
