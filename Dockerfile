FROM tensorflow/tensorflow:1.12.0-gpu-py3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt update && apt install -y libsm6 libxext6
RUN apt-get install -y libfontconfig1 libxrender1
EXPOSE 5000
CMD python3 ./app.py