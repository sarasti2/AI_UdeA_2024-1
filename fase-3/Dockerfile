FROM python

RUN pip install flask loguru pandas pickle

RUN mkdir /app

COPY myrestapi.py /app

WORKDIR /app

CMD flask --app myrestapi run --host=0.0.0.0 