from Crypto.Random import get_random_bytes
import binascii
import os
import argparse
import time


parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-f', '--input-file', required=True, help='The input file')

args = parser.parse_args()

print(f"Input file: {args.input_file}")

ENCRYPT_SIZE = 1024
BLOCK_SIZE = 16 * 1024
download_path = args.input_file
output_filename = f"encrypt_{args.input_file}"

#print(f"key lenght:{len(binascii.unhexlify(keys))}")

in_file_length = os.path.getsize(download_path)
block_count = in_file_length / BLOCK_SIZE
print(in_file_length)
start_time = time.time()
count = 0
with open(download_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        # 1. write mess 1k data first
        out_file.write( get_random_bytes(1024) )
        # 2. read 1k data
        head = in_file.read(ENCRYPT_SIZE)
        # 3. aes encrypt and write
        #hex_string = binascii.hexlify(head).decode()
        #print(f"head content:{hex_string}")
        crypted_chunk = bytes([~byte & 0xFF for byte in head])
        out_file.write(crypted_chunk)
        # 4. copy other part file
        head_time = time.time() - start_time
        print(f"加密头时间: {head_time} 秒")
        while content := in_file.read(BLOCK_SIZE):
            out_file.write(content)

out_file_length = os.path.getsize(output_filename)
print(f"encrypt ok,size {out_file_length}")
end_time = time.time()
run_time = end_time - start_time
print(f"按位取反加密运行时间: {run_time} 秒")