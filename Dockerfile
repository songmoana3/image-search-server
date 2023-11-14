FROM nvcr.io/nvidia/pytorch:21.02-py3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /songmoana
WORKDIR /songmoana
RUN apt update && apt install -y screen libgl1-mesa-glx
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3001", "--reload"]