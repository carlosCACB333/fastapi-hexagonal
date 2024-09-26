
FROM python:3.12-slim AS base



FROM base AS development
ARG APP_PORT
ENV APP_PORT=${APP_PORT}
WORKDIR /code
COPY ./requirements.txt /requirements.txt
RUN pip install -U pytest && pip install -r /requirements.txt
COPY ./ /code/
EXPOSE ${APP_PORT}
CMD ["sh", "-c", "fastapi dev src/main.py --host 0.0.0.0 --port ${APP_PORT}"]



FROM base AS production
ARG APP_PORT
ENV APP_PORT=${APP_PORT}
WORKDIR /code
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./src /code/src
EXPOSE ${APP_PORT}
CMD ["sh", "-c", "fastapi run src/main.py --host 0.0.0.0 --port ${APP_PORT}"]
