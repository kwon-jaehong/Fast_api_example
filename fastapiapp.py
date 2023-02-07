from fastapi import FastAPI, Request,Form,UploadFile,HTTPException,status
from typing import Union
import uvicorn

app = FastAPI()
@app.post("/")
async def upload( request: Request,filename: str = Form(...), filedata: Union[str, UploadFile] = Form(...)):
    # ...는 무조건 파라미터값이 필요하다라는 뜻임
    # filedata: Union[str, UploadFile]는 str타입과 UploadFile두개다 볼수 있다
    try:
        if "UploadFile" in str(type(filedata)):
            print("파일임",filedata.filename)
        elif type(filedata) == str:
            print("문자열기반")
        else:
            raise
    except:
        print("받은 파일 알수 없음")
        
        
    return {"message": f"Successfuly uploaded "} 

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=32220)