FROM python:3.8.3-alpine

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip 
RUN pip install --user -r requirements.txt

ENV PATH="$PATH:$HOME/.local/bin"


CMD ["python", "app.py"]