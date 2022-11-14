FROM python:3.10-alpine3.16

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && pipenv install --system --deploy

COPY . .

CMD ["python", "/app/src/presentation/worker.py"]
