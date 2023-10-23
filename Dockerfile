FROM python:3.10

# We copy just the requirements.txt first to leverage 
# Docker cache
COPY ./requirements.txt ./requirements.txt


RUN pip install -r requirements.txt

ADD . ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
