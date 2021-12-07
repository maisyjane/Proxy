FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y python3-pip python3
WORKDIR /app
RUN pip3 install Flask
RUN pip3 install requests
COPY ./src /app
EXPOSE 5001
ENTRYPOINT ["python3"]
CMD ["app.py"]