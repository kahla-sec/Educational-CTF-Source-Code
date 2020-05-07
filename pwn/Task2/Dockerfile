FROM ubuntu:19.10

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf
ARG flag=Securinets{Fmt_StriNgS_Can_Leak_T00}
ENV FLAG=$flag
COPY task .
COPY ynetd .

RUN chown -R root:root /home/ctf

USER ctf
CMD ./ynetd -p 1234 ./task
