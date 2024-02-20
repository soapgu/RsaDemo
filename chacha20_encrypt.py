from Crypto.Cipher import ChaCha20
import binascii
import argparse
import os
import time

parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-f', '--input-file', required=True, help='The input file')

args = parser.parse_args()

download_path = args.input_file
output_filename = f"encrypt_{args.input_file}"

print(f"Input file: {args.input_file}")
start_time = time.time()

key = 'fd1c04e1e5d6f545b11a8320a8197a9763ca9b65cfc22ae2477ea047f01a7350';
nonce = '21b7653f2ca8cc35'
BLOCK_SIZE = 8 * 1024
cipher = ChaCha20.new(key=binascii.unhexlify(key),nonce=binascii.unhexlify(nonce))

with open(download_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(BLOCK_SIZE):
            crypted_chunk = cipher.encrypt(content)
            out_file.write(crypted_chunk)

out_file_length = os.path.getsize(output_filename)
print(f"encrypt ok,size {out_file_length}")
end_time = time.time()
run_time = end_time - start_time
print(f"ChaCha20加密运行时间: {run_time} 秒")