FROM debian:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt update

RUN python3 --version
RUN pip3 --version

COPY ./ ./

RUN pip3 install python-binance
RUN pip3 install numpy
RUN pip3 install pprintpp
RUN pip3 install websocket

CMD [ "python3", "main.py" ]
