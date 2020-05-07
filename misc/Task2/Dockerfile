FROM ubuntu:19.10
RUN apt-get upgrade
RUN apt-get update
RUN apt-get -y install python2 python-pip
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf
COPY requirements.txt .
COPY app.py .
COPY ynetd .
RUN pip install -r requirements.txt
RUN chown -R root:root /home/ctf

USER ctf
CMD ./ynetd -p 1234 "python -u app.py" 2>/dev/null
