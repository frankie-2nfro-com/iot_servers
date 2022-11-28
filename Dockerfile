FROM python:3.8-slim

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*
#COPY ./req.txt /req.txt
COPY ./src /src

RUN pip3 install --no-cache-dir -r /src/req.txt

#CMD ["python3", "/src/main.py"]
ENTRYPOINT ["python3", "-u", "/src/main.py"]

EXPOSE 8080