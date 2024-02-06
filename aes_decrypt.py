from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii
import os
import argparse
import time

parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-f', '--input-file', required=True, help='The input file')
args = parser.parse_args()
print(f"Input file: {args.input_file}")
start_time = time.time()
keys = '30980f98296b77f00a55f3c92b35322d898ae2ffcdb906de40336d2cf3d556a0'
iv = 'e5889166bb98ba01e1a6bc9b32dbf3e6'
download_path = args.input_file
output_filename = f"restore_{download_path}"


cipher = AES.new(binascii.unhexlify(keys), AES.MODE_CBC,iv=binascii.unhexlify(iv))

in_file_length = os.path.getsize(download_path)
BLOCK_SIZE = AES.block_size * 1024
block_count = in_file_length / BLOCK_SIZE

count = 0
with open(download_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(BLOCK_SIZE):  # 每次读取数据
            count = count + 1
            decrypted_chunk = cipher.decrypt(content)
            if(block_count == count):
                print(f"before pad content:{decrypted_chunk}")
                decrypted_chunk = unpad( decrypted_chunk,AES.block_size )
            #hex_string = binascii.hexlify(decrypted_chunk).decode()
            #print(f"content:{hex_string}")
            out_file.write(decrypted_chunk)
            #print(f"计数{count}/总数{block_count},length:{len(decrypted_chunk)}")
print(f"decrypt {output_filename} OK")

out_file_length = os.path.getsize(output_filename)
print(f"in file size:{in_file_length},out file size{out_file_length}")
end_time = time.time()
run_time = end_time - start_time
print(f"AES解密运行时间: {run_time} 秒")