FROM python:3.10.5-slim-buster
COPY requirements.txt /requirements.txt
COPY client_http.py /client_http.py
COPY tasks.py /tasks.py
RUN pip3 install -r requirements.txt
CMD [ "python", "client_http.py"]