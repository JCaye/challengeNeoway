FROM python:3.6-slim

ADD ./requirements.txt /root/requirements.txt
ADD ./app/main.py /root/main.py
ADD ./app/model.py /root/model.py
ADD ./app/service.py /root/service.py
ADD ./app/db.py /root/db.py

WORKDIR /root

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

EXPOSE 5000
