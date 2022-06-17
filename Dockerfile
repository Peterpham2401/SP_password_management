FROM python:3.8

WORKDIR /

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY ./app /

CMD ["python","/GM_App.py"]
