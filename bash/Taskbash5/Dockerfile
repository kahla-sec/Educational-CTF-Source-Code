FROM ubuntu:19.10
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y figlet
RUN apt-get -y install openssh-server
RUN mkdir -p /run/sshd
RUN rm /etc/ssh/sshd_config
RUN rm /etc/legal
RUN chmod -x /etc/update-motd.d/*
COPY welcome /etc/update-motd.d/
RUN chmod +x /etc/update-motd.d/welcome
COPY sshd_config /etc/ssh/
COPY banner /opt/
COPY jail.sh /opt/
RUN useradd -d /home/ctf/ -m -p SecurinetsxKahla -s /opt/jail.sh ctf
RUN echo "ctf:Securinetsxkahla" | chpasswd
RUN service ssh reload
WORKDIR /home/ctf
COPY flag.txt .
RUN chown -R root:root /home/ctf

CMD /bin/sh 
