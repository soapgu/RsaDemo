from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import binascii
import os
import argparse


parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-f', '--input-file', required=True, help='The input file')

args = parser.parse_args()

print(f"Input file: {args.input_file}")

keys = '30980f98296b77f00a55f3c92b35322d898ae2ffcdb906de40336d2cf3d556a0'
iv = 'e5889166bb98ba01e1a6bc9b32dbf3e6'
download_path = args.input_file
output_filename = f"encrypt_{args.input_file}"

#print(f"key lenght:{len(binascii.unhexlify(keys))}")

cipher = AES.new(binascii.unhexlify(keys), AES.MODE_CBC,iv=binascii.unhexlify(iv))
in_file_length = os.path.getsize(download_path)
block_count = in_file_length / AES.block_size
print(in_file_length)

count = 0
with open(download_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(AES.block_size):
            if(len(content) < AES.block_size):
                content = pad(content,AES.block_size)
                hex_string = binascii.hexlify(content).decode()
                print(f"pad content:{hex_string}")
            crypted_chunk = cipher.encrypt(content)
            out_file.write(crypted_chunk)
            #print(f"计数{count}/总数{block_count},length:{len(crypted_chunk)}")

out_file_length = os.path.getsize(output_filename)
print(f"encrypt ok,size {out_file_length}")