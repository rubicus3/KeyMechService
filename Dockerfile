FROM python:3.13-bookworm
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
EXPOSE 8000
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
