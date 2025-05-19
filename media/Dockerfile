FROM python:3.13-bookworm
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code/media
EXPOSE 8000
CMD ["fastapi", "run", "media/main.py", "--port", "8000"]
