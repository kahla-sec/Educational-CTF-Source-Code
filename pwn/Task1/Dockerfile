FROM ubuntu:19.10

RUN apt-get upgrade
RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

RUN dpkg --add-architecture i386 && \
    apt-get -y update && \
    apt install -y \
    libc6:i386 \
    libc6-dbg:i386 \
    libc6-dbg \
    lib32stdc++6 \
    g++-multilib

WORKDIR /home/ctf

COPY pwntask .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf

USER ctf
CMD ./ynetd -p 1234 ./pwntask
