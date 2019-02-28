FROM python:3.6-slim

ADD ./requirements.txt /root/requirements.txt
ADD ./main.py /root/main.py
ADD ./model.py /root/model.py
ADD ./service.py /root/service.py
ADD ./db.py /root/db.py

WORKDIR /root

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

EXPOSE 5000
