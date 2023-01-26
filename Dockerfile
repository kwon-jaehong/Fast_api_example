FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils
WORKDIR app/
COPY . .

# RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
RUN ln -s /usr/bin/python3.7 /usr/bin/python
RUN python get-pip.py 
RUN pip install -r requirements.txt
CMD python -m uvicorn fastapiapp:app --host 0.0.0.0 --port 5000
# uvicorn ex1:app --reload --host=0.0.0.0 --port=32210