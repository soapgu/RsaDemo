from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse,FileResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP,AES
import os
import time

app = FastAPI()
recipient_key = RSA.import_key(open("publicKey").read())
max_plain_text_len = recipient_key.size_in_bytes() - 42 
cipher_rsa = PKCS1_OAEP.new(recipient_key)
private_key = RSA.import_key(open("privateKey").read())
decipher_rsa = PKCS1_OAEP.new(private_key)
data_length = private_key.size_in_bytes()

BLOCK_SIZE = 16 * 1024
aes_key = open("aes_key","rb").read()
aes_iv = open("aes_iv","rb").read()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    print(file.filename)
    start_time = time.time()
    save_path = os.path.join(os.getcwd(), "downloads" , file.filename)
    print(save_path)
    with open(save_path, 'wb') as out_file:
        while content := await file.read(max_plain_text_len):  # 每次读取RSA加密最大值
            encrypted_chunk = cipher_rsa.encrypt(content)
            out_file.write(encrypted_chunk)
    end_time = time.time()
    run_time = end_time - start_time
    print(f"加密运行时间: {run_time} 秒")
    return {"filename": file.filename}

@app.get("/download")
async def get_file( file: str ):
    download_path = os.path.join(os.getcwd(), "downloads" , file)
    def iterfile():
        with open(download_path, 'rb') as in_file:
            while content := in_file.read(data_length):  # 每次读取数据
            #print("---read data---")
                decrypted_chunk = decipher_rsa.decrypt(content)
                yield decrypted_chunk
    headers = {
       "Content-Disposition": f"attachment; filename={file}",  # 设置下载文件名
    }
    return StreamingResponse(iterfile(), headers=headers , media_type="application/octet-stream")

@app.post("/aes/upload")
async def ase_upload( file: UploadFile ):
    print(file.filename)
    start_time = time.time()
    save_path = os.path.join(os.getcwd(), "downloads" , file.filename)
    cipher_aes = AES.new(aes_key, AES.MODE_CTR,nonce=aes_iv)
    with open(save_path, 'wb') as out_file:
        while content := await file.read(BLOCK_SIZE):  # 每次读取RSA加密最大值
            encrypted_chunk = cipher_aes.encrypt(content)
            out_file.write(encrypted_chunk)
    end_time = time.time()
    run_time = end_time - start_time
    print(f"AES加密运行时间: {run_time} 秒")
    return {"filename": file.filename}

@app.get("/aes/download")
async def ase_get_file( file: str ):
    download_path = os.path.join(os.getcwd(), "downloads" , file)
    def iterfileaes():
        start_time = time.time()
        count = 0
        decipher_aes = AES.new(aes_key, AES.MODE_CTR,nonce=aes_iv)
        with open(download_path, 'rb') as in_file:
            while content := in_file.read(BLOCK_SIZE):  # 每次读取数据
                decrypted_chunk = decipher_aes.decrypt(content)
                count = count + 1
                #print(f"计数{count},length:{len(decrypted_chunk)}")
                yield decrypted_chunk
        end_time = time.time()
        run_time = end_time - start_time
        print(f"AES解密运行时间: {run_time} 秒")
    headers = {
       "Content-Disposition": f"attachment; filename={file}",  # 设置下载文件名
    }
    return StreamingResponse(iterfileaes(), headers=headers , media_type="application/octet-stream")
