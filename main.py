from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import time

app = FastAPI()
recipient_key = RSA.import_key(open("publicKey").read())
max_plain_text_len = recipient_key.size_in_bytes() - 42 
cipher_rsa = PKCS1_OAEP.new(recipient_key)
private_key = RSA.import_key(open("privateKey").read())
decipher_rsa = PKCS1_OAEP.new(private_key)
data_length = private_key.size_in_bytes()


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
