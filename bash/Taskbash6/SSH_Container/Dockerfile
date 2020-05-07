FROM ubuntu:19.10
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y figlet
RUN apt-get -y install openssh-server docker.io sudo
RUN mkdir -p /run/sshd
RUN rm /etc/legal
RUN rm /etc/ssh/sshd_config
RUN chmod -x /etc/update-motd.d/*
COPY welcome /etc/update-motd.d/
RUN chmod +x /etc/update-motd.d/welcome
COPY sshd_config /etc/ssh/
COPY banner /opt/
COPY manage.sh /opt/
RUN rm /etc/sudoers
COPY sudoers /etc/
RUN useradd -d /home/ctf/ -m -p SecurinetsxKahla -s /opt/manage.sh ctf
RUN echo "ctf:Securinetsxkahla" | chpasswd
RUN service ssh reload
WORKDIR /home/ctf
RUN chown -R root:root /home/ctf

CMD /bin/sh 

#Add this option when launching container -v /var/run/docker.sock:/var/run/docker.sock
