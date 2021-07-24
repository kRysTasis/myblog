FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/myblog/api/

RUN apt-get update && apt-get install -y --no-install-recommends \
  net-tools \
  sudo \
  bzip2 \
  curl \
  gcc \
  git \
  python3-dev \
  vim
RUN apt-get clean

ENV DJANGO_ENV production

ADD . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN ls
RUN python manage.py collectstatic --noinput

MAINTAINER admin
ENV USER admin
RUN useradd -m ${USER}
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:test_pass" | chpasswd
USER ${USER}

CMD gunicorn -b 0.0.0.0:$PORT api.wsgi
