FROM ubuntu
ENV TZ=America/Santiago
RUN apt update && apt -y upgrade && apt install -y python3 python3-pip python3-venv pkg-config libmysqlclient-dev && DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
RUN useradd -rm -d /home/user -s /bin/bash -g root -G sudo -u 1001 user
WORKDIR /home/user
RUN python3 -m venv venv && /home/user/venv/bin/pip install --upgrade pip
COPY requirements.txt /home/user
RUN python3 -m venv venv && /home/user/venv/bin/pip install -r requirements.txt
RUN apt-get clean all
RUN . /home/user/venv/bin/activate && django-admin startproject proyecto .
ADD proyecto /home/user/proyecto
ADD app_newfms /home/user/app_newfms
ADD *.py /home/user/
CMD ["/home/user/venv/bin/python", "app.py"]
