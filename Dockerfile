FROM fnndsc/ubuntu-python3

RUN apt-get update && \
    apt-get install -y libmemcached-dev && \
    apt-get install -y zlib1g-dev && \
    apt-get clean

ENV PYTHONUNBUFFERED=0

ADD requirements.txt /
RUN pip install -r requirements.txt

 ADD ./manage.py /manage.py
 ADD ./mighty_ping_pong /mighty_ping_pong
 ADD ./matches /matches
 ADD ./base /base

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
