FAST API 연습

------
pip install fastapi 'uvicorn[standard]' requests
------


FAST API
- 성능이 빠름
- 스웨거라는 문서제공이 편리함






------------------------------------

uvicorn(파이썬 웹서버) 설치
-> 장고나 플라스크 같은 경우 자체적인 WSGI,웹서버를 구성해서 페이지를 띄어준다.


아래 사이트에서
https://www.toptal.com/flask/flask-production-recipes


Gunicorn을 사용한 자체 호스팅 Flask 애플리케이션. Flask에는 웹 서버가 내장되어 있지만 모두 알고 있듯이 프로덕션에는 적합하지 않으며 WSGI 프로토콜을 통해 Flask와 통신할 수 있는 실제 웹 서버 뒤에 배치해야 합니다. 이를 위한 일반적인 선택은 Python WSGI HTTP 서버인 Gunicorn 입니다.
Nginx 로 정적 파일 제공 및 프록시 요청 . Gunicorn은 HTTP 웹 서버이기는 하지만 웹과 마주하기에는 적합하지 않은 애플리케이션 서버입니다. 그렇기 때문에 Nginx가 리버스 프록시로 필요하고 정적 파일을 제공해야 합니다. 애플리케이션을 여러 서버로 확장해야 하는 경우 Nginx가 로드 밸런싱도 처리합니다.


fastapi pytorch 모델 서빙하기 + 마이크로 배치
https://velog.io/@rapidrabbit76/FastAPI%EB%A1%9C-Model-serving-%ED%95%98%EA%B8%B0-with-Micro-Batching
https://velog.io/@timointhebush/FastAPI%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-PyTorch%EB%A5%BC-REST-API%EB%A1%9C-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0

구니콘+uvicorn 합쳐서 동시성 + 병렬성
https://medium.com/@mingc.me/deploying-pytorch-model-to-production-with-fastapi-in-cuda-supported-docker-c161cca68bb8
https://roseline.oopy.io/dev/gunicorn-nginx-fastapi-deploy-on-lightsail


하지만 쿠버네티스같은 경우 이문서를 읽어보자
https://jonnung.dev/python/2021/10/24/asgi-uvicorn-with-guicorn/#gsc.tab=0
쿠버네티스에서 구성한다면, 이미 uvicorn이 단일 

-----------------------------------
FastAPI 실행 명령어는 
-> uvicorn 파일이름:앱 객체 
uvicorn ex1:app 

uvicorn main:app --reload --host=0.0.0.0 --port=8000
-> reload는 코드 변경시 자동으로 저장되어 재시작되는 플래그

curl 확인
curl http://localhost:32210/date

--------------------------------------------------
docker build -t fastapi:0.1 .
docker run -d -it --ipc=host -p 5000:5000 fastapi:0.1










