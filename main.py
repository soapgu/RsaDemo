from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    save_path = os.path.join(os.getcwd(), file.filename)
    print(save_path)
    with open(save_path, 'wb') as out_file:
        while content := await file.read(1024 * 8):  # 每次读取8KB数据
            out_file.write(content)
    return {"filename": file.filename}