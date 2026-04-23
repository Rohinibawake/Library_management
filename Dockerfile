FROM python:3.12
WORKDIR /sample
COPY . .
RUN pip install -r requirements.txt
CMD ["python3","main.py"]


