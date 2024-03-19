from itertools import cycle
import os
import argparse
import time

def xor_cipher(text, key):
    #encrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, cycle(key)))
    encrypted_text = bytes([(c^k) for c, k in zip(text, cycle(key))])
    return encrypted_text


parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-f', '--input-file', required=True, help='The input file')

args = parser.parse_args()

print(f"Input file: {args.input_file}")

ENCRYPT_SIZE = 1024
download_path = args.input_file

#print(f"key lenght:{len(binascii.unhexlify(keys))}")

in_file_length = os.path.getsize(download_path)
print(in_file_length)
start_time = time.time()
count = 0
with open(download_path, 'rb') as in_file:
    # read 1k data
    head = in_file.read(ENCRYPT_SIZE)
    # aes encrypt and write
    crypted_chunk = xor_cipher(head,b"shgbit")
    

with open(download_path, 'r+b') as out_file:
    out_file.seek(0)
    out_file.write(crypted_chunk)    

end_time = time.time()
run_time = end_time - start_time
print(f"按位异或加(解)密运行时间: {run_time} 秒")