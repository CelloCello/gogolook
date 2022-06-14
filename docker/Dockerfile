FROM python:3.7.10-alpine3.13 as builder

WORKDIR /wheels

COPY requirements.txt   .

RUN pip install -U pip \
    && pip wheel -r ./requirements.txt


FROM python:3.7.10-alpine3.13

WORKDIR /root

COPY --from=builder /wheels /wheels

RUN apk --no-cache add bash

RUN pip install -U pip \
   && pip install -r /wheels/requirements.txt -f /wheels \
   && rm -rf /wheels /root/.cache/pip/* \
   && mkdir -p /root/marvin_scripts /root/script_locks

WORKDIR /root/app
COPY ./app    ./app
COPY ./docker/entrypoint.sh     .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/root/app/entrypoint.sh"]
