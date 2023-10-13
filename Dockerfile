FROM python:3.9-slim

WORKDIR /app

RUN apt-get update -y \
   && apt-get upgrade -y \
   && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "8000"]