import binascii
import os
import argparse
import time

parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-f', '--input-file', required=True, help='The input file')
args = parser.parse_args()
print(f"Input file: {args.input_file}")
start_time = time.time()
download_path = args.input_file
output_filename = f"restore_{download_path}"


in_file_length = os.path.getsize(download_path)
BLOCK_SIZE = 8 * 1024
block_count = in_file_length / BLOCK_SIZE

count = 0
with open(download_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        # 1. skip first 1024 size
        in_file.read(1024)
        # 2. read encrypt head data,if data < 1K
        ENCRYPT_SIZE = 1024
        # if head data > 1K
        head = in_file.read(ENCRYPT_SIZE)
        # 3. aes decrypt header and write
        decrypted_chunk = bytes([~byte & 0xFF for byte in head])
        out_file.write(decrypted_chunk)
        head_time = time.time() - start_time
        print(f"解密头时间: {head_time} 秒")
        # 4 copy other data
        while content := in_file.read(BLOCK_SIZE):  # 每次读取数据
            out_file.write(content)            
print(f"decrypt {output_filename} OK")

out_file_length = os.path.getsize(output_filename)
print(f"in file size:{in_file_length},out file size{out_file_length}")
end_time = time.time()
run_time = end_time - start_time
print(f"按位取反解密运行时间: {run_time} 秒")