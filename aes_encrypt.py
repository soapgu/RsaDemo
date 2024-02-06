from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import binascii
import os
import argparse
import time


parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-f', '--input-file', required=True, help='The input file')

args = parser.parse_args()

print(f"Input file: {args.input_file}")

keys = '30980f98296b77f00a55f3c92b35322d898ae2ffcdb906de40336d2cf3d556a0'
iv = 'e5889166bb98ba01e1a6bc9b32dbf3e6'
BLOCK_SIZE = AES.block_size * 1024
download_path = args.input_file
output_filename = f"encrypt_{args.input_file}"

#print(f"key lenght:{len(binascii.unhexlify(keys))}")

cipher = AES.new(binascii.unhexlify(keys), AES.MODE_CBC,iv=binascii.unhexlify(iv))
in_file_length = os.path.getsize(download_path)
block_count = in_file_length / BLOCK_SIZE
print(in_file_length)
start_time = time.time()
count = 0
with open(download_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while True:
            content = in_file.read(BLOCK_SIZE)
            end = len(content) < BLOCK_SIZE
            if(end):
                content = pad(content,AES.block_size)
                hex_string = binascii.hexlify(content).decode()
                print(f"pad content:{hex_string}")
            crypted_chunk = cipher.encrypt(content)
            out_file.write(crypted_chunk)
            if(end):
                break
            #print(f"计数{count}/总数{block_count},length:{len(crypted_chunk)}")

out_file_length = os.path.getsize(output_filename)
print(f"encrypt ok,size {out_file_length}")
end_time = time.time()
run_time = end_time - start_time
print(f"AES加密运行时间: {run_time} 秒")