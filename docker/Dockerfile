FROM python:3

WORKDIR /var/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /var/src

CMD [ "python3", "-m", "http.server", "8000" ]
