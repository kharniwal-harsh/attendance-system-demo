FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y cmake build-essential libsm6 libxext6 libxrender-dev \
    libgtk-3-dev libboost-python-dev libopenblas-dev liblapack-dev python3-dev \
    libgl1 libglib2.0-0 gcc g++ wget make && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip
# Install Python cmake module and dlib in the same layer
RUN pip install cmake && pip install dlib
# Now install the rest of your requirements (excluding dlib)
RUN pip install --no-deps -r requirements.txt

CMD ["gunicorn", "app:app"]