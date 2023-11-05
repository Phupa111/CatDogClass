FROM python:3.9
WORKDIR /CatDogClass
COPY ./requirements.txt /CatDogClass/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /CatDogClass/requirements.txt

COPY ./app /CatDogClass/app
COPY ./model /CatDogClass/model

ENV PYTHONPATH "${PYTHONPATH}:/CatDogClass"

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]