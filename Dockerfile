FROM ubuntu:latest
ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ="Asia/Kolkata"
WORKDIR /app
RUN apt update 
RUN apt upgrade -y
RUN apt install python wget -y
COPY . .
RUN apt install python3-pip -y
RUN pip install --no-cache-dir -r requirements.txt
CMD ["bash","startup"]
