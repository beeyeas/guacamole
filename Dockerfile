FROM ubuntu:latest
MAINTAINER beeyeas "beeyeas@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN pip install psutil
RUN mkdir /app
COPY guacomole.py /app/guacomole.py
COPY requirements.txt /app/requirements.txt
RUN chmod +x /app/guacomole.py
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["guacomole.py"]