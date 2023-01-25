import uvicorn
from fastapi import FastAPI



# @app.get("/date")
# def index():
#     return {"name":"재홍!"}

BOOKS = {
    'book_1':{"title":"title one","author":"author one"},
    'book_2':{"title":"title two","author":"author two"},
    'book_3':{"title":"title three","author":"author three"},
    'book_4':{"title":"title four","author":"author four"},
    'book_5':{"title":"title five","author":"author five"},
}

def create_app():
    '''
    앱 생성
    '''
    
    ## config 파싱 or 생성
    
    ## fastapi 앱 생성
    app = FastAPI()
    
    
    ## 디비 연결 또는 초기화
    
    ## 미들웨어 정의
    
    ## 라우터 정의

    
    return app   

app = create_app()
if "__main__" == __name__:
    uvicorn.run("main:app",host="0.0.0.0",port=31123)
 


