from Crypto.Cipher import ChaCha20
import binascii
import argparse
import os
import time

from Crypto.Cipher import ChaCha20
import binascii
import argparse
import os
import time

parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-f', '--input-file', required=True, help='The input file')

args = parser.parse_args()
download_path = args.input_file
output_filename = f"restore_{download_path}"
start_time = time.time()

key = 'fd1c04e1e5d6f545b11a8320a8197a9763ca9b65cfc22ae2477ea047f01a7350'
nonce = '21b7653f2ca8cc35'
BLOCK_SIZE = 8 * 1024
cipher = ChaCha20.new(key=binascii.unhexlify(key),nonce=binascii.unhexlify(nonce))

with open(download_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(BLOCK_SIZE):  # 每次读取数据
            decrypted_chunk = cipher.decrypt(content)
            out_file.write(decrypted_chunk)

end_time = time.time()
run_time = end_time - start_time
print(f"ChaCha20解密{output_filename}，运行时间: {run_time} 秒")
