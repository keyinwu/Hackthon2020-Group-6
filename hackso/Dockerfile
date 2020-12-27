FROM python:3.7
MAINTAINER harumonia
WORKDIR /Project/hackson
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
COPY . .
CMD ["flask", "run"]