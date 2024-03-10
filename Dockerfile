FROM python:3.13.0a4-alpine3.19
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY downloader.py downloader.py
CMD ["python", "downloader.py"]